version = '0.42'

def height():
    return 24

def baseline():
    return 19

def max_width():
    return 21

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 126

_font =\
b'\x0b\x00\x00\x00\x00\x00\x1f\x00\x3f\xc0\x7b\xc0\x71\xc0\x01\xc0'\
b'\x01\xc0\x01\xc0\x03\x80\x07\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00'\
b'\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x30\x30\x30\x30\x00\x00\x30\x78'\
b'\x30\x00\x00\x00\x00\x00\x07\x00\x00\x00\x6e\x6e\x6c\x6c\x6c\x6c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x06\x30\x06\x20\x06\x60\x06\x60\x06\x60'\
b'\x3f\xf8\x3f\xf8\x0c\x40\x0c\xc0\x0c\xc0\x7f\xf8\x7f\xf8\x18\xc0'\
b'\x19\x80\x19\x80\x19\x80\x19\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x03\x00\x03\x00\x0f\x80\x1f\xe0\x3c\xe0\x38\x70'\
b'\x38\x70\x38\x00\x3c\x00\x1f\x00\x0f\xc0\x03\xe0\x00\xf0\x00\x70'\
b'\x70\x70\x70\x70\x3c\xf0\x3f\xe0\x0f\x80\x03\x00\x03\x00\x00\x00'\
b'\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x3f'\
b'\x00\x00\x63\x18\x00\x63\x18\x00\x63\x30\x00\x63\x60\x00\x3f\x60'\
b'\x00\x1e\xc0\x00\x00\xc0\x00\x01\x9c\x00\x03\x3e\x00\x03\x63\x00'\
b'\x06\x63\x00\x0c\x63\x00\x0c\x63\x00\x00\x3e\x00\x00\x1c\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x00\x00\x00\x00\x0f\x80\x1f\xc0\x1d\xe0\x38\xe0\x38\xe0\x39\xc0'\
b'\x1f\xc0\x0f\x00\x1f\x00\x3f\x9c\x73\x9c\x71\xd8\x70\xf8\x70\xf8'\
b'\x79\xf8\x3f\xf8\x0f\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x04\x00\x00\x00\x60\x60\x60\x60\x60\x60\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x02\x07\x0e'\
b'\x1c\x18\x38\x38\x30\x30\x30\x70\x70\x70\x30\x30\x30\x38\x38\x18'\
b'\x1c\x0e\x07\x02\x08\x00\x00\x40\xe0\x70\x38\x18\x1c\x1c\x0c\x0c'\
b'\x0e\x0e\x0e\x0e\x0e\x0c\x0c\x1c\x1c\x18\x38\x70\xe0\x40\x0a\x00'\
b'\x00\x00\x00\x00\x0c\x00\x0c\x00\x0c\x00\x6c\xc0\xff\xc0\x0e\x00'\
b'\x1e\x00\x3b\x00\x33\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00'\
b'\x07\x00\x07\x00\x07\x00\x7f\xf0\x7f\xf0\x7f\xf0\x07\x00\x07\x00'\
b'\x07\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x30\x30\x30\x70\x70\x60\x40\x00\x08\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7e\x7e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x78\x30\x00\x00\x00\x00\x00'\
b'\x09\x00\x00\x00\x00\x00\x03\x00\x03\x00\x07\x00\x06\x00\x06\x00'\
b'\x0c\x00\x0c\x00\x0c\x00\x18\x00\x18\x00\x18\x00\x30\x00\x30\x00'\
b'\x70\x00\x60\x00\x60\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\x0f\x80\x1f\xc0\x3d\xe0\x38\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x38\x70\x3d\xe0\x1f\xc0\x0f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x01\x80\x0f\x80\x3f\x80'\
b'\x3f\x80\x23\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80'\
b'\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x0f\x80\x3f\xe0'\
b'\x39\xe0\x70\xf0\x70\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x03\xc0'\
b'\x07\x80\x0f\x00\x1e\x00\x1c\x00\x38\x00\x7f\xf0\x7f\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x0f\x80'\
b'\x3f\xe0\x79\xe0\x70\x70\x00\x70\x00\x60\x01\xe0\x0f\xc0\x0f\xc0'\
b'\x00\xe0\x00\x70\x00\x70\x70\x70\x70\x70\x79\xe0\x3f\xe0\x0f\x80'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00'\
b'\x01\xe0\x01\xe0\x03\xe0\x07\xe0\x06\xe0\x0e\xe0\x0c\xe0\x1c\xe0'\
b'\x38\xe0\x30\xe0\x70\xe0\x7f\xf8\x7f\xf8\x00\xe0\x00\xe0\x00\xe0'\
b'\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x00\x00\x1f\xf0\x3f\xf0\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xc0'\
b'\x3f\xe0\x38\xf0\x00\x70\x00\x70\x00\x70\x70\x70\x38\x70\x3c\xe0'\
b'\x1f\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x00\x00\x03\xc0\x07\xc0\x1f\x00\x1c\x00\x38\x00\x38\x00'\
b'\x77\xc0\x7f\xe0\x7c\xf0\x70\x70\x70\x70\x70\x70\x70\x70\x38\x70'\
b'\x3c\xe0\x1f\xe0\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x7f\xf0\x7f\xf0\x00\x70\x00\x60\x00\xe0'\
b'\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x07\x00'\
b'\x0e\x00\x0e\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\x0f\x80\x1f\xe0\x3d\xe0\x38\x70'\
b'\x70\x70\x38\x70\x3d\xe0\x1f\xc0\x1f\xc0\x38\xe0\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x3c\xe0\x3f\xe0\x0f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x0f\x80\x1f\xc0\x3d\xe0'\
b'\x70\xe0\x70\x70\x70\x70\x70\x70\x70\x70\x38\xf0\x3f\xf0\x0f\x70'\
b'\x00\x60\x00\xe0\x01\xe0\x07\xc0\x1f\x80\x1e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x38'\
b'\x78\x30\x00\x00\x00\x00\x00\x00\x38\x78\x30\x00\x00\x00\x00\x00'\
b'\x06\x00\x00\x00\x00\x00\x00\x00\x00\x30\x78\x30\x00\x00\x00\x00'\
b'\x00\x00\x30\x30\x30\x30\x70\x60\x60\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x01\xc0\x0f\xc0'\
b'\x3f\x00\x78\x00\x78\x00\x3f\x00\x0f\xc0\x01\xc0\x00\x40\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xe0'\
b'\x3f\xe0\x00\x00\x00\x00\x00\x00\x3f\xe0\x3f\xe0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00'\
b'\x78\x00\x7f\x00\x0f\xc0\x01\xe0\x01\xe0\x0f\xc0\x7f\x00\x78\x00'\
b'\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0b\x00\x00\x00\x00\x00\x1f\x00\x3f\xc0\x7b\xc0\x71\xc0\x01\xc0'\
b'\x01\xc0\x01\xc0\x03\x80\x07\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00'\
b'\x00\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x00'\
b'\x03\xff\x00\x0e\x03\x80\x1c\x00\xc0\x18\x00\x60\x30\x78\x60\x30'\
b'\xfc\x60\x71\xcc\x30\x61\x8c\x30\x63\x8c\x30\x63\x0c\x30\x63\x0c'\
b'\x20\x63\x0c\x60\x63\x9c\x60\x63\xff\xc0\x31\xe7\x80\x30\x00\x00'\
b'\x18\x00\x00\x1e\x00\x00\x07\xfc\x00\x01\xf8\x00\x0f\x00\x00\x00'\
b'\x00\x00\x03\x80\x03\xc0\x07\xc0\x07\xc0\x06\xe0\x0e\xe0\x0e\x60'\
b'\x0c\x70\x1c\x70\x1c\x38\x38\x38\x3f\xf8\x3f\xfc\x78\x1c\x70\x1c'\
b'\x70\x1e\xf0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'\
b'\x00\x00\x00\x00\x3f\xc0\x3f\xf0\x38\xf8\x38\x38\x38\x38\x38\x38'\
b'\x38\x70\x3f\xe0\x3f\xf0\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\xf8\x3f\xf0\x3f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x00\x00\x00\x00\x00\x07\xe0\x0f\xf0\x1e\xf8\x38\x3c\x38\x1c'\
b'\x70\x1c\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x1c\x38\x1c'\
b'\x38\x3c\x1e\xf8\x1f\xf0\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x3f\x80\x3f\xe0\x39\xf0\x38\x78'\
b'\x38\x38\x38\x3c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x3c'\
b'\x38\x38\x38\x78\x39\xf0\x3f\xe0\x3f\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xe0\x3f\xe0\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xf0\x3f\xf0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xe0\x3f\xe0'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x07\xe0'\
b'\x0f\xf8\x1e\x78\x3c\x1c\x38\x1c\x78\x00\x70\x00\x70\x00\x70\xfc'\
b'\x70\xfc\x70\x1c\x78\x1c\x38\x1c\x3c\x1c\x1e\x7c\x0f\xf8\x07\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'\
b'\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e'\
b'\x3f\xfe\x3f\xfe\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e'\
b'\x38\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00\x00\x00\xe0\x00\xe0'\
b'\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0'\
b'\x00\xe0\x00\xe0\x70\xe0\x70\xe0\x79\xe0\x3f\xc0\x1f\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x38\x3c'\
b'\x38\x38\x38\x70\x38\xf0\x39\xe0\x3b\xc0\x3b\x80\x3f\x80\x3f\x80'\
b'\x3f\xc0\x3d\xc0\x38\xe0\x38\xf0\x38\x70\x38\x78\x38\x3c\x38\x1c'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xf0'\
b'\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00'\
b'\x00\x00\x00\x00\x3c\x03\xe0\x3c\x03\xe0\x3c\x03\xe0\x3e\x07\xe0'\
b'\x36\x07\xe0\x36\x06\xe0\x37\x0e\xe0\x33\x0e\xe0\x3b\x8c\xe0\x3b'\
b'\x9c\xe0\x39\x98\xe0\x39\xf9\xe0\x39\xf9\xe0\x38\xf1\xe0\x38\xf1'\
b'\xe0\x38\xf1\xe0\x38\x61\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x38\x0e\x3c\x0e'\
b'\x3c\x0e\x3e\x0e\x3e\x0e\x3f\x0e\x3f\x0e\x3b\x8e\x39\xce\x39\xce'\
b'\x38\xee\x38\xee\x38\x7e\x38\x3e\x38\x3e\x38\x1e\x38\x1e\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x07\xe0'\
b'\x0f\xf0\x1f\xf8\x38\x3c\x38\x1c\x70\x1e\x70\x0e\x70\x0e\x70\x0e'\
b'\x70\x0e\x70\x0e\x70\x1e\x38\x1c\x38\x3c\x1e\xf8\x0f\xf0\x07\xe0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00'\
b'\x3f\xe0\x3f\xf0\x38\x78\x38\x3c\x38\x1c\x38\x1c\x38\x1c\x38\x3c'\
b'\x38\x78\x3f\xf0\x3f\xe0\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00'\
b'\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x00\x07\xe0\x0f\xf0\x1f\xf8\x38\x3c\x38\x1c\x70\x1c\x70\x0e'\
b'\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x1c\x38\x1c\x38\x3c\x1e\xf8'\
b'\x0f\xf0\x07\xf8\x00\x3c\x00\x1c\x00\x08\x00\x00\x00\x00\x0f\x00'\
b'\x00\x00\x00\x00\x3f\xc0\x3f\xf0\x38\xf8\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\xf8\x3f\xf0\x3f\xe0\x38\xe0\x38\xf0\x38\x70'\
b'\x38\x78\x38\x38\x38\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0e\x00\x00\x00\x00\x00\x0f\xc0\x1f\xf0\x3c\xf0\x78\x38\x70\x38'\
b'\x78\x00\x3c\x00\x1f\x80\x0f\xe0\x03\xf0\x00\x78\x00\x38\x70\x38'\
b'\x70\x38\x3c\xf8\x3f\xf0\x0f\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0e\x00\x00\x00\x00\x00\xff\xfc\xff\xfc\x07\x80\x07\x80'\
b'\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80'\
b'\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x70\x1c\x70\x1c\x70\x1c'\
b'\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x70\x1c\x70\x1c'\
b'\x70\x1c\x78\x1c\x38\x38\x3e\xf8\x1f\xf0\x07\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\xf0\x1e\x70\x1c'\
b'\x70\x1c\x78\x3c\x38\x38\x38\x38\x38\x78\x1c\x70\x1c\x70\x1c\x70'\
b'\x0e\xe0\x0e\xe0\x0e\xe0\x07\xc0\x07\xc0\x07\xc0\x03\x80\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00'\
b'\x70\x70\x70\x70\xf0\xe0\x70\xf0\xe0\x70\xf0\xe0\x70\xf8\xe0\x38'\
b'\xf8\xe0\x39\xf9\xc0\x39\xd9\xc0\x39\x99\xc0\x19\x9d\xc0\x1f\x9d'\
b'\xc0\x1f\x8d\x80\x1f\x0f\x80\x1f\x0f\x80\x0f\x0f\x80\x0f\x07\x00'\
b'\x0e\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0f\x00\x00\x00\x00\x00\x70\x3c\x78\x38\x38\x78\x3c\x70'\
b'\x1c\xf0\x0e\xe0\x0f\xc0\x07\xc0\x07\x80\x07\xc0\x0f\xc0\x0e\xe0'\
b'\x1c\xf0\x3c\x70\x38\x78\x78\x38\x70\x3c\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\xf0\x3c\x70\x38\x78\x38'\
b'\x38\x70\x3c\x70\x1c\xe0\x1c\xe0\x0f\xc0\x0f\xc0\x07\x80\x07\x80'\
b'\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x07\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x7f\xf8\x7f\xf8'\
b'\x00\x78\x00\x70\x00\xe0\x01\xe0\x01\xc0\x03\x80\x07\x80\x07\x00'\
b'\x0e\x00\x1e\x00\x1c\x00\x38\x00\x78\x00\x7f\xf8\x7f\xf8\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x7c\x7c\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x7c'\
b'\x7c\x00\x0a\x00\x00\x00\x00\x00\xe0\x00\x70\x00\x70\x00\x70\x00'\
b'\x38\x00\x38\x00\x1c\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x00\x0e\x00'\
b'\x07\x00\x07\x00\x03\x80\x03\x80\x03\x80\x01\xc0\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\xf8\xf8\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\xf8\xf8\x00\x0a\x00'\
b'\x00\x00\x00\x00\x0c\x00\x1e\x00\x1e\x00\x3f\x00\x33\x00\x33\x00'\
b'\x73\x80\x61\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xc0\xff\xc0\x00\x00\x00\x00'\
b'\x00\x00\x07\x00\x00\x00\x70\x38\x1c\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x3f\xc0'\
b'\x79\xe0\x70\xe0\x00\xe0\x1f\xe0\x3f\xe0\x70\xe0\x70\xe0\x79\xe0'\
b'\x7f\xe0\x1e\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x77\xc0'\
b'\x7f\xe0\x7c\xe0\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x7c\xe0\x7f\xe0\x77\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x80\x3f\xc0\x39\xe0\x70\xe0\x70\x60\x70\x00\x70\x00\x70\x00'\
b'\x70\xe0\x39\xe0\x3f\xc0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70'\
b'\x00\x70\x1f\x70\x3f\xf0\x39\xf0\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x39\xf0\x3f\xf0\x1f\x70\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x0f\x80\x1f\xc0\x39\xe0\x70\x60\x70\x70\x7f\xf0'\
b'\x7f\xf0\x70\x00\x70\x00\x3c\xe0\x1f\xe0\x0f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x08\x00\x00\x0f\x1f\x1c\x38\x38\x38\xff'\
b'\xff\x38\x38\x38\x38\x38\x38\x38\x38\x38\x38\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x70\x3f\xf0\x3d\xf0\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x3d\xf0\x3f\xf0\x0f\x70\x00\x70\x00\xf0\x39\xe0\x3f\xc0'\
b'\x0f\x80\x0d\x00\x00\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00'\
b'\x70\x00\x73\xc0\x7f\xe0\x7d\xe0\x70\xf0\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x06\x00\x00\x00\x30\x78\x30\x00\x00\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x00\x00\x00\x00\x00\x07\x00'\
b'\x00\x00\x18\x3c\x18\x00\x00\x38\x38\x38\x38\x38\x38\x38\x38\x38'\
b'\x38\x38\x38\x38\x38\x38\xf8\xf0\x0c\x00\x00\x00\x70\x00\x70\x00'\
b'\x70\x00\x70\x00\x70\x00\x70\x00\x70\xe0\x71\xe0\x73\xc0\x77\x80'\
b'\x7f\x00\x7f\x00\x7f\x00\x7b\x80\x71\xc0\x71\xe0\x70\xe0\x70\x70'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x00'\
b'\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x73\xc7\x80\x7f\xff'\
b'\xc0\x7d\xf9\xc0\x70\xf0\xe0\x70\xe0\xe0\x70\xe0\xe0\x70\xe0\xe0'\
b'\x70\xe0\xe0\x70\xe0\xe0\x70\xe0\xe0\x70\xe0\xe0\x70\xe0\xe0\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0d\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x73\xc0'\
b'\x7f\xe0\x7d\xe0\x70\xf0\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x0f\x80\x3f\xe0\x39\xe0\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x38\xe0\x3f\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x77\xc0\x7f\xe0\x7d\xe0\x70\x70\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x7c\xe0\x7f\xe0\x77\xc0\x70\x00\x70\x00\x70\x00'\
b'\x70\x00\x70\x00\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x1f\x70\x3f\xf0\x39\xf0\x70\x70\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x39\xf0\x3f\xf0\x1f\x70\x00\x70\x00\x70'\
b'\x00\x70\x00\x70\x00\x70\x08\x00\x00\x00\x00\x00\x00\x00\x00\x77'\
b'\x7f\x7f\x78\x70\x70\x70\x70\x70\x70\x70\x70\x00\x00\x00\x00\x00'\
b'\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x1f\x80\x3f\xc0\x71\xe0\x70\xe0\x78\x00\x3f\x00\x0f\xc0\x01\xe0'\
b'\x70\xe0\x70\xe0\x3f\xc0\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x08\x00\x00\x00\x00\x00\x38\x38\x38\xfe\xfe\x38\x38\x38'\
b'\x38\x38\x38\x38\x3c\x3e\x1e\x00\x00\x00\x00\x00\x0d\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x70\x70\x70'\
b'\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\x70\xf0\x39\xf0'\
b'\x3f\xf0\x1e\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0'\
b'\x70\xe0\x71\xc0\x71\xc0\x39\xc0\x39\x80\x3b\x80\x1b\x80\x1f\x00'\
b'\x0f\x00\x0f\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\xe1\xc3\x00\x71\xc7\x00\x71\xc7\x00'\
b'\x73\xe7\x00\x33\x66\x00\x33\x6e\x00\x3f\x6e\x00\x3e\x3e\x00\x1e'\
b'\x3c\x00\x1e\x3c\x00\x1c\x3c\x00\x1c\x1c\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\xe0\x79\xc0\x39\xc0'\
b'\x1f\x80\x1f\x80\x0f\x00\x0f\x00\x1f\x80\x3f\x80\x39\xc0\x71\xc0'\
b'\x70\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\x70\xe0'\
b'\x71\xc0\x71\xc0\x39\xc0\x3b\x80\x3b\x80\x1f\x80\x1f\x00\x1f\x00'\
b'\x0f\x00\x0e\x00\x0e\x00\x0e\x00\x1c\x00\x7c\x00\x78\x00\x0c\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xe0'\
b'\x7f\xe0\x01\xc0\x03\x80\x07\x80\x0f\x00\x0e\x00\x1c\x00\x3c\x00'\
b'\x78\x00\x7f\xe0\x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x08\x00\x00\x06\x0e\x1c\x1c\x18\x18\x18\x18\x18\x38\x70\x70\x38'\
b'\x18\x18\x18\x18\x18\x1c\x1c\x0e\x06\x00\x06\x00\x00\x00\x30\x30'\
b'\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'\
b'\x30\x30\x00\x00\x08\x00\x00\x40\xf0\x30\x38\x38\x38\x38\x38\x38'\
b'\x1c\x0e\x1e\x1c\x38\x38\x38\x38\x38\x38\x30\xf0\x40\x00\x0f\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x1e\x0c\x3f\x1c\x3b\xb8\x71\xf8\x70\xf0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

_index =\
b'\x00\x00\x32\x00\x4c\x00\x66\x00\x80\x00\xb2\x00\xe4\x00\x2e\x01'\
b'\x60\x01\x7a\x01\x94\x01\xae\x01\xe0\x01\x12\x02\x2c\x02\x46\x02'\
b'\x60\x02\x92\x02\xc4\x02\xf6\x02\x28\x03\x5a\x03\x8c\x03\xbe\x03'\
b'\xf0\x03\x22\x04\x54\x04\x86\x04\xa0\x04\xba\x04\xec\x04\x1e\x05'\
b'\x50\x05\x82\x05\xcc\x05\xfe\x05\x30\x06\x62\x06\x94\x06\xc6\x06'\
b'\xf8\x06\x2a\x07\x5c\x07\x76\x07\xa8\x07\xda\x07\x0c\x08\x56\x08'\
b'\x88\x08\xba\x08\xec\x08\x1e\x09\x50\x09\x82\x09\xb4\x09\xe6\x09'\
b'\x18\x0a\x62\x0a\x94\x0a\xc6\x0a\xf8\x0a\x12\x0b\x44\x0b\x5e\x0b'\
b'\x90\x0b\xc2\x0b\xdc\x0b\x0e\x0c\x40\x0c\x72\x0c\xa4\x0c\xd6\x0c'\
b'\xf0\x0c\x22\x0d\x54\x0d\x6e\x0d\x88\x0d\xba\x0d\xd4\x0d\x1e\x0e'\
b'\x50\x0e\x82\x0e\xb4\x0e\xe6\x0e\x00\x0f\x32\x0f\x4c\x0f\x7e\x0f'\
b'\xb0\x0f\xfa\x0f\x2c\x10\x5e\x10\x90\x10\xaa\x10\xc4\x10\xde\x10'\
b'\x10\x11'

_mvfont = memoryview(_font)
_mvi = memoryview(_index)
ifb = lambda l : l[0] | (l[1] << 8)

def get_ch(ch):
    oc = ord(ch)
    ioff = 2 * (oc - 32 + 1) if oc >= 32 and oc <= 126 else 0
    doff = ifb(_mvi[ioff : ])
    width = ifb(_mvfont[doff : ])

    next_offs = doff + 2 + ((width - 1)//8 + 1) * 24
    return _mvfont[doff + 2:next_offs], 24, width

