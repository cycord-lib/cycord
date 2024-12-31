from datetime import datetime
class Color:
    """
    A class to represent an RGB color.

    Attributes:
    -----------
    r : int
        Red component of the color.
    g : int
        Green component of the color.
    b : int
        Blue component of the color.

    Methods:
    --------
    __init__(self, red: int, green: int, blue: int) -> None:
        Initializes the Color object with red, green, and blue components.

    set_color(self, red: int, green: int, blue: int) -> None:
        Sets the color using red, green, and blue components.

    hex(self) -> str:
        Returns the hexadecimal string representation of the color.

    __int__(self) -> int:
        Returns the integer representation of the color.

    decimal(self) -> int:
        Returns the decimal representation of the color.

    __repr__(self) -> str:
        Returns the string representation of the Color object.

    __eq__(self, other: object) -> bool:
        Checks if two Color objects are equal.

    from_decimal(decimal_value: int) -> "Color":
        Creates a Color object from a decimal value.

    from_rgb(red: int, green: int, blue: int) -> "Color":
        Creates a Color object from red, green, and blue components.
    """
    r: int
    g: int
    b: int

    def __init__(self, red: int, green: int, blue: int) -> None: ...
    def set_color(self, red: int, green: int, blue: int) -> None: ...
    def hex(self) -> str: ...
    def __int__(self) -> int: ...
    def decimal(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...

    @staticmethod
    def from_decimal(decimal_value: int) -> "Color": ...
    @staticmethod
    def from_rgb(red: int, green: int, blue: int) -> "Color": ...

class Object:
    """
    A class representing an object with an ID and creation timestamp.

    Attributes:
        id (int): The unique identifier for the object.
        created_at (datetime): The timestamp when the object was created.

    Methods:
        __init__(): Initializes a new instance of the Object class.
    """
    id: int
    created_at: datetime

    def __init__(self) -> None: ...