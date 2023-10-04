# height = input('How tall are you (in cm)? ')
# height_int = float(height)
# if height_int > 120:
#     print("Can Ride!")
# else:
#     print("Can't Ride!")

# Challenge - Odd or even number checker
# number = int(input("Pick any number that comes to mind: "))
# if number % 2 == 1:
#     print("This is an odd number")
# else:
#     print("This is an even number")

# incorporating nested ifs and elifs
# Rollercoaster tickets
# height = float(input("How tall are you (in m)? "))
# bill = 0
# photo = 0
# midlife_crisis = False
# if height >= 1.2:
#     print("Congrats, you can ride")
#     age = int(input("How old are you? "))
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         if age >= 45 and age <= 55:
#             is_crisis = input("Are you going through a midlife crisis? Y or N: ")
#             if is_crisis == "Y":
#                 bill = 0
#                 midlife_crisis = True
#             else:
#                 bill = 12
#         else:
#             bill = 12
#     wants_photo = input("Do you want a photo? Y for yes or N for No: ")
#     if wants_photo == "Y" and midlife_crisis == False:
#         photo = 3
#         print(
#             f"TOTAL BILL\nBase Fee: ${bill}\nPhoto: ${photo}\nTotal Fee: ${bill + photo}"
#         )
#     else:
#         print(
#             f"TOTAL BILL\nBase Fee: ${bill}\nPhoto: ${photo}\nTotal Fee: ${bill + photo}"
#         )
# else:
#     print("Sorry, you cannot ride")

# Challenge. Building upon BMI app from last page
# weight = input("What is your weight in kilograms? ")
# height = input("What is your height in metres? ")
# bmi = round(float(weight) / (float(height) ** 2), 2)


# def message(interpretation):
#     return f"Your BMI is {bmi} hence you are {interpretation}"


# if bmi < 18.5:
#     print(message("Underweight"))
# elif bmi < 25:
#     print(message("Normal weight"))
# elif bmi < 30:
#     print(message("Overweight"))
# elif bmi < 35:
#     print(message("Obese"))
# else:
#     print(message("Morbidly Obese"))

# Challenge - Leap year checker
# year = int(input("The year on my mind is... "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("It is a leap year")
#         else:
#             print("It is not a leap year")
#     else:
#         print("It is a leap year")
# else:
#     print("It is not a leap year")

# Papa John's Pizza
# print("Welcome to Papa Johns!")
# size = input("What size of Pizza do you want? S, M or L: ")
# pepperoni = input("Do you want some pepperoni on that? Y or N: ")
# olives = input("Olives nko? Y or N: ")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if olives == "Y":
#     bill += 1

# print(f"Your total bill is ${bill}")

# Challenge - Love calculator
your_name = input("What is your name?\n")
their_name = input("What is their name?\n")
our_name = your_name + their_name
our_name_lower = our_name.lower()

# Our Name Match
our_t = our_name_lower.count("t")
our_r = our_name_lower.count("r")
our_u = our_name_lower.count("u")
our_e = our_name_lower.count("e")
our_l = our_name_lower.count("l")
our_o = our_name_lower.count("o")
our_v = our_name_lower.count("v")

# TRUE LOVE
true = str(our_t + our_r + our_u + our_e)
love = str(our_l + our_o + our_v + our_e)
true_love = int(true + love)

# Message
if true_love < 10 or true_love > 90:
    print(f"Your love score is {true_love}, You go together like coke and menthos")
elif true_love > 40 and true_love < 50:
    print(f"Your love score is {true_love}, You blend like gin and juice")
else:
    print(
        f"Your Love score is {true_love}, Can't say. Guess You'd have to fuck around and find out"
    )
