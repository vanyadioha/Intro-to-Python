import random

# Random Integer
# random_int = random.randint(1, 10)
# print(random_int)
# # Random float
# random_float = random.random()
# print(random_float)
# # Random float 0 - 5
# random_float1 = random.random() * 5

# Coin toss program challenge
# toss = random.randint(0, 1)
# if toss == 0:
#     print("Coin toss says Heads")
# else:
#     print("Coin toss says tails")

# Python Lists
# fruits = ["Orange", "Apple", "Grapes", "Pineapple", "Watermelon", "Pear", "Apple"]
# # Arranged in the order of which they joined the union
us_states = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachussets",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New york",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Missisippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

# print(len(us_states))

# Banker Roulette
# string_of_Friends = input(
#     "Enter the names of everyone at the table only seperated by whitespace (ie Name1 Name2 Name3)\n"
# )
# list_of_friends = string_of_Friends.split()
# payers_index = random.randint(0, len(list_of_friends) - 1)
# print(f"The Entire bill will be handled by Idan {list_of_friends[payers_index]}")

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
position = input("Where do you want to place the treasure? ")
column = int(position[0])
row = int(position[1])

chosen_list = map[row - 1]
chosen_list[column - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")
