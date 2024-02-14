from lists import word_list
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import customtkinter
from tkinter import font as tkFont
import random
import time

all_time = []
count = 0
typed_word = []
typing = ""
mistakes = []
characters = 0

def display_word():
    global words_to_display
    words_to_display=[]
    for _ in range(10):
        if _ == 5:
            words_to_display.append("\n")
        words_to_display.append(random.choice([word for word in word_list]))
    
    words_text = ' '.join(words_to_display)

    # Update the label text
    words.config(text=words_text)

def check_time():
    current_time = time.time()
    try:
        end_time = inital_time + 30
        if current_time >= end_time:
            show_score()
        else:
            root.after(1000, check_time)
    except:
        # print("No initail")
        
        root.after(1000, check_time)

def calculate_time(time):
    all_time.append(time - inital_time)

    # print(f"times: {all_time}")

def correct_word(input_text):
    global mistakes
    if words_to_display[count-1] == "\n":
        if input_text != words_to_display[count]:
            mistakes.append(input_text)
    else:
        if input_text != words_to_display[count-1]:
            mistakes.append(input_text)    


def show_score():
    # wpm = sum(all_time)/len(all_time)
    wpm = (characters/5)/0.5
    accuracy = (len(mistakes)/len(typed_word))*100

    mistakes_label = Label(root, text=f'Accuracy : {accuracy}%   WPM: {wpm}', font=helv6,bg="#252525",fg="white")
    mistakes_label.pack(pady=5)
    # wpm_label = Label(root, text=f'WPM: {wpm}', font=helv6,bg="#252525",fg="white")
    # wpm_label.pack() 
    user_input.configure(state='disabled')
    # print("ok enough done finished kaam!")





def check_word(event):
    global typed_word
    global typing
    global count   
    global inital_time
    # global end_time
    global characters
    characters+=1
    if count == 0:
        
        inital_time = time.time()
        
        count+=1

    # cursor_label.configure(text= user_input.get+ "|")
    
    if event.keysym == 'space' :
        

        if count == 10:
            count=1
            display_word()
        
        time_after_space = time.time()
        calculate_time(time_after_space)

        typed_word.append(user_input.get()) 
        # print(words_to_display)
        typing = typing + " " +  typed_word[-1]
        cursor_label.configure(text= typing)
        input_text = user_input.get()

        correct_word(input_text)
        count+=1

        # print("Space bar pressed! Input:", input_text)
        user_input.delete(0, tk.END)  # Clear the entry after getting the input

        # Move the cursor label to the end of the text
    # cursor_label.place(x=user_input.winfo_width(), y=0)

    # update_cursor_position()

def update_cursor_position():
    # Move the cursor label based on the current position in the entry
    cursor_label.place(x=user_input.winfo_x() + user_input.index(tk.INSERT) * 8, y=500)
    user_input.after(100, update_cursor_position)



customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
helv36 = tkFont.Font(family='Helvetica', size=30, weight='bold')
helv69 = tkFont.Font(family='Helvetica', size=10, weight='normal')
helv6 = tkFont.Font(family='Helvetica', size=20, weight='bold')



root.geometry("900x600")

root.title("TypeSpeed Testing - by Joyesh")

root.config(padx=100, pady=50)






# start= Button(master=root, text="Start Game",width=10,height=5,command=display_word)

# start.pack()


words = Label(root, text = ' ', font=helv36,height=10,width=50)

words.pack()
display_word()

user_input = customtkinter.CTkEntry(master=root,
                               placeholder_text="Start Typing ...",
                               width=300,
                               height=35,
                               border_width=2,
                               corner_radius=5,
                               
                               )

user_input.bind("<Key>", check_word)

user_input.pack(pady= 30)

cursor_label = Label(root, text=typed_word, font=helv69,bg="#252525",fg="white")
cursor_label.pack() 

# if time.time() == end_time:
#     show_score()
root.after(1000, check_time)

root.mainloop()