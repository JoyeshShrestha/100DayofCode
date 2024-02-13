from lists import word_list
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import customtkinter
from tkinter import font as tkFont
import random
typed_word = []
typing = ""
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


def check_word(event):
    global typed_word
    global typing

    # cursor_label.configure(text= user_input.get+ "|")
    
    if event.keysym == 'space':
        typed_word.append(user_input.get()) 
        print(words_to_display)
        typing = typing + " " +  typed_word[-1]
        cursor_label.configure(text= typing)
        input_text = user_input.get()
        print("Space bar pressed! Input:", input_text)
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
helv69 = tkFont.Font(family='Helvetica', size=20, weight='normal')


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


root.mainloop()