####################################################
#   Python by example
#   Problem 
#   Author: Omar Rahman
#   Date:   12//2019
####################################################

#------------------------------------
#   String
#   Testing string
#------------------------------------

string = "omar rahman"
text = "  This is some text  "

print(string.capitalize()) # i.e: Omar rahman
print(string.title())      # i.e: Omar Rahman
print(text.strip(" "))     # Removes all the spaces from the text

print("Hello World"[1:5])   # i.e: ello not including the last charector

#------------------------------------
#   Problem 020
#------------------------------------

name = input("Enter your first-name: ")

print("your name has a length of", len(name))
