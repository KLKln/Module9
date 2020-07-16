"""
Program: my_definitions_test.py
Author: Kelly Klein
Last date modified: 7/1/2020
This program will test the modules written by me
"""

from my_definitions import greeting
from my_definitions import me_as_author
from my_definitions import print_dict
from my_definitions import print_set

if __name__ == '__main__':

    greeting()
    me_as_author()
    print_dict()
    new_dict = {'Slayer': 'Reign In Blood', 'Green Day': 'Dookie', 'Direct Hit!': 'Crown of Nothing', 'Strapping Young Lad': 'Heavy as a Really Heavy Thing'}
    print_dict(new_dict)
    print_set()
    even_set = {2,4,6,8,10,12}
    print_set(even_set)
