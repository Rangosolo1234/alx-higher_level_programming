#!/usr/bin/python3


# uniq_add - Adds all unique integers in a list, each int once
def uniq_add(my_list=[]):
	unique = set(my_list)
	unique_list = list(unique)
	sum = 0

	for i in unique_list:
		sum += i
	return sum
