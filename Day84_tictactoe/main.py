from tkinter import *
import customtkinter
from tkinter import font as tkFont

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.geometry("400x300")

root.title("TIC TAC TOE - by Joyesh")

root.config(padx=100, pady=50)

# --------------------CONSTANTS-------------------------------------
helv36 = tkFont.Font(family='Helvetica', size=10, weight='normal')

buttons = []


# button_border = Frame(root, ) 


# ----------------------All Functions-------------------------------------
def checklogic(clicked_button):
    global buttons
    buttons.append(clicked_button)
    disable_one(buttons)
    if a1.cget('text')==a2.cget('text') and a2.cget('text') == a3.cget('text') and a1 in buttons and a2 in buttons and a3 in buttons:
        won.configure(text=f"{a1.cget('text')} won this match")
        disable_buttons()
    elif b1.cget('text')==b2.cget('text') and b2.cget('text') == b3.cget('text') and b1 in buttons and b2 in buttons and b3 in buttons:
        won.configure(text=f"{b2.cget('text')} won this match")
        disable_buttons()

    elif c1.cget('text')==c2.cget('text') and c2.cget('text') == c3.cget('text') and c1 in buttons and c2 in buttons and c3 in buttons:
        won.configure(text=f"{c3.cget('text')} won this match")
        disable_buttons()

    elif a2.cget('text')==b2.cget('text') and b2.cget('text') == c2.cget('text') and a2 in buttons and b2 in buttons and c2 in buttons:
        disable_buttons()

        won.configure(text=f"{a2.cget('text')} won this match")
    elif a3.cget('text')==b3.cget('text') and b3.cget('text') == c3.cget('text') and a3 in buttons and b3 in buttons and c3 in buttons:
        disable_buttons()

        won.configure(text=f"{a3.cget('text')} won this match")
    elif a1.cget('text')==b1.cget('text') and b1.cget('text') == c1.cget('text') and a1 in buttons and b1 in buttons and c1 in buttons:
        disable_buttons()

        won.configure(text=f"{a1.cget('text')} won this match")
    elif a1.cget('text')==b2.cget('text') and b2.cget('text') == c3.cget('text') and a1 in buttons and b2 in buttons and c3 in buttons:
        disable_buttons()

        won.configure(text=f"{a1.cget('text')} won this match")    
    elif c1.cget('text')==b2.cget('text') and b2.cget('text') == a3.cget('text') and c1 in buttons and b2 in buttons and a3 in buttons:
        disable_buttons()

        won.configure(text=f"{a3.cget('text')} won this match")  
    else:
        if len(buttons)==9:
            won.configure(text="It's a tie!")
            disable_buttons()






def change_current_value():
    
    if current_value:
        if current_value == 'O':
            turn.configure(text = 'O Turn')
            return 'X'
        elif current_value == 'X':
            turn.configure(text = 'X Turn')
            return 'O'
    else:
        turn.configure(text = 'O Turn')
        
        return "O"  
        
    # return current_value

def disable_one(buttons):
    for button in buttons:
        button.configure(
             bg = "black", fg = "white",state='disabled')
        


def disable_buttons():
    for button in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
        
        button.configure(
             bg = "#6CD300", fg = "white",state='disabled')


def button_clicked(clicked_button):

    # text = clicked_button.cget("text")
    # state = clicked_button.cget("state")
    global current_value
    global next_turn

    next_turn = change_current_value()
    
    current_value = next_turn
    clicked_button.configure(text = current_value, highlightcolor= "green")
    checklogic(clicked_button)


    

current_value = 'X'
    
# next_turn = change_current_value()


turn = customtkinter.CTkLabel(master=root,text=f"O Turn")
turn.grid(column=2,row=0)
a1 = Button(master=root,
                  text = "",background="white",width=10,height=5,command= lambda: button_clicked(a1)) 
a1.grid(column=1,row=1)

a2 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(a2)) 
a2.grid(column=2,row=1)

a3 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(a3)) 
a3.grid(column=3,row=1)
b1 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(b1)) 
b1.grid(column=1,row=2)

b2 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(b2)) 
b2.grid(column=2,row=2)

b3 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(b3)) 
b3.grid(column=3,row=2)


c1 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(c1)) 
c1.grid(column=1,row=3)
c2 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(c2)) 
c2.grid(column=2,row=3)
c3 = Button(master=root,
                  text = "",background="white",width=10,height=5, command= lambda: button_clicked(c3)) 
c3.grid(column=3,row=3)

# button = customtkinter.CTkButton(master=root,text="Hello World")

# button.place(relx=0.5, rely=0.5 , anchor =CENTER)
won = customtkinter.CTkLabel(master=root,text="")

won.grid(column=1,columnspan =2, row=4)
root.mainloop()