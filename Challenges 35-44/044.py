#------------------------------------
#   Problem 043
#------------------------------------

"""
044
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.
"""

number_of_people = int(input("How many people do you want in the party? "))

if number_of_people < 10:

    for i in range(10):
        name = input("Enter Guest's Name: ")
        print(name,"has been invited")

else:
    print("Too many people")









