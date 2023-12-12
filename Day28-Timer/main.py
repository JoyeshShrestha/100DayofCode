from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
whole_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(whole_timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    check.config(text= "")  
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = 1*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps% 8 == 0:
        timer.config(text="Longer Break",fg=RED)

        count_down(long_break_sec)

    elif reps%2 == 0:
        timer.config( text="Breaks",fg=PINK)

        count_down(short_break_sec)
    else:
        timer.config( text="Work",fg=GREEN)

        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60 

    if count_min == 0:
        count_min = "00"


    if int(count_min) < 10 and int(count_min)>0:
        count_min=f"0{count_min}"          
    if count_sec == 0:
        count_sec = "00"

    if int(count_sec) < 10 and int(count_sec)>0:
        count_sec=f"0{count_sec}"    
        
     
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count>0:
        global whole_timer
        whole_timer = window.after(1000, count_down,count-1)
    else:
        start_timer()  
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        # if reps % 3 == 0:
        check.config(text= marks)  

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50, bg=YELLOW)

# Canvas

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day28-Timer\\tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text = "00:00",fill="white",font=(FONT_NAME,25,"bold"))


canvas.grid(column=2,row=2)

timer = Label(text="Timer",fg= GREEN, font= (FONT_NAME,50),bg=YELLOW)
# timer.create_text(100,130,text = "Timer",fill=GREEN,font=(FONT_NAME,35,"bold"))
timer.grid(column=2,row=1)

start = Button(text="Start",highlightthickness = 0,command=start_timer)

start.grid(column=1,row=3)



reset = Button(text="Reset",highlightthickness = 0,command=reset_timer)
reset.grid(column=3,row=3)


check = Label(fg= GREEN,bg=YELLOW)
check.grid(column=2,row=4)

window.mainloop()
