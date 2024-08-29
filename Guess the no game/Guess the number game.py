import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("Guess the no :"))
    if(a>n):
        print("Lower no please")
        guesses+=1
    elif(a<n):
        print("Higher no please")
        guesses+=1
    
print(f"You guessed the correct no {n} in {guesses} attempts")