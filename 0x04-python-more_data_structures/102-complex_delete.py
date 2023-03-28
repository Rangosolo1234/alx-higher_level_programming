#!/usr/bin/python3
def complex_delete(my_dict, value):
    vals = []
    for key, key_value in my_dict.items():
        if key_value is value:
            vals.append(key)
    for k in vals:
        del my_dict[k]
    return(my_dict)
