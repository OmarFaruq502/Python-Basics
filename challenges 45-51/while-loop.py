####################################################
#   Python by example
#   Problem : 045 - 051
#   Author: Omar Rahman
#   Date:   1/1/2020
####################################################

#------------------------------------
#   Problem 045
#------------------------------------

def fourty_five():
    total = 0

    while total <= 50:
        num = int(input("Enter a number: "))
        total += num

        if(total > 50):
            break

        print("The total is:",total)

# fourty_five()

#------------------------------------
#   Problem 046
#------------------------------------

def fourty_six():
    num = int(input("Enter a number: "))

    while num <= 5:
        num = int(input("Enter a number: "))

    print("The last number you entered was a",num)

# fourty_six()


#------------------------------------
#   Problem 047
#------------------------------------

def fourty_seven():
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))

    sum = num1 + num2

    choice = input("Would you like to add more number?(y/n) ")

    while choice == 'y':
        
        num3 = int(input("Enter a number: ",))

        sum += num3

        choice = input("Would you like to add more number?(y/n) ")

    print("Total is",sum)

# fourty_seven()

#------------------------------------
#   Problem 048
#------------------------------------

def fourty_eight():
    name = input("Enter guest's name: ")
    print(name,"has been invited to the party")
    count = 1
    choice = input("would you like to add more people to the party? ")

    while choice == "y":
        name = input("Enter guest's name: ")
        print(name,"has been invited to the party")
        count += 1

        choice = input("would you like to add more people to the party? ")
    print(count,"number of people are coming to the party")

# fourty_eight()

#------------------------------------
#   Problem 049
#------------------------------------

def fourty_nine():
    compnum = 50
    

    guess = int(input("Enter a number: ",))
    count = 1

    while guess != compnum:

        count += 1

        if guess > compnum:
            print("Too High")

        elif guess < compnum:
            print("Too Low")
        
        guess = int(input("Enter a number: ",))
        
    print("It has taken you",count,"tries")

# fourty_nine()
