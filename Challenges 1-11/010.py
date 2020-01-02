####################################################
#   Python by example
#   Problem 010,011
#   Author: Omar Rahman
#   Date:   12//2019
####################################################

kilograms = int(input("Enter weight in Kilograms: "))

lbs = kilograms * 2.2046

print("In lbs ", lbs)

# formula => lb = kg * 2.2046

#------------------------------------
#   Problem 11
#------------------------------------

print("------------------------------------")
print("       problem 11                   ")
print("------------------------------------")
num1 = int(input("Enter a number over 100: "))
num2 = int(input("Enter a number less than 10: "))

goes = num1 // num2

print(num2,"goes into",num1,",",goes,"times")
