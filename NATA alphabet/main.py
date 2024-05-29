#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter : row.code for (index, row) in nato_data_frame.iterrows()}

word = input()
word = word.upper()
list = []

for x in word:
    list.append(data_dict[x])

print(list)