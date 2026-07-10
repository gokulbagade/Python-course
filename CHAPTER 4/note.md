CHAPTER 4 - LISTS AND TUPLES
Python lists are containers to store a set of values of any data type.

friends= ["apple","akash","rohan",7,false] ☒
            |                     |     |
           str()                int()   bool() 
can store value of any datatype

LIST INDEXING
A list can be indexed just like a string.

L1 = [7,9, "harry"]

L1[0] # 7 
L1[1] # 9
L1[70] # error
L1[0:2] # [7,9] #list slicing

LIST METHODS.

Consider the following list:

L1 = [1,8,7, 2, 21,15]
· L1.sort(): updates the list to [1,2,7,8,15,21]

· L1.reverse(): updates the list to [15,21,2,7,8,1]

· L1.append(8): adds 8 at the end of the list

· L1.insert(3,8): This will add 8 at 3 index

· L1.pop(2): Will delete element at index 2 and return its value.

· L1.remove(21): Will remove 21 from the list.



| Function    | Purpose                             | Example                     | Output      |
| ----------- | ----------------------------------- | --------------------------- | ----------- |
| `append()`  | Adds one element at the end         | `a=[1,2]; a.append(3)`      | `[1,2,3]`   |
| `extend()`  | Adds multiple elements              | `a=[1,2]; a.extend([3,4])`  | `[1,2,3,4]` |
| `insert()`  | Inserts element at a specific index | `a=[1,3]; a.insert(1,2)`    | `[1,2,3]`   |
| `remove()`  | Removes first occurrence of a value | `a=[1,2,3]; a.remove(2)`    | `[1,3]`     |
| `pop()`     | Removes and returns an element      | `a=[1,2,3]; a.pop()`        | `3`         |
| `clear()`   | Removes all elements                | `a=[1,2]; a.clear()`        | `[]`        |
| `index()`   | Returns index of an element         | `a=[10,20,30]; a.index(20)` | `1`         |
| `count()`   | Counts occurrences of an element    | `a=[1,2,2,3]; a.count(2)`   | `2`         |
| `sort()`    | Sorts the list                      | `a=[3,1,2]; a.sort()`       | `[1,2,3]`   |
| `reverse()` | Reverses the list                   | `a=[1,2,3]; a.reverse()`    | `[3,2,1]`   |
| `copy()`    | Creates a copy of the list          | `b=a.copy()`                | Copy of `a` |




**TUPLES IN PYTHON**
A tuple is an immutable data type in python.

a= () # empty tuple

a= (1,) # tuple with only one element needs a comma a= (1,7,2) # tuple with more than one element

TUPLE METHODS
Consider the following tuple.