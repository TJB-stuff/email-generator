# Author: Tyler Black
# Description: This is a header
# Date Created: March 26, 2020
# Date Modified: March 27, 2020

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280"
ask1 = input("What is your first name? (at least 4 letters): ")
int_1 = len(ask1)
minimum = 4
is_greater = int_1 >= minimum
print("Your name is at least 4 characters long: " + str(is_greater))
ask2 = input("What is your last name?: ")
int_2 = len(ask2)
ask3 = input("How old are you?: ")
age = int(ask3)
ask4 = input("Birth month? (print this as a word): ")
end = "@compsci.ca"
first_letter = (ask1[0])
last_letter = (ask2[-1])
first_letter_month = (ask4[0])
month_len = len(ask4)
print("Here are the first 100 digits in pi: " + (pi))
print("The length of your first name is: " + str(int_1))
print("The length of your last name is: " + str(int_2))
print("Your age is: " + str(ask3))
print("The first letter of your first name is: " + (first_letter))
print("The last letter of your last name is: " + (last_letter))
print("The first letter of your birth month is: " + (first_letter_month))
math_calculation = (int_1 + int_2 + age)
print("The value of the length of your first and last names, and your age is: " + str(math_calculation))
print ("In pi, character " + str(math_calculation) + " is " + (pi[math_calculation]))
print("Your new email address is: " + str(first_letter) + str(ask2) + str(first_letter_month) + str(math_calculation) + str(month_len) + str(last_letter) + str(end))