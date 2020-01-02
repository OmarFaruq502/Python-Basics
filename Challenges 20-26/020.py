####################################################
#   Python by example
#   Problem 
#   Author: Omar Rahman
#   Date:   12//2019
####################################################

#------------------------------------
#   Problem 020
#------------------------------------

name = input("Enter your first-name: ")

print("your name has a length of", len(name))

#------------------------------------
#   Problem 021
#------------------------------------

"""
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.

"""
first_name = input("Enter your first-name: ")
sur_name = input("Enter your sur name: ")

full_name = first_name + " "+ sur_name
name_length = len(first_name + sur_name)

print(full_name)
print(name_length)

#------------------------------------
#   Problem 022
#------------------------------------
"""
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.

"""
first_name = str.lower(input("Enter your first-name: "))
sur_name = str.lower(input("Enter your sur name: "))

first_name = first_name.title()
sur_name = sur_name.title()

print(first_name + " " + sur_name)

#------------------------------------
#   Problem 023
#------------------------------------
"""
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).

"""
line = input("Enter line from nursery rhyme song \n=>")

line_length = len(line)

print("Length of the string is", line_length)

start = int(input("Enter starting number: "))
end = int(input("Enter the end line: "))

print(line[start:end])

#------------------------------------
#   Problem 024
#------------------------------------
word = input("Enter a word: ")

print(word.upper())

#------------------------------------
#   Problem 025
#------------------------------------
"""
Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.

"""
firstName = input("Enter your first-name: ")

if len(firstName) < 5 and len(firstName) > 0:
    surName = input("Enter your Surname: ")

    fullName = firstName + surName
    print(fullName.upper())

else:
    print(firstName.lower())

#------------------------------------
#   Problem 026
#------------------------------------
"""
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.

"""
#------------------------------------
#   Pig Latin
#------------------------------------
ay = "ay"
way = "way"

word = input("Enter a word: ")

word = word.lower()

if word[0:1] == "a" or word[0:1] == "e" or word[0:1] == "i" or word[0:1] == "o" or word[0:1] == "u":
    print(word + way)
else:
    first_letter = word[0:1]
    print(word[1:]+first_letter+ay)
