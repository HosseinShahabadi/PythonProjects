import pandas as pd

nato_data_frame = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {value.letter:value.code for (index, value) in nato_data_frame.iterrows()}

user_input = input('Enter your word: ').upper()
for letter in user_input:
    if letter in nato_dict:
        print(nato_dict[letter])
    else:
        print(letter)
