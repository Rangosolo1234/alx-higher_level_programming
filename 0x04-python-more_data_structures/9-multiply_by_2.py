#!/usr/bin/python3


# multiply_by_2 - Function that returns a new dict values multiplied by 2
def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    for k in new_dict.keys():
        new_dict[k] *= 2
    return (new_dict)
