from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
CORRECT_LIST=[]
import pandas
import random
import time

# ----------------read file-----------------------------------------

try:
    data = pandas.read_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\data\\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\data\\words_to_learn.csv",index=False)
    next_card()

def next_card():
    global current_card, whole_timer
    window.after_cancel(whole_timer)
    
    current_card = random.choice(to_learn)
    
    if current_card in CORRECT_LIST:
        next_card(False)
    canva.itemconfig(current_image,image=front_img)
    
    canva.itemconfig(language, text="French",fill="black")
    canva.itemconfig(word, text=current_card["French"],fill="black")
    
    whole_timer = window.after(3000, flip_card)


    


# -----------------flip card-----------------------------------

def flip_card():
   
        # CORRECT_LIST.append(current_card)
    canva.itemconfig(current_image,image=back_img)
    canva.itemconfig(language,fill="white",text="English")
    canva.itemconfig(word,fill="white",text=current_card["English"])
    
 




# -----------------main-------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50 , pady=50, bg=BACKGROUND_COLOR)
whole_timer = window.after(3000, flip_card)


canva = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness = 0)
front_img = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\images\\card_front.png")
back_img = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\images\\card_back.png")

current_image=canva.create_image(400,260,image=front_img)
language = canva.create_text(400,150,text = "French",fill="black",font=("Arial",40,"italic"))
word = canva.create_text(400,263,text = "hola",fill="black",font=("Arial",60,"bold"))

canva.grid(column=2,row=2,columnspan=2)

# buttons
right_image = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\images\\right.png")
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(column=3,row=3)


wrong_image = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day031-Flashcards_capstone\\images\\wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=2,row=3)


next_card()

window.mainloop()