

import pandas

data= pandas.read_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day026-List Comprehension\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")

# for(index,row) in data.iterrows():
code_dict = {row.letter:row.code for(index,row) in data.iterrows()}

# print(code_dict)

def here():
    user_input = input().upper()

    user_word_list=[letter for letter in user_input]

    try:
        user_code_list = [code_dict[letter] for letter in user_word_list]
    except KeyError:
        print("Sorry only letters from alphabet please")
        here()
    else:    
        print(user_code_list)

    
here()




#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

