# 2. Write a program to fill in a letter template given below with name and date.
''' letter = Dear < | Name | >, 
           You are selected! ‹ | Date | >

'''

name = str(input("enter your name :"))
date = input("enter a date: ")

letter = f''' Dear {name},\n You are selected!{date}

'''
print(letter)