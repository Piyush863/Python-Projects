import random
computer=random.choice([1, -1, 0])
youstr = input("Enter your Choice :")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}

you=youdict[youstr]

print(f"You choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer==you):
    print("Draw")
    
else:
    if(computer==-1 and you==1):
        print("You win")
    
    elif(computer==-1 and you==0):
        print("You lose")

    elif(computer==1 and you==-1):
        print("You lose")

    elif(computer==1 and you==0):
        print("You win")

    elif(computer==0 and you==-1):
        print("You Win")

    elif(computer==0 and you==1):
        print("You lose")
    
    else:
        print("Something went wrong")

   