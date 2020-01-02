####################################################
#   Python by example
#   Problem: 016
#   Author: Omar Rahman
#   Date:   12//2019
####################################################

##   Problem 016

"""
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”.
"""

raining = input("Is it raining outside? ")

raining = str.lower(raining)

if raining == "yes":
    
    windy = str.lower(input("Is it windy? "))

    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella..")

else:
    print("Enjoy your day..")

####################
#    Problem 017
####################    
"""
Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trickor-
Treating”.

"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick or Treating")






















