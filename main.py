import math
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    timers = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN]
    work_break_label.config(text="Work")

    for timer in timers:
        update_work_break(timer)
        count = timer * 60
        count_down(count)


def update_work_break(duration):
    new_text = ""
    if duration == WORK_MIN:
        new_text = "Working"
    elif duration == SHORT_BREAK_MIN | duration == LONG_BREAK_MIN:
        new_text = "On Break"

    work_break_label.config(text=new_text)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_minute = math.floor(count/60)
    count_seconds = count % 60

    if count_minute < 10:
        count_minute = f"0{count_minute}"
    if count_minute == 0:
        count_minute = "00"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_seconds == 0:
        count_seconds = "00"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    if count > 0:
        window.after(1000, count_down, count-1)
    if count == 0:
        canvas.itemconfig(timer_text, text="Time's Up")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
heading_label.grid(column=1, row= 0)

work_break_label = Label(text="", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
work_break_label.grid(column=1, row=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

start_btn = Button(text="Start", command=start_timer, bg="white", highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", command= reset_timer, bg="white", highlightthickness=0)
reset_btn.grid(column=2, row=3)

check_marks = Label(text="✔", bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)
window.mainloop()
