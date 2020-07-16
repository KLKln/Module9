"""
Program: my_definitions.py
Author: Kelly Klein
Last date modified: 7/1/2020
This program will contains modules written by me to be tested
in my_definitions_test
"""


def greeting():
    user_name = input("Please enter your name: ")
    print('Hello', user_name, ', good to meet you!')


def me_as_author():
    print('Kelly Klein wrote this code!')


def print_dict(new_dict = {"Book1" : 365, "Book2" : 800, "Book3" : 543, "Book4" : 198}):

    for k, v in new_dict.items():
        print(k,':',v)



def print_set(new_set = {1,3,5,7,9,11,13}):

    for i in new_set:
        print(i)

