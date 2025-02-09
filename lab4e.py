#!/usr/bin/env python3
# Author: asaini85

def is_digits(s):
    return s.isdigit()

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(f"{item} is an integer.")
        else:
            print(f"{item} is not an integer.")
