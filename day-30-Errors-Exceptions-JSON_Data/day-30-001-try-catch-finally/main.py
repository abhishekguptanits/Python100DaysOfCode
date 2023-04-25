# FileNotFound, KeyError, IndexError, TypeError

try:
    file = open("a_file.txt")
    temp_dict = {"key": "value"}
    # print(temp_dict["wrong-key"])
except FileNotFoundError:
    # print("There was an error while accessing the file")
    file = open("a_file.txt", "w")
    file.write("Lorem ipsum")
except KeyError as error_msg:
    print(f"Key {error_msg} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file closed successfully")
