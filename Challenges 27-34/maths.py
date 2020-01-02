####################################################
#   Python by example
#   Problem : 027 - 034
#   Author: Omar Rahman
#   Date:   12//2019
####################################################
import math

#------------------------------------
#   Problem 027
#------------------------------------
"""
Ask the user to enter a
number with lots of
decimal places. Multiply
this number by two and
display the answer.

"""
number = float(input("Enter a number with lots decimal places: "))

answer = number * 2

print(answer)

#------------------------------------
#   Problem 028
#------------------------------------
print(round(answer,2)) #rounds the number by 2 places


#------------------------------------
#   Problem 029
#------------------------------------
num = int(input("Enter a number over 500: "))

sqrt = math.sqrt(num)

if num > 500:

    print("Square root for that number is", round(sqrt,2))

else:
    print("Invalid input")

#------------------------------------
#   Problem 030
#------------------------------------
pi = math.pi

print(round(pi,5))

#------------------------------------
#   Problem 031
#------------------------------------
radius = float(input("Enter the radius: "))

area = math.pi * (radius ** 2) # (pi * radius ^ 2)

#------------------------------------
#   Problem 032
#------------------------------------

radius = float(input("Enter the radius: "))
depth = float(input("Enter the depth: "))
area = math.pi * (radius ** 2)

volume = depth * area
print(round(volume,3))

#------------------------------------
#   Problem 034
#------------------------------------

display ="""
  1) Square
  2) Triangle
""" 
print(display)

choice = int(input("Enter choice: "))

if choice == 1:
    side = int(input("Enter lenth of one side: "))
    area = side * side
    print(area)

elif choice == 2:
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: ")) 

    area = 1/2 * base * height
    print(area)
else:
    print("Invalid entry")
    
















