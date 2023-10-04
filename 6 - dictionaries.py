data = {
    "bug": "Code misbehaviour",
    "function": "reusable code",
    "loop": "Rerunning code",
}
data["string"] = "Data bordered by quotation marks"

# for key in data:
#     print(f"{key}: {data[key]}")

# Grading program
student_scores = {"Harry": 81, "Ron": 78, "Hermoine": 99, "Draco": 74, "Neville": 62}

student_grades = {}


def grader(score):
    grade = ""
    if score >= 91:
        grade += "Outstanding"
    elif score >= 81:
        grade += "Exceeds Expectations"
    elif score >= 71:
        grade += "Acceptable"
    else:
        grade += "Fail"

    return grade


# for student in student_scores:
#     grade = grader(student_scores[student])
#     student_grades[student] = grade
# print(student_grades)

travel_log = [
    {
        "country": "france",
        "cities_visited": ["Paris", "Lyon", "Marseille", "Guingamp", "Lorient"],
        "food_eaten": ["Hors d'oeuvres", "Macaron"],
    },
    {
        "country": "germany",
        "cities_visited": ["Berlin", "Munich", "Cologne", "Leipzig", "Freiburg"],
        "food_eaten": ["Schnitzel", "Hamburger"],
    },
]


def add_new_country(country, cities, food):
    new_country = {"country": country, "cities_visited": cities, "food_eaten": food}
    travel_log.append(new_country)


add_new_country(
    "United Kingdom",
    ["London", "Manchester", "Brighton", "Tyne", "The Hamptons", "Leeds"],
    ["Shepherd's pie", "English breakfast", "Scran"],
)

# print(travel_log)
import os


# Custom terminal clearing function to help UX
def clear():
    os.system("cls" if os.name == "nt" else "clear")


bidders = {}
still_bidding = True

# while still_bidding:
#     name = input("What is your name: ")
#     bid = float(input("How much is your bid: $"))
#     bidders[name] = bid
#     other_bidder = input("Is there any other bidder? yes or no: ")
#     if other_bidder.lower() == "no":
#         still_bidding = False
#         winning_bid = 0
#         winner = ""
#         for bidder in bidders:
#             if bidders[bidder] > winning_bid:
#                 winning_bid = bidders[bidder]
#                 winner = bidder
#         print(f"{winner} is the winner for bidding ${winning_bid}")
#     elif other_bidder.lower() == "yes":
#         clear()
