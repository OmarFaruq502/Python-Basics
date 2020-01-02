
#------------------------------------
#   Problem 059
#   Subject: color guessing game
#------------------------------------
import random

"""
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.
"""

display = """
    1) Blue
    2) Orange
    3) Red
    4) Green
    5) Black
"""

randomColor =  random.choice(["Blue","Orange","Red","Green","Black"])

blue_response = "You are probably feeling BLUE right now"
orange_response = "I am feeling a Fresh morning juice vibe"
red_response = "You are RED with anger"
green_response = "I bet you are green with envy"
black_response = "Damn Black is illegal"

print(display)
choice = input("Enter your choice?: ")

randomColor = str.lower(randomColor)
choice = str.lower(choice)

while choice == randomColor:
    if choice == "blue":
        print(blue_response)
    elif choice == "orange":
        print(orange_response)
    elif choice == "red":
        print(red_response)
    elif choice == "green":
        print(green_response)
    elif choice == "black":
        print(black_response)

    choice = input("Enter your choice?: ")

print("Well Done!!")