#!/usr/bin/python3
"""
===================================
BaseGeometry class validation methods
===================================
"""

class BaseGeometry:
    """BaseGeometry class contains method"""

    def area(self):
        """Method to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates if value is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
