# 1. Arithmetic operators: +, -, *, / etc.
#  2. Assignment operators: = , +=, -= etc.
# 3. Comparison operators: == , >, >=, <, != etc.
# 4. Logical operators: and, or, not.


# Arithmetic Operators
a = 7
b = 4
c = a + b
d = a-b
e = a * b
f = a / b
g = a % b  # it returns the reminder 
print(c)
print(d)
print(e)
print(f)
print(g)


# Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b)

# Comparison Operators

a = 7       #7 assigne to a
b = 4       # 4 assigne to b
c = a <= b  # if a is less then equal to b then returns true either false
e = a>=b        # if a is greater then equal to b then returns true either false
d = a == b      # if a is equal to b then returns true either false
print(c)
print(e)
print(d)



# Logical Operators

e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))