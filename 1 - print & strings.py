# Print and Input manipulation
# name = input("What is your name?\n")
# age = input("How old are you?\n")
# job = input("What is your profession?\n")
# print("My name is " + name + " and I am a " + age + " year old " + job + ".")

# Data types
# Strings
greeting = "Hello"
h = greeting[len(greeting) - 1]
# Integers
my_age = 16
her_age = 32
sum_age = my_age + her_age
# Floats
my_score = 95.6
# Boolean
is_old = True
is_young = False

# Type Converters
# str()
# name = input("What is your Name?\n")
# name_length = len(name)
# length_str = str(name_length)
# text = "Your name has " + length_str + " Characters"
# int()
maths = "99"
english = 83
science = 96.3
arts = 91.7
score_avg = (int(maths) + english + science + arts) / 4
# print(type(maths), type(int(maths)), score_avg)

# Challenge
# num = input("Two-digit number?\n")
# char1 = num[0]
# char2 = num[1]
# sum = int(char1) + int(char2)

# operators
square = 6**6

# Challenge
# weight = input("What is your weight in kilograms? ")
# height = input("What is your height in metres? ")
# bmi = float(weight) / (float(height) ** 2)
score = 7
score //= 4

# F-strings
score = 3
isWinning = True
news = f"Your score is {score}, Hence, it is {isWinning} that you are winning"
# print(news)

# Your Life in weeks
# age = input("How old are you? ")
# intAge = int(age)
# maxAge = 90
# lifeInDays = intAge * 365
# lifeInWeeks = intAge * 52
# lifeInMonths = intAge * 12

# maxlifeInDays = maxAge * 365
# maxlifeInWeeks = maxAge * 52
# maxlifeInMonths = maxAge * 12

# lifeLeftDays = maxlifeInDays - lifeInDays
# lifeLeftWeeks = maxlifeInWeeks - lifeInWeeks
# lifeLeftMonths = maxlifeInMonths - lifeInMonths

# Challenge
# Tip Calculator
print("Welcome to the Tip calculator")
total_bill = input("What is the total Bill? $")
int_bill = float(total_bill)
tip_percent = input("What percentage tip would you like to give? ")
int_tip = float(tip_percent)
people = input("How many people to split the bill? ")
int_people = int(people)
total_tip = round((int_tip / 100) * int_bill, 2)
indie_bill = round((int_bill / int_people), 2)
indie_tip = round((total_tip / int_people), 2)
indie_total_fee = indie_bill + indie_tip

print(f"Bill: ${indie_bill}\nTip: ${indie_tip}\nTotal: ${indie_total_fee}")
