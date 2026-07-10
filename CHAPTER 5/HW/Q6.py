#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("enter your name :")
lang = input("enter your language :")
d.update({name : lang})
name = input("enter your name :")
lang = input("enter your language :")
d.update({name : lang})
name = input("enter your name :")
lang = input("enter your language :")
d.update({name : lang})
name = input("enter your name :")
lang = input("enter your language :")
d.update({name : lang})

print(d)