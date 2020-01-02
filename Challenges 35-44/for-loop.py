####################################################
#   Python by example
#   Problem : 035 - 044
#   Author: Omar Rahman
#   Date:   1/1/2020
####################################################

def cleanroom():
    times = int(input("How many times do i have to tell you to clean your room? "))

    for i in range(times):
        print("Go clean your room")

# cleanroom()

def unlucky():
    for i in range(1,20):
        
        if i == 4 or i == 13:
            print(i,"is UNLUCKY!")
        elif (i % 2) == 0:
            print(i,"is even :)")
        else:
            print(i,"is ODD")

# unlucky()

#------------------------------------
#   Problem 035
#------------------------------------

def repeatName():
    name = input("Enter your name ")

    for i in range(3):
        print(name)

# repeatName()

#------------------------------------
#   Problem 036
#------------------------------------
def repeatName_withNumber():
    name = input("Enter your name ")
    number = int(input("Enter the times you wanna repeat? "))

    for i in range(number):
        print(name)

# repeatName_withNumber()

#------------------------------------
#   Problem 037
#------------------------------------

def displayName():
    name = input("Enter your name ")

    for char in name:
        print(char)

# displayName()

#------------------------------------
#   Problem 038
#------------------------------------

def nameDigit():
    name = input("Enter your name: ")
    number = int(input("Enter how many times you wanna repeat this: "))

    for i in range(number):
        for char in name:
            print(char)

# nameDigit()

#------------------------------------
#   Problem 039
#------------------------------------

def multiTable():
    number = int(input("Enter a number between 1 and 12: "))
    
    for i in range(1,13):
        answer = i * number
        print(i, "x",number,"=",answer)

# multiTable()

#------------------------------------
#   Problem 040
#------------------------------------

def countDown():
    number = int(input("Enter a number below 50: "))

    print("You have entered",number)

    for i in range(50, number-1 , -1):
        print(i)

# countDown()





















