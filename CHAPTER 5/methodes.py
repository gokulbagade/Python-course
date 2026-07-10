student = {
    "name": "Gokul",
    "age": 20,
    "city": "Shegaon"
}

print("Dictionary:", student)
print("Get:", student.get("name"))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.update({"age": 21})
print("After Update:", student)

student.setdefault("Course", "AI&DS")
print("After SetDefault:", student)

print("Pop:", student.pop("city"))
print("After Pop:", student)

copy_dict = student.copy()
print("Copied Dictionary:", copy_dict)

print("PopItem:", student.popitem())
print("After PopItem:", student)

student.clear()
print("After Clear:", student)