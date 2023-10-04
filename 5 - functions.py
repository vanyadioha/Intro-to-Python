# Functions
import math


# def first_function():
#     print("Hello")


# first_function()


# Final Hurdle Challenge reeborgs world
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump_hurdle():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()


# while not at_goal():
#     if wall_in_front():
#         jump_hurdle()
#     else:
#         move()


# functions that allow inputs
def greet(name, location):
    print(f"Hello {name}, How's the weather in {location}?")


# greet("Enciso", "Brighton")
# greet(location="Brighton", name="Enciso")

# Paint area calculator
# h = float(input("Wall Height: "))
# w = float(input("Wall Width: "))


# def paint_area_calculator(height, width):
#     sm_per_can = 5
#     wall_area = height * width
#     cans_needed = math.ceil(wall_area / sm_per_can)
#     print(cans_needed)


# paint_area_calculator(h, w)

# Prime number checker
# number = int(input("Check this Number: "))


# def prime_checker(n):
#     isPrimeNumber = True
#     for i in range(2, n):
#         remainder = n % i
#         if remainder == 0:
#             isPrimeNumber = False
#     if isPrimeNumber:
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")


# prime_checker(number)


def format_name(f, l):
    if f == "" or l == "":
        return
    return f"My name is {f.title()} {l.title()}"


# print(format_name("", ""))


# Days in month
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(yyyy, mm):
    """Takes in a year and a month and returns how many days occur in said month"""
    leap_year = is_leap_year(yyyy)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        days[1] = 29
    return days[mm - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month (Digit): "))
days = days_in_month(year, month)
print(days)
