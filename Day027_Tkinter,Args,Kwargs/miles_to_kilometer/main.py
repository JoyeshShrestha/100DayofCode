import tkinter


def calculation():
    miles = input_Miles.get()
    km = 1.609 * int(miles)
    second_label .config(text=km)









window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300,height=200)
window.config(padx=30,pady=30)
window.config(background="white")


#input

input_Miles = tkinter.Entry(textvariable="0",width=15)
input_Miles.grid(column=2,row=0)

input_Miles.config(background="white")


#miles_label

miles_label = tkinter.Label(text="Miles",font=("Arial",10,'normal'))
miles_label.grid(column=3,row=0)
miles_label.config(padx=0,pady=10)
miles_label.config(background="white")


first_label = tkinter.Label(text="is equal to",font=("Arial",10,'normal'))
first_label.grid(column=1,row=1)
first_label.config(padx=0,pady=5)
first_label.config(background="white")






second_label = tkinter.Label(text="0",font=("Arial",10,'normal'))
second_label.grid(column=2,row=1)
second_label.config(padx=0,pady=5)
second_label.config(background="white")


km_label = tkinter.Label(text="km",font=("Arial",10,'normal'))
km_label.grid(column=3,row=1)
km_label.config(padx=0,pady=5)
km_label.config(background="white")



button2 = tkinter.Button(text="Calculate",command=calculation)
button2.grid(column=2,row=2)
















window.mainloop()

