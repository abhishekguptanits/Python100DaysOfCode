# Dictionary Comprehension
# Method 1: new_dict = {new_key:new_value for item in list}
# Method 2: new_dict = {new_key:new_value for (key, value) in dict.items()}
# Method 3: new_dict = {new_key:new_value for (key, value) in dict.items() if condition/test}

import random

# Example 1:
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {name:random.randint(10, 100) for name in names}
print(student_scores)
print(type(student_scores))

passed_students = {key:student_scores[key] for key in student_scores if student_scores[key] >= 60}
print(f"Passed Student: {passed_students}")

failed_students = {name:score for (name, score) in student_scores.items() if score < 60}
print(f"Failed Students: {failed_students}")



# for item in student_scores.items():
#     print(item)


