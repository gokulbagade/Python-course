#1. Write a program to find the greatest of four numbers entered by the user.

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
c = int(input("enter number 3: "))
d = int(input("enter number 4: "))

if (a>b and a>c and a>d):
    print(f"{a} is greater a")
elif(b >a and b>c and b>d):
    print(f"{b} is greater b")
elif(c >a and c>b and c>d):
    print(f"{c} is greater c")
elif(d>a and d>b and d>c):
    print(f"{d} is greater d")
else:
    print("invalid statement")