"""
Program: dictionary_ops.py
Author: Kelly Klein
Last date modified: 7/1/2020
This program will accept a dictionary and print it's contents one key value pair
at a time
"""


def print_dict(new_dict = {'Flint': 'Dwarf', 'Tasslehof': 'Kender', 'Tanis': 'Half-Elf'}):
    for k, v in new_dict.items():
        print(k,':',v)


if __name__ == '__main__':
    print_dict()
