#Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

#specify the dirctory path
path=input("enter directory path :")

#print the context of the directory
try:
    contents=os.listdir(path)
    print("contents of directory")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("directory not found")
except PermissionError:
    print("permission denine")