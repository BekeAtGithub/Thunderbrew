# functions for actions that the user can use
# for invalid user input - the program will return a list of all available inputs

from tkinter import Y


x = input("")
y = input("")
z = input("")

list = []

if x or y or z == 1:
    list.append("Oats")
if x or y or z == 2:
    list.append("Barley")
if x or y or z == 3:
    list.append("Hops")

print(list)


# will have functions that will put items into inventory when processed

# farm hops will add 1 hop into inventory every 2 seconds

# use quit() to exit game