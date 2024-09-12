#Task1: Leap Year Checker 
    # Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

#===============================================================================

# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100
    # number must be divisible by 4 but not divisble by 400 (AND)
       
# but these centurial years are leap years if they are exactly divisible by 400.
    # if not both but divisble by 400 it is still a leap year (OR)


year = int(input("Enter a year: "))

if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(year,"is a leap year!")
else: 
    print(year,"is not a leap year..")

