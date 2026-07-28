#7. Write a program to find out whether a given post is talking about "pig" or not.

post = input("enter the post : ")

if "pig".lower() in post.lower():
    print("relited to pig")
else:
    print("not relited to pig")