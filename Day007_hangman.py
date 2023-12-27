import random
h1 = """
   _______
     |/      |
     |      (_)
     |      
     |      
     |     
     |
    _|___
"""
h2 = """
   _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
"""
h3 = """
   _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
"""
h4 = """
   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
"""
h5 = """
   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ 
     |
    _|___
"""
h6  = """
   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ \_
     |
    _|___
"""

print("WELCOME TO HANGMAN -made by Joyesh")
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/        
""")
hangman= [h1,h2,h3,h4,h5,h6]
words = [
    'Tree', 'Apple', 'River', 'Bridge', 'Sun', 'Cat', 'Book', 'Key', 'Hat', 'Cloud',
    'Chair', 'Smile', 'Door', 'Fish', 'Road', 'Moon', 'Star', 'Cup', 'Shoe', 'Song',
    'Ball', 'Clock', 'Park', 'Car', 'Flower', 'Friend', 'House', 'Bird', 'Ocean', 'Watch'
]

pick = random.randint(0,len(words)-1)


selected_word = words[pick].lower()


length_word = len(selected_word)
dash=[]
word_list = []
all_dash =""
for i in range(0,length_word):
    all_dash += "_"
    dash .append("_")
    word_list.append(selected_word[i])



# print(word_list)
print(all_dash)
count = 0
wrong_count = 0
toshow_dash =all_dash
already_list =[]
while count ==0:

    user_input = input("Enter a letter: ").lower()
    
    word_exists = False
    if user_input in already_list:
                 print(f"You have entered {user_input} already")
                 continue
    else:
                 already_list.append(user_input)
    print(f"all the entered letters were {already_list}")

    for i in range(0,length_word):

        if user_input==selected_word[i]:
            
            if toshow_dash == all_dash:
                toshow_dash =""
            dash[i] = user_input
            word_exists=True
    if toshow_dash != all_dash:
        for every in dash:
                toshow_dash+= every        
        # print(dash)
            
        


    if word_exists is False:        
        wrong_count+=1
        # print("wrongs: ", wrong_count)
        print(hangman[wrong_count-1])
        # print(toshow_dash)

    print(toshow_dash)

    toshow_dash =""
    if dash == word_list:
        print("Congrats you win")
        break
    if wrong_count==6:
        print("You lose")
        print(f"Your word was {selected_word}")

        break
    
        


