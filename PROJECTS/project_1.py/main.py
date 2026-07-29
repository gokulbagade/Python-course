import random

dict ={ "s":1 ,"w":-1 ,"g":0}
reversedict = {1 : "snake", -1 :"water" , 0 : "gun"}
you=str(input("enter 's','w','g' : "))
youstr = dict[you]
bot = random.choice([1,-1,0])

print(f"bot choice : {reversedict[bot]} \n you choice : {reversedict[youstr]}")

if bot == youstr :
    print("it's a taie !")
elif bot == 1 and youstr == -1 :
    print("bot win !")
elif bot == 1 and youstr == 0 :
    print("you win !")
elif bot == -1 and youstr == 0 :
    print("bot win !")
elif bot == -1 and youstr ==  1:
    print("you win !")
elif bot == 0 and youstr == -1 :
    print("you win !")
elif bot == 0 and youstr == 1 :
    print("bot win !")
else:
    print("something is wrong")
