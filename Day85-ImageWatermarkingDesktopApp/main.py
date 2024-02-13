from tkinter import *
from tkinter import filedialog
import customtkinter
from tkinter import font as tkFont
from PIL import Image, ImageTk, ImageDraw, ImageFont



def open_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[(".\\Day85-ImageWatermarkingDesktopApp\\1", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
    if file_path:
        image = Image.open(file_path)
        # photo = ImageTk.PhotoImage(image)
        aspect_ratio = image.width / image.height

        # Calculate the new dimensions while maintaining the aspect ratio
        new_width = 300
        new_height = int(new_width / aspect_ratio)
        image = image.resize((new_width, new_height))

        # Display the image
        display_image(image)

def display_image(image):
    photo = ImageTk.PhotoImage(image)
    for widget in root.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()
        if isinstance(widget, Entry):
            widget.destroy()
        if isinstance(widget, Button):
            widget.destroy()    
       
    # Display the image
    label = Label(root, image=photo)
    label.image = photo
    label.pack()

    # Entry widget for user input
    text_entry = Entry(root, width=30)
    text_entry.pack(pady=10)
    
    # Font for the text
    font = ImageFont.truetype(r"C:\Users\lenovo\AppData\Local\Microsoft\Windows\Fonts\MATURASC.TTF", 20)  # Change the font file path and size as needed
    # fontpath="C:\\Users\\lenovo\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Simply*Glamorous.ttf"
    # font = ImageFont.truetype(fontpath, 20)
    def overlay_text():
        
        user_text = text_entry.get()

        # Create a copy of the original image
        image_with_text = image.copy()

        # Create a drawing object
        draw = ImageDraw.Draw(image_with_text)

        # Get the size of the text to center it on the image
        text_size = draw.textsize(user_text, font)
        text_position = ((image.width - text_size[0]) // 2, image.height - text_size[1])

        # Draw the text on the image
        draw.text(text_position, user_text, font=font, fill="white")

        # Update the displayed image
        photo_with_text = ImageTk.PhotoImage(image_with_text)
        label.configure(image=photo_with_text)
        label.image = photo_with_text
        display_image(image_with_text)

    def save_image():
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            image.save(save_path)    
    # Button to overlay text on the image
    overlay_button = Button(root, text="Overlay Text", command=overlay_text)
    overlay_button.pack()


    save = Button(root,text="Save",command=save_image)
    save.pack()




customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.geometry("1000x1000")

root.title("ImageWaterMarking - by Joyesh")

root.config(padx=100, pady=50)




button = Button(root, text="Open Image", command=open_image)
button.pack(pady=10)
# button.grid(column=1,row=1)
# img = PhotoImage(file =".\\Day85-ImageWatermarkingDesktopApp\\1.jpg")

# img.image = img   


# entry = Entry(root, width=30)
# entry.pack(pady=10)

# # Button to get user input
# button = Button(root, text="Get Input", command=get_user_input)
# button.pack()
   
root.mainloop()