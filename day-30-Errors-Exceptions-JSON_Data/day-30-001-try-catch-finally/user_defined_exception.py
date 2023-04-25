
# try:
#     file = open("a_file.txt")
#     temp_dict = {"key": "value"}
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Lorem ipsum")
# except KeyError as error_msg:
#     print(f"Key {error_msg} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # raise KeyError
#     raise TypeError("This is an error thrown by user's choice")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height can't be over 3 meters, Please review your input!")

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi}")

