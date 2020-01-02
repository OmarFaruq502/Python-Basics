####################################################
#   Python by example
#   Problem 009
#   Author: Omar Rahman
#   Date:   12//2019
####################################################

number_of_days = int(input("Enter number of days: "))

hours = number_of_days * 24
minutes = number_of_days * (60 * 24)
seconds = number_of_days * (24 * 60 * 60)

#alternative
hours_1 = number_of_days * 24
minutes_1 = hours * 60
seconds_1 = minutes * 60

print(number_of_days,"day has", hours, "hours ",minutes,"minutes", seconds,"seconds")
