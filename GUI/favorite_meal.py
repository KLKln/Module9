"""
Program: favorite_meal.py
Author: Kelly Klein
Last date modified: 7/1/2020
This program will open a window and prompt user to check a box for favorite meal.
It will then return a somewhat comedic statement about my opinion of said meal
"""
import tkinter


def pick_breakfast():
    label.config(text="Nice choice")


def pick_second_breakfast():
    label.config(text="Excellent choice!")


def pick_lunch():
    label.config(text="Really?")


def pick_dinner():
    label.config(text="Boorriing")


m = tkinter.Tk() #where m is the name of the main window object
m.geometry("250x200")


m.title('Favorite Meal')

label = tkinter.Label(m, text="Waiting")
label.grid(row=5)

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()
var4 = tkinter.IntVar()

check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)
var2.set(0)
var3.set(0)
var4.set(0)

check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)
var1.set(0)
var3.set(0)
var4.set(0)

check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)
var2.set(0)
var1.set(0)
var4.set(0)

check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)
var2.set(0)
var3.set(0)
var1.set(0)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)


m.mainloop() #infinite loop that waits for events to happen
