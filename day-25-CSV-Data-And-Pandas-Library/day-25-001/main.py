# # Method 1: Using file read method
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# ===========================================================================================

# # Method 2: Using python "csv" library
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data, None)        # skips the header of the csv file
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

# ===========================================================================================

# Method 3: Using Pandas Library
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(type(temp_list))
# avg_temp = sum(temp_list) / len(temp_list)
# print(f"Average Temperature: {avg_temp}")

# avg_temp = data["temp"].mean()
# print(f"Average Temperature: {avg_temp}")
#
# max_temp = data["temp"].max()
# print(f"Max Temperature: {max_temp}")


# # Get Data in Columns
# print(data["temp"])
# print(data.temp)



# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == 15])
# print(data[data.temp == 14])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.day)
# print(monday.temp)
# print(monday.condition)
#
# monday_temp_C = int(monday.temp)
# monday_temp_F = monday_temp_C * 9/5 + 32
# print(f"Temperature Celsius: {monday_temp_C}\nTemperature Fahrenheit: {monday_temp_F}")






# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_dataframe = pandas.DataFrame(data_dict)
# print(new_dataframe)
new_dataframe.to_csv("new_data.csv")          # creates a csv file from an existing dataframe




