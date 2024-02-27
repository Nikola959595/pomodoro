from tkinter import *
from tkinter import simpledialog
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = simpledialog.askinteger(title="Work time!👩‍💻", prompt="How many minutes do you want to work for?")
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text="Timer")
    start_button.config(state="normal")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN  * 60
    start_button.config(state="disabled")
    REPS += 1
    if REPS == 8:
        count_down(long_break_sec)
        REPS = 0
        title_label.config(text="Long Break",font=(FONT_NAME, 50, "bold",), fg=RED, bg= YELLOW, highlightthickness=0) 
    elif REPS % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work",font=(FONT_NAME, 50, "bold",), fg=GREEN, bg= YELLOW, highlightthickness=0)
    elif REPS % 2 == 0:
        count_down(short_break_sec)  
        title_label.config(text="Break",font=(FONT_NAME, 50, "bold",), fg=PINK, bg= YELLOW, highlightthickness=0)     

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmark.configure(text=mark)        


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)
window.update_idletasks()

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2,column=2)
title_label = Label(text="Timer",font=(FONT_NAME, 50, "bold",), fg=GREEN, bg= YELLOW, highlightthickness=0)
title_label.grid(row=1, column=2)

start_button = Button(text="Start", highlightthickness=0, command= start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(row=3, column=3)

checkmark = Label(font=(FONT_NAME, 30), fg=GREEN, bg= YELLOW, highlightthickness= 0)
checkmark.grid(row=4, column=2)

if WORK_MIN == None:
    window.destroy()

window.mainloop()