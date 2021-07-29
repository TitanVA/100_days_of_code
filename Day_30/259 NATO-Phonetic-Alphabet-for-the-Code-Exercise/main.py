# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# Create a list of the phonetic code words from a word that the user inputs.

def generic_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except NameError:
        generic_phonetic()
    except KeyError:
        generic_phonetic()
    else:
        print(output_list)


generic_phonetic()
