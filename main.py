import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

#TODO 1. Creating a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Creating a list of the phonetic code words from a word that the user inputs.

def generate_nato():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters A–Z.")
        generate_nato()
    else:
        print(output_list)

generate_nato()
