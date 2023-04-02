#!/usr/bin/python3
"""
===================================
-------------------------------
===================================
"""


def inherits_from(obj, a_class):
    """Returns true if object is inherited from class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
