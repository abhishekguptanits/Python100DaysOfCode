# Creating a class in Python

class Random:
    pass


class User:
    def __init__(self):
        print("New user is created")

user_1 = User()


user_2 = User()


# Method 1 to add Attributes to the Object
user_1.id = "001"
user_1.username = "aryan"


# print(user_1)
print(user_1.id)
print(user_1.username)

