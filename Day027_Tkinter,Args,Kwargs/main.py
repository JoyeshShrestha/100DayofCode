import tkinter

def button_clicked():
    # print("I got clicked")
    new_text = input.get()
    my_label.config(text= new_text)





window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=30,pady=30)

#Label

my_label = tkinter.Label(text="I am Label",font=("Arial",24,'bold'))
my_label.grid(column=0,row=0)







# Entry

input = tkinter.Entry()
input.grid(column=4,row=4)

button = tkinter.Button(text="Click Me", command=button_clicked)

button.grid(column=3,row=0)
button2 = tkinter.Button(text="Whatss app?")
button2.grid(column=1,row=2)



window.mainloop()