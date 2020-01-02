####################################################
#   Python by example
#   Problem : 052 - 059
#   Author: Omar Rahman
#   Date:   1/1/2020
####################################################
import random

#------------------------------------
#   Problem 052
#------------------------------------

def fifty_two():
    number = random.randint(1,100)

    print(number)

# fifty_two()

#------------------------------------
#   Problem 053
#------------------------------------
def fifty_three():
    fruit = random.choice(["banana","apple","orange","guava","blueberry"])

    print(fruit)

# fifty_three()

#------------------------------------
#   Problem 054
#------------------------------------
def fifty_four():
    userSelection = input("choose heads or tails(h/t):")

    computerChoice = random.choice(["h","t"])

    if computerChoice == userSelection:
        print("You Win!")
    else:
        print("Bad luck :(")

    print("Computer selected ",computerChoice)

# fifty_four()


#------------------------------------
#   Problem 056
#------------------------------------

def fifty_six():
    random_number = random.randint(1,10)

    guess = int(input("Enter your selection: "))

    while guess != random_number:
        if guess > random_number:
            print("Too High")
        else:
            print("Too Low")

        guess = int(input("Enter your selection: "))

    print("Congratulations you have picked the number!")

# fifty_six()
