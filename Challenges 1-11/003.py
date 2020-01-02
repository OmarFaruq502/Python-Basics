####################################################
#   Python by example
#   Problem 003, 004, 005, 006, 007, 008
#   Author: Omar Rahman
#   Date:   12//2019
####################################################
print("-----------------------------------")
print("            Problem 3              ")
print("-----------------------------------")

print("What would you call a bear with no teeth?\nA Gummy bear!")

print("-----------------------------------")
print("            Problem 4              ")
print("-----------------------------------")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

total = num1 + num2
print("The Total is " + str(total))

print("-----------------------------------")
print("            Problem 5              ")
print("-----------------------------------")

num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))

total = num3 + num4
answer = total * num5
print("The answer is " + str(answer))

print("-----------------------------------")
print("            Problem 6              ")
print("-----------------------------------")

wholePizza = int(input("How many Pizza Slices were there?: "))
pizzaEaten = int(input("How many did you eat?: "))

remainingPizza = wholePizza - pizzaEaten
print("Pizza left: " + str(remainingPizza))

print("-----------------------------------")
print("            Problem 7              ")
print("-----------------------------------")

name = input("What is your name? => ")
age = int(input("How old are you? => "))

newAge = age + 1

print(name +" next birthday you will be",newAge) # this could be done with a comma as well

print("-----------------------------------")
print("            Problem 8              ")
print("-----------------------------------")

bill = int(input("How much is the bill: "))
diners = int(input("How many diners were there: "))

payment = bill / diners

print("Each Diner should pay $",payment)



















