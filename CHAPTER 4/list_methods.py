list1 = [30, 10, 20]

list1.append(40)
list1.extend([50, 60])
list1.insert(1, 15)
print(list1)
print("List:", list1)
print("Count of 20:", list1.count(20))
print("Index of 30:", list1.index(30))
print("Length:", len(list1))
print("Maximum:", max(list1))
print("Minimum:", min(list1))
print("Sum:", sum(list1))

list2 = list1.copy()
print("Copied List:", list2)

list1.sort()
print("Sorted:", list1)

list1.reverse()
print("Reversed:", list1)

list1.pop()
print("After Pop:", list1)

list1.remove(15)
print("After Remove:", list1)

list1.clear()
print("After Clear:", list1)