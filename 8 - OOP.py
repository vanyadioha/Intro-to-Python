import random


class User:
    """Users for a hypothetical App"""

    def __init__(self, name, user_name, age, gender):
        self.name = name
        self.user_name = user_name
        self.age = age
        self.gender = gender
        self.cgpa = 0

    def give_nice_gp(self):
        nice_gp = round(random.random() + 4.0, 2)
        self.cgpa = nice_gp


user_1 = User("Victor Anyadioha", "thegr8khallie", 22, "Male")
user_1.name = "Fetty Wap"
user_1.give_nice_gp()
print(f"My name is {user_1.name} and I have a CGPA of {float(user_1.cgpa)}/5.0")
