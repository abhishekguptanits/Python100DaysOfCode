import pandas

student_dict = {
    "student": ['Aryan', 'James', 'Saurabh'],
    'score': [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Loop through a data frame: Method 1
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)
#     print(f"{key}: {value.tolist()}")

# Loop through a data frame: Method 2 -> Using inbuilt method in pandas library
    # Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    print(f"{row.student}: {row.score}")

