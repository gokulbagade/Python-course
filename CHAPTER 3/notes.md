We can primarily write a string in these three ways.

a ='harry'	  Single  quoted string
b = "harry"  	Double quoted	string
c = '''harry'''	Triple quoted	string

STRING SLICING
A string in python can be sliced for getting a part of the strings.

Consider the following string:

Name= Ha r r y => Lenght = 5
  0     1    2    3    4 
 (-5) (-4) (-3) (-2) (-1)
The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:

sl = name [indstart: ind end]

first index included

last index is not included


*ESCAPE SEQUENCE CHARACTERS*

Sequence of characters after backslash "\" - Escape Sequence characters

Escape Sequence characters comprise of more than one character but represent one character when used within the strings.

example    \n,     \t      ,    \'       ,        \\       etc.
         newline    tab      singlequote        backslash.