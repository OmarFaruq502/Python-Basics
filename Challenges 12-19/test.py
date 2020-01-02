####################################################
#   Python by example
#   Problem 
#   Author: Omar Rahman
#   Date:   12//2019
####################################################

##Problem 012

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print("Larger number is ", num1, " Smaller number is ", num2)
else:
    print("Larger number is ", num2, " Smaller number is ", num1)

##Problem 013

num1 = int(input("Enter number under 20: "))

if num1 > 20:
    print("Too High")
else:
    print("Thank You")
    
##Problem 014

num1 = int(input("Enter number between 10 and 20: "))

if num1 >= 10 and num1 <= 20:
    print("Thank You")
else:
    print("Incorrect answer")


##Problem 015

color = input("Enter your favorite color: ")

color = str.lower(color)

if color == 'red':
    print("I like red too")

else:
    print("i dont like ", color," i prefer red")

    
    


