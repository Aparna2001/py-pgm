from random import randint
a=randint(0,9)
# print(a)
s=int(input("Are you ready to begin the game:(0/1) "))
if s==1:
    i=1
    while i<=3:
        n=int(input("Guess a number from 0 to 9 "))
        if n>=0 and n<=9:
            if n==a:
                print("Guess correct")
                break
            else:
                if i==3:
                    print("Game over")
                else:
                    print("Try again")
                i+=1
        else:
            print("Please choose a value from 0 to 9")
            break
else:
    print("See you next time")      