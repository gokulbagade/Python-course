import calc
print("enter the value of a , b :")
num1=float(input("enter a value of 'a' :"))
num2=float(input("enter a value of 'b' :"))

input_method=input('''  1.add
    2.sub
    3.mult
    4,div ''')

if input_method == "1":
    print(calc.add(num1,num2))
elif input_method == "2":
    print(calc.sub(num1,num2))
elif input_method == "3":
    print(calc.mult(num1,num2))
elif input_method == "4":
    print(calc.div(num1,num2))
else:
    print("Error: add a valid option")

