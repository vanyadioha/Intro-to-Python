# Global scope
enemies = 1


def increase_enemies():
    # Local Scope
    enemies = 2
    # print(f"number of {enemies}")


increase_enemies()
# print(f"number of {enemies}")

# There is no block scope in python
if 3 < 2:
    greeting = "Hello"
    # print(greeting)

# print(greeting)

# Modifying global variables

no_of_students = 50

# Global Constant
GRAVITY = 9.81


def update_no_of_students():
    global no_of_students
    no_of_students += 1
    print(f"No of Students: {no_of_students}")


update_no_of_students()
