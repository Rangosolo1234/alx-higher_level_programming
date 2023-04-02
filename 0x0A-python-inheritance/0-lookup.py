#!/usr/bin/python3
def lookup(obj):
    """Function for return the attributes for an object"""    

    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    return attributes + methods
