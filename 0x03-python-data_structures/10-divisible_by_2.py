#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mul_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            mul_list[count] = True
        else:
            mul_list[count] = False
    return(mul_list)
