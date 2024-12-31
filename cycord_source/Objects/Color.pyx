cdef class Color:
    cdef unsigned char r, g, b

    def __cinit__(self, unsigned char red, unsigned char green, unsigned char blue):
        self.r = red
        self.g = green
        self.b = blue

    cpdef void set_color(self, unsigned char red, unsigned char green, unsigned char blue):
        self.r = red
        self.g = green
        self.b = blue

    cpdef str hex(self):
        return '#{:02X}{:02X}{:02X}'.format(self.r, self.g, self.b)

    def __int__(self):
        return self.decimal()

    cpdef int decimal(self):
        return (self.r << 16) | (self.g << 8) | self.b

    def __repr__(self):
        return f"Color(r={self.r}, g={self.g}, b={self.b})"

    def __eq__(self, other):
        if type(other) is Color:
            return self.r == other.r and self.g == other.g and self.b == other.b
        elif type(other) is int:
            return self.r == ((other >> 16) & 0xFF) and self.g == ((other >> 8) & 0xFF) and self.b == (other & 0xFF)
        return False

    @staticmethod
    def from_decimal(decimal_value: int):
        '''Change to cython when staticmethod support is added'''
        return Color(
            red=(decimal_value >> 16) & 0xFF,
            green=(decimal_value >> 8) & 0xFF,
            blue=decimal_value & 0xFF
        )

    @staticmethod
    def from_rgb(red: int, green: int, blue: int):
        '''Change to cython when staticmethod support is added'''
        return Color(red, green, blue)