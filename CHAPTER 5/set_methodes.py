s = {1,34,5,2,3,6,6,56,3}

print(s,type(s))

s.add(643)

print(s,type(s))
print("----"*40)

A = {10, 20, 30}
B = {20, 30, 40}
print("set A :",A)
print("set B :",B)


A.add(50)
print("After Add:", A)

A.update([60, 70])
print("After Update:", A)

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

print("Subset:", {20, 30}.issubset(A))
print("Superset:", A.issuperset({20, 30}))
print("Disjoint:", A.isdisjoint({100, 200}))

A.remove(70)
print("After Remove:", A)

A.discard(100)
print("After Discard:", A)

copy_set = A.copy()
print("Copied Set:", copy_set)

A.clear()
print("After Clear:", A)