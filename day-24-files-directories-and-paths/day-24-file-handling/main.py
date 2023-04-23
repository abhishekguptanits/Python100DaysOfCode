# # READING A FILE
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# # WRITING TO A FILE -> Overwrites the previous contents
# with open("my_file.txt", mode="w") as file:
#     file.write("New text...")


# # TO MODIFY(append the new content) THE CONTENT OF THE FILE
# with open("my_file.txt", mode="a") as file:
#     # file.write("\ntext to be appended in a new line!")
#     file.write("text to be appended in the same line")


# IN WRITE MODE, IF A FILE DOESN'T EXIST, THEN IT CREATES A NEW FILE
with open("new_file.txt", mode="w") as file:
    file.write("New file is created and the content is added...")



