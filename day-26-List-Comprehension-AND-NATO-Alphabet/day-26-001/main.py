# ========================= List comprehension syntax =========================
# new_list = [new_item for item in list]   ---> Similar to "map"

# numbers = [1, 2, 3]
# print(f"numbers: {numbers}")
#
# new_numbers = [n+1 for n in numbers]
# print(f"new_numbers: {new_numbers}")


# name = "Abhishek"
# print(f"name: {name}")
#
# name_chars = [letter for letter in name]
# print(f"List of letters/characters in name: {name_chars}")
#
# even_numbers = [num * 2 for num in range(1, 5)]
# print(even_numbers)




# ==================== Conditional List Comprehension ====================
# new_list = [new_item for item in list if condition/test]  --> Similar to "filter"

names = ['Alex', "Beth", 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) == 4]

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)




