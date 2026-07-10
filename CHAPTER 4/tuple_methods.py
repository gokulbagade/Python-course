t = (10, 20, 30, 20, 40)

# Print the entire tuple
print("Tuple:", t)

# Count how many times the value 20 appears in the tuple
print("Count of 20:", t.count(20))

# Find the index (position) of the value 30 in the tuple
print("Index of 30:", t.index(30))

# Find and print the total number of elements in the tuple
print("Length:", len(t))

# Find and print the largest element in the tuple
print("Maximum:", max(t))

# Find and print the smallest element in the tuple
print("Minimum:", min(t))

# Calculate and print the sum of all elements in the tuple
print("Sum:", sum(t))

# Return a sorted list containing the tuple's elements and print it
print("Sorted:", sorted(t))


print("---"*50)

# any()
print("Any:", any(t))

# all()
print("All:", all(t))

# enumerate()
print("Enumerate:")
for i, value in enumerate(t):
    print(i, value)

# Concatenation
t2 = (40, 50)
print("Concatenation:", t + t2)

# Repetition
print("Repetition:", t * 2)

# Membership
print("20 in tuple:", 20 in t)
print("100 not in tuple:", 100 not in t)