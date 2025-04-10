# writer.py Implements the Writer class.
# Handles colour, word wrap and tab stops

# V0.5.1 Dec 2022 Support 4-bit color display drivers.
# V0.5.0 Sep 2021 Color now requires firmware >= 1.17.
# V0.4.3 Aug 2021 Support for fast blit to color displays (PR7682).
# V0.4.0 Jan 2021 Improved handling of word wrap and line clip. Upside-down
# rendering no longer supported: delegate to device driver.
# V0.3.5 Sept 2020 Fast rendering option for color displays

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2019-2021 Peter Hinch

# A Writer supports rendering text to a Display instance in a given font.
# Multiple Writer instances may be created, each rendering a font to the
# same Display object.

# Timings were run on a pyboard D SF6W comparing slow and fast rendering
# and averaging over multiple characters. Proportional fonts were used.
# 20 pixel high font, timings were 5.44ms/467μs, gain 11.7 (freesans20).
# 10 pixel high font, timings were 1.76ms/396μs, gain 4.36 (arial10).


import framebuf

__version__ = (0, 5, 1)

fast_mode = True  # Does nothing. Kept to avoid breaking code.


class DisplayState():
    def __init__(self):
        self.text_row = 0
        self.text_col = 0


def _get_id(device):
    if not isinstance(device, framebuf.FrameBuffer):
        raise ValueError('Device must be derived from FrameBuffer.')
    return id(device)

# Basic Writer class for monochrome displays


class Writer():
    """
    A class for writing text on a display device.

    Attributes:
    - state: Holds a display state for each device

    Methods:
    - set_textpos: Sets the text position on the display
    - __init__: Initializes the Writer object
    - _getstate: Returns the display state for the device
    - _newline: Moves the text position to the next line
    - set_clip: Sets the clipping and wrapping options for text printing
    - height: Returns the height of the font
    - printstring: Prints a string of text on the display
    - _printline: Prints a line of text on the display
    - stringlen: Returns the length of a string in pixels
    - _truelen: Returns the printable width of a glyph
    - _get_char: Gets the glyph and dimensions of a character
    - _printchar: Prints a character on the display
    - tabsize: Sets the size of a tab
    - setcolor: Sets the foreground and background colors
    - clear_line: Clears a line on the display
    - mytext_both_side: Prints two strings on the same line, one on each side
    - mytext: Prints a string on a specific line and column
    """
    state = {}  # Holds a display state for each device

    @staticmethod
    def set_textpos(device, row=None, col=None):
        """
        Sets the text position on the display.

        Args:
        - device: The display device
        - row: The row number (optional)
        - col: The column number (optional)

        Returns:
        - The current text row and column
        """
        devid = _get_id(device)
        if devid not in Writer.state:
            Writer.state[devid] = DisplayState()
        s = Writer.state[devid]  # Current state
        if row is not None:
            if row < 0 or row >= device.height:
                raise ValueError('row is out of range')
            s.text_row = row
        if col is not None:
            if col < 0 or col >= device.width:
                raise ValueError('col is out of range')
            s.text_col = col
        return s.text_row,  s.text_col

    def __init__(self, device, font, verbose=True, header_height=2, line_space=3):
        """
        Initializes the Writer object.

        Args:
        - device: The display device
        - font: The font used for text rendering
        - verbose: Whether to print verbose information (default: True)
        - header_height: Height of the header (default: 2)
        - line_space: Space between lines (default: 3)
        """
        self.devid = _get_id(device)
        self.device = device
        if self.devid not in Writer.state:
            Writer.state[self.devid] = DisplayState()
        self.font = font
        if font.height() >= device.height or font.max_width() >= device.width:
            raise ValueError('Font too large for screen')
        # Allow to work with reverse or normal font mapping
        if font.hmap():
            self.map = framebuf.MONO_HMSB if font.reverse() else framebuf.MONO_HLSB
        else:
            raise ValueError('Font must be horizontally mapped.')
        if verbose:
            fstr = 'Orientation: Horizontal. Reversal: {}. Width: {}. Height: {}.'
            print(fstr.format(font.reverse(), device.width, device.height))
            print('Start row = {} col = {}'.format(
                self._getstate().text_row, self._getstate().text_col))
        self.screenwidth = device.width  # In pixels
        self.screenheight = device.height
        self.bgcolor = 0  # Monochrome background and foreground colors
        self.fgcolor = 1
        self.invert = False # Invert colors
        self.row_clip = False  # Clip or scroll when screen fullt
        self.col_clip = False  # Clip or new line when row is full
        self.wrap = False  # Word wrap
        self.cpos = 0
        self.tab = 4

        self.glyph = None  # Current char
        self.char_height = 0
        self.char_width = 0
        self.clip_width = 0

        # calculate line row position
        self.lines = []
        rows = header_height
        while rows + font.height() <= self.screenheight:
            self.lines.append(rows)
            rows += font.height() + line_space
        print(f"{len(self.lines)} lines available: {self.lines}")

    def _getstate(self):
        """
        Returns the display state for the device.

        Returns:
        - The display state
        """
        return Writer.state[self.devid]

    def _newline(self):
        """
        Moves the text position to the next line.
        """
        s = self._getstate()
        height = self.font.height()
        s.text_row += height
        s.text_col = 0
        margin = self.screenheight - (s.text_row + height)
        y = self.screenheight + margin
        if margin < 0:
            if not self.row_clip:
                self.device.scroll(0, margin)
                self.device.fill_rect(
                    0, y, self.screenwidth, abs(margin), self.bgcolor)
                s.text_row += margin

    def set_clip(self, row_clip=None, col_clip=None, wrap=None):
        """
        Sets the clipping and wrapping options for text printing.

        Args:
        - row_clip: Whether to clip or scroll when the screen is full (optional)
        - col_clip: Whether to clip or start a new line when a row is full (optional)
        - wrap: Whether to enable word wrap (optional)

        Returns:
        - The current row_clip, col_clip, and wrap options
        """
        if row_clip is not None:
            self.row_clip = row_clip
        if col_clip is not None:
            self.col_clip = col_clip
        if wrap is not None:
            self.wrap = wrap
        return self.row_clip, self.col_clip, self.wrap

    @property
    def height(self):
        """
        Returns the height of the font.

        Returns:
        - The font height
        """
        return self.font.height()

    def printstring(self, string, invert=False):
        """
        Prints a string of text on the display.

        Args:
        - string: The string to print
        - invert: Whether to invert the colors (default: False)
        """
        # word wrapping. Assumes words separated by single space.
        q = string.split('\n')
        last = len(q) - 1
        for n, s in enumerate(q):
            if s:
                self._printline(s, invert)
            if n != last:
                self._printchar('\n')

    def _printline(self, string, invert):
        """
        Prints a line of text on the display.

        Args:
        - string: The line of text to print
        - invert: Whether to invert the colors
        """
        rstr = None
        # Length > self.screenwidth
        if self.wrap and self.stringlen(string, True):
            pos = 0
            lstr = string[:]
            while self.stringlen(lstr, True):  # Length > self.screenwidth
                pos = lstr.rfind(' ')
                lstr = lstr[:pos].rstrip()
            if pos > 0:
                rstr = string[pos + 1:]
                string = lstr

        for char in string:
            self._printchar(char, invert)
        if rstr is not None:
            self._printchar('\n')
            self._printline(rstr, invert)  # Recurse

    def stringlen(self, string, oh=False):
        """
        Returns the length of a string in pixels.

        Args:
        - string: The string to measure
        - oh: Whether to consider overhang (default: False)

        Returns:
        - The length of the string in pixels
        """
        if not len(string):
            return 0
        sc = self._getstate().text_col  # Start column
        wd = self.screenwidth
        l = 0
        for char in string[:-1]:
            _, _, char_width = self.font.get_ch(char)
            l += char_width
            if oh and l + sc > wd:
                return True  # All done. Save time.
        char = string[-1]
        _, _, char_width = self.font.get_ch(char)
        if oh and l + sc + char_width > wd:
            l += self._truelen(char)  # Last char might have blank cols on RHS
        else:
            l += char_width  # Public method. Return same value as old code.
        return l + sc > wd if oh else l

    def _truelen(self, char):
        """
        Returns the printable width of a glyph less any blank columns on the right-hand side.

        Args:
        - char: The character to measure

        Returns:
        - The printable width of the glyph
        """
        glyph, ht, wd = self.font.get_ch(char)
        div, mod = divmod(wd, 8)
        gbytes = div + 1 if mod else div  # No. of bytes per row of glyph
        mc = 0  # Max non-blank column
        data = glyph[(wd - 1) // 8]  # Last byte of row 0
        for row in range(ht):  # Glyph row
            for col in range(wd - 1, -1, -1):  # Glyph column
                gbyte, gbit = divmod(col, 8)
                if gbit == 0:  # Next glyph byte
                    data = glyph[row * gbytes + gbyte]
                if col <= mc:
                    break
                if data & (1 << (7 - gbit)):  # Pixel is lit (1)
                    mc = col  # Eventually gives rightmost lit pixel
                    break
            if mc + 1 == wd:
                break  # All done: no trailing space
        return mc + 1

    def _get_char(self, char, recurse):
        """
        Gets the glyph and dimensions of a character.

        Args:
        - char: The character to get
        - recurse: Whether to handle tabs and newlines

        Returns:
        - The glyph, character height, and character width
        """
        if not recurse:  # Handle tabs
            if char == '\n':
                self.cpos = 0
            elif char == '\t':
                nspaces = self.tab - (self.cpos % self.tab)
                if nspaces == 0:
                    nspaces = self.tab
                while nspaces:
                    nspaces -= 1
                    self._printchar(' ', recurse=True)
                self.glyph = None  # All done
                return

        self.glyph = None  # Assume all done
        if char == '\n':
            self._newline()
            return
        glyph, char_height, char_width = self.font.get_ch(char)
        s = self._getstate()
        np = None  # Allow restriction on printable columns
        if s.text_row + char_height > self.screenheight:
            if self.row_clip:
                return
            self._newline()
        oh = s.text_col + char_width - self.screenwidth  # Overhang (+ve)
        if oh > 0:
            if self.col_clip or self.wrap:
                np = char_width - oh  # No. of printable columns
                if np <= 0:
                    return
            else:
                self._newline()
        self.glyph = glyph
        self.char_height = char_height
        self.char_width = char_width
        self.clip_width = char_width if np is None else np

    # Method using blitting. Efficient rendering for monochrome displays.
    # Tested on SSD1306. Invert is for black-on-white rendering.
    def _printchar(self, char, invert=False, recurse=False):
        s = self._getstate()
        self._get_char(char, recurse)
        if self.glyph is None:
            return  # All done
        buf = bytearray(self.glyph)
        if invert:
            for i, v in enumerate(buf):
                buf[i] = 0xFF & ~ v
        fbc = framebuf.FrameBuffer(
            buf, self.clip_width, self.char_height, self.map)
        self.device.blit(fbc, s.text_col, s.text_row)
        s.text_col += self.char_width
        self.cpos += 1

    def tabsize(self, value=None):
        if value is not None:
            self.tab = value
        return self.tab

    def setcolor(self, *_):
        return self.fgcolor, self.bgcolor

    def get_num_lines(self) -> int:
        """Return the total number of lines on the display."""
        return len(self.lines)

    def clear_line(self, line: int) -> bool:
        """Clear a line on the display.

        Args:
            line (int): line number (starting from 0)

        Returns:
            bool: True if successful, False otherwise (invalid line number)
        """
        if self.invert:
            colour = 0xff
        else:
            colour = 0x00
        if line < len(self.lines):
            row = self.lines[line]
            
            if self.invert:
                self.set_textpos(self.device, 0, row)
                self.device.rect(0, row, self.screenwidth,
                                self.font.height(), colour, True)
            else:
                self.set_textpos(self.device, row, 0)
                self.device.fill_rect(colour, row, self.screenwidth,
                                      self.font.height(), self.bgcolor)
            return True
        else:
            print("Invalid line number, no action taken")
            return False

    def mytext(self, string: str, line: int, col: int = 0, invert: bool | None = None) -> bool:
        """Print text on a specific line and column.

        Args:
            string (str): text to print
            line (int): line number (starting from 0)
            col (int, optional): column pixel position. Defaults to 0.
            invert (bool, optional): invert option of internal printstring function. Default to read from `Writer.invert`.

        Returns:
            bool: True if successful, False otherwise
        """
        if invert is None:
            invert = self.invert

        if self.stringlen(string) > self.screenwidth:
            print("Warning: Input string too long for one line")

        if line < len(self.lines):
            row = self.lines[line]
            self.set_textpos(self.device, row, col)
            self.printstring(string, invert)
            return True
        else:
            print("Invalid line number, no action taken")
            return False

    def mytext_both_side(self, string1: str, string2: str, line: int, invert: bool | None = None) -> bool:
        """Print two strings on the same line, one on each side.

        Args:
            string1 (str): Text on the left side
            string2 (str): Text on the right side
            line (int): line number (starting from 0)
            invert (bool, optional): invert option of internal printstring function. Defaults to False.

        Returns:
            bool: True if successful, False otherwise
        """
        if invert is None:
            invert = self.invert

        stringlen1 = self.stringlen(string1)
        stringlen2 = self.stringlen(string2)

        if stringlen1 + stringlen2 > self.screenwidth:
            string1_strip = ""
            while self.stringlen(string1_strip + string2) < self.screenwidth:
                string1_strip += string1[0]
                string1 = string1[1:]
            string1 = string1_strip[:-1]  # Remove the last char

        self.mytext(string1, line)
        self.mytext(string2, line, col=int(self.screenwidth-stringlen2))
        return True
