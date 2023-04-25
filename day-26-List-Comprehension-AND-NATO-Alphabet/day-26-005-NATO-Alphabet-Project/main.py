import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# flag = True
#
# while flag:
#     word = input('Enter any word: ')
#     try:
#         phonetic_list = [phonetic_dict[letter.upper()] for letter in word]
#     except KeyError:
#         print("Only Alphabet letters are allowed, Please try again!")
#     else:
#         print(phonetic_list)
#         flag = False


def generate_phonetic():
    word = input('Enter any word: ')
    try:
        phonetic_list = [phonetic_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Only Alphabet letters are allowed, Please try again!")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
