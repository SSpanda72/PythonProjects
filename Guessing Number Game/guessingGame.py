#This is a Python implementation of Guessing Number Game by Simran Panda
import random

Round = "yes"
while Round == "yes": 

    randomNumber = random.randint(1,10)
    Guess = 0
    Count=0
    while randomNumber != Guess:
        Guess = int(raw_input("Guess my number on a 0-10 scale "))
        Count+=1
        print Count
        if randomNumber > Guess:
            print("Too Low")
        elif randomNumber < Guess:
            print("Too high")
        else:
            print("You guessed my number, it took you " + str(Count) + "tries to guess my number" )
            Round = raw_input("Do you want to play again? ")
            if Round == "yes":
                print("Okay, let's play!")
            else:
                print("It was fun playing!")


