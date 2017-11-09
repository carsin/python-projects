from datetime import *

def get_choice(day, month, year):
    print("1)   Calculate the number of days in the given month.\n2)   Calculate the number of days left in the given year.")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        number_of_days(month, year)
    elif (choice == 2):
        days_left(day, month, year)
    else:
        print("Invalid choice!")
        get_choice(day, month, year)

def leap_year(year):
    if (year % 4 == 0):
        return True
    else:
        return False
    
def number_of_days(month, year):
    if (month == 2):
        if (leap_year(year)):
            print(str(monthDays[month - 1] + 1))
        
    print(str(monthDays[month - 1]))

def days_left(day, month, year):
    print((date(year, 12, 31) - date(year, month, day)).days)
    
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
get_choice(day, month, year)
