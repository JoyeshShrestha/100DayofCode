from tkinter import *
from tkinter import messagebox
from pwGen import Password
import pyperclip
import json


def find_password():
    try:
        with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day29-Password_Gen_GUI\\data.json","r") as file_data:
            data = json.load(file_data)
            website=website_entry.get()
            if website in data:
                email = data[website]["email"]    
                pw = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {pw}") 

            else:
                messagebox.showinfo(title=website, message=f"NO data for {website}")
    except FileNotFoundError:
                messagebox.showinfo(title="Error", message=f"NO file found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_gen = Password()

def pass_gen():
     pw = password_gen.generate_password()
     password_entry.insert(0,pw)
     pyperclip.copy(pw)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_all():
    website_entry.delete(0,END)
    password_entry.delete(0,END)
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
         website:{
              "email":email,
              "password":password,
         }
    }
    if len(website)==0 or len(email)==0 or len(password)==0:
           messagebox.showinfo(title="Error", message="Empty boxes!")    
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"These are the details entered: \nEmail:{email}"
                       f"\nPassword:{password} \nIs it ok to save?" )
    


        if is_ok: 
            try:
                with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day29-Password_Gen_GUI\\data.json","r") as data_file:
                    data=json.load(data_file)
                    
                    data.update(new_data)
                    
                with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day29-Password_Gen_GUI\\data.json","w") as data_file:

                    json.dump(data,data_file, indent=4)
            except FileNotFoundError:
                with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day29-Password_Gen_GUI\\data.json","w") as data_file:
                    json.dump(new_data,data_file, indent=4)
                 
            clear_all()     



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50, bg="white")

# Canvas

canvas = Canvas(width=200,height=200, bg="white", highlightthickness = 0)
logo_img = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day29-Password_Gen_GUI\\logo.png")
canvas.create_image(100,112,image = logo_img)

canvas.grid(column=2,row=2)


website_label = Label(padx=5 , pady=5,text="Website:", bg="white")
website_label.grid(column=1,row=3)

website_entry = Entry(width=21)
website_entry.grid(column=2,row=3)
website_entry.focus()


search = Button(text="Search",font=("Arial",6),width=35-21,command=find_password)
search.grid(column=3,row=3)

email_label = Label(padx=5 , pady=5, text="Email/Username:", bg="white")
email_label.grid(column=1,row=4)



email_entry = Entry(width=35)
email_entry.grid(column=2,row=4,columnspan=2)
email_entry.insert(END,"sjoyesh2000@gmail.com")


password_label = Label(padx=5 , pady=5, text="Password:", bg="white")
password_label.grid(column=1,row=5)

password_entry = Entry(width=21,text="")
password_entry.grid(column=2,row=5)

generate_button = Button(padx=5 , pady=5,highlightthickness = 0,text="Generate Password",font=("Arial",6),width=35-21,command=pass_gen)
generate_button.grid(column=3,row=5)


add = Button(padx=10 , pady=5,highlightthickness = 0, text="Add",font=("Arial",7),width=36,command=save_password)
add.grid(column=2,row=6,columnspan=2)

window.mainloop()
