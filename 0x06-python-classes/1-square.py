#!/usr/bin/python3
""" Module: class Square """


class Square():
    """
        Square: defines a square
        Attributes:
            size: size of square
        Method:
                __init__ : initialize size attribute for each instance
    """

    def __init__(self, size):

        """ Initialization of attributes for instances
            Args:
                size: size of the square.
        """
        self.__size = size
