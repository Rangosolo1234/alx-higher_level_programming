#!/usr/bin/python3

import sys

length = len(sys.argv)
add = 0
if __name__ == "__main__":
    if length == 1:
        add = 0
    else:
        for i in range(1, length):
            add += int(sys.argv[i])
    print("{:d}".format(add))
