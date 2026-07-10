CHAPTER 5: DICTIONARY & SETS
Dictionary is a collection of keys-value pairs.

Syntax:

a= {"key":"value", "haÏry":"code", "marks":"100" "list": [1,2,9] }
 a["key"] # prints "value"
 a[list] # prints [1,2,9]

PROPERTIES OF PYTHON DICTIONARIES
1. It is unordered.

2. It is mutable.

3. It is indexed.

4. Cannot contain duplicate keys.

DICTIONARY METHODS
Consider the following dictionary.

a={"name":"harry" "from": "india" "marks": [92,98,96]}

· a.items(): Returns a list of (key,value)tuples.

· a.keys(): Returns a list containing dictionary's keys.

· a.update({"friends":}): Updates the dictionary with supplied key-value pairs.

· a.get("name"): Returns the value of the specified keys (and value is returned eg."harry" is returned here).


| Method         | Purpose                            | Example                       | Output                                      |
| -------------- | ---------------------------------- | ----------------------------- | ------------------------------------------- |
| `get()`        | Gets value of a key                | `d.get("name")`               | `"Gokul"`                                   |
| `keys()`       | Returns all keys                   | `d.keys()`                    | `dict_keys(['name','age'])`                 |
| `values()`     | Returns all values                 | `d.values()`                  | `dict_values(['Gokul',20])`                 |
| `items()`      | Returns key-value pairs            | `d.items()`                   | `dict_items([('name','Gokul'),('age',20)])` |
| `update()`     | Updates/adds key-value pairs       | `d.update({"age":21})`        | Dictionary updated                          |
| `pop()`        | Removes a key                      | `d.pop("age")`                | Removed value                               |
| `popitem()`    | Removes last inserted item         | `d.popitem()`                 | Last key-value pair                         |
| `clear()`      | Removes all items                  | `d.clear()`                   | `{}`                                        |
| `copy()`       | Creates a copy                     | `d.copy()`                    | Copy of dictionary                          |
| `setdefault()` | Returns value; adds key if missing | `d.setdefault("city","Pune")` | `"Pune"`                                    |
| `fromkeys()`   | Creates dictionary from keys       | `dict.fromkeys(["a","b"],0)`  | `{'a':0,'b':0}`                             |




SETS IN PYTHON.
Set is a collection of non-repetitive elements.

S= set()	
s.add(1)  #no repetition allowed!

s.add(2) # or set ={1,2}	


If you are a programming beginner without much knowledge of mathematical operations on sets, you can simply look at sets in python as data types containing unique values.

PROPERTIES OF SETS:-

1. Sets are unordered => Element's order doesn't matter

2. Sets are unindexed => Cannot access elements by index

3. There is no way to change items in sets.

4. Sets cannot contain duplicate values.

| Method                   | Purpose                                    | Example                     | Output                 |
| ------------------------ | ------------------------------------------ | --------------------------- | ---------------------- |
| `add()`                  | Adds one element                           | `s.add(40)`                 | `{10,20,30,40}`        |
| `update()`               | Adds multiple elements                     | `s.update([40,50])`         | `{10,20,30,40,50}`     |
| `remove()`               | Removes an element (error if not found)    | `s.remove(20)`              | `{10,30}`              |
| `discard()`              | Removes an element (no error if not found) | `s.discard(20)`             | `{10,30}`              |
| `pop()`                  | Removes a random element                   | `s.pop()`                   | Random element removed |
| `clear()`                | Removes all elements                       | `s.clear()`                 | `set()`                |
| `copy()`                 | Creates a copy of the set                  | `s.copy()`                  | Copy of set            |
| `union()`                | Combines two sets                          | `A.union(B)`                | All unique elements    |
| `intersection()`         | Common elements                            | `A.intersection(B)`         | Common elements        |
| `difference()`           | Elements in first set only                 | `A.difference(B)`           | Unique to A            |
| `symmetric_difference()` | Elements in either set but not both        | `A.symmetric_difference(B)` | Unique elements        |
| `issubset()`             | Checks if one set is a subset              | `A.issubset(B)`             | `True/False`           |
| `issuperset()`           | Checks if one set is a superset            | `A.issuperset(B)`           | `True/False`           |
| `isdisjoint()`           | Checks if sets have no common elements     | `A.isdisjoint(B)`           | `True/False`           |



OPERATIONS ON SETS
Consider the following set:

s={1,8,2,3}

· len(s): Returns 4, the length of the set

. s.remove(8): Updates the set s and removes 8 from s.

. s.pop(): Removes an arbitrary element from the set and return the element removed.

· s.clear():empties the set s.

· s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.

· s.intersection({8,11}): Return a set which contains only item in both sets {8}.

example :- 
R2 = An B

R1+R2+R3 = AUB

R1+R3=> A A B

R1=> A-B