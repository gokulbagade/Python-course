s = "  Hello Python  "

print(len(s))
print(s.endswith("rry"))
print(s.startswith("ha"))
print(s.capitalize())


print(len(s))
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("Python", "World"))
print(s.find("Python"))
print(s.count("o"))
print(s.split())
print(s.startswith(" "))
print(s.endswith(" "))


print("Length:", len(s))
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Capitalized:", s.capitalize())
print("Title:", s.title())
print("Replace a with @:", s.replace("a", "@"))
print("Count of a:", s.count("a"))
print("Find e:", s.find("e"))
print("Starts with P:", s.startswith("P"))
print("Ends with n:", s.endswith("n"))
print("Is Alphabet:", s.isalpha())
print("Is Digit:", s.isdigit())
print("Is Alphanumeric:", s.isalnum())
print("Without Spaces:", s.strip())