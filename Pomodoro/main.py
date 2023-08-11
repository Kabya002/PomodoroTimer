from tkinter import *
from math import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "green"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.5
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    count_check.config(text="0")
    canvas.itemconfig(count_canvas, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0 and reps < 8:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        count_check.config(text=f"{int(reps / 2)}")

    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        count_check.config(text="4")

    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    if reps > 8:
        pop_up()


# ---------------------------POPUP WINDOW-------------------------------- #


def pop_up():
    is_yes = messagebox.askyesno(title="Completed", message="You've completed a pomodoro session."
                                                            "\n Do you want to start another session?")
    if is_yes:
        reset_timer()
        start_timer()
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    if 0 < count_sec < 10:
        canvas.itemconfig(count_canvas, text=count_sec)
    else:
        canvas.itemconfig(count_canvas, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP -------------------------------#

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=150, pady=75, bg=YELLOW)
window.iconbitmap("3586375-clock-hour-timer-watch_107942.ico")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
count_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=("Arial", 40, "bold"), fg=GREEN)
timer_label.grid(column=1, row=0)
timer_label.config(bg=YELLOW)

start_button = Button(text="Start", bg="white", highlightthickness=0, fg=GREEN, command=start_timer, font=("Arial", 10,
                                                                                                           "bold"))
start_button.grid(column=0, row=4)

reset_button = Button(text="Reset", bg="white", highlightthickness=0, fg=GREEN, font=("Arial", 10, "bold"),
                      command=reset_timer)
reset_button.grid(column=2, row=4)

count_check = Label(width=10, height=5, bg=YELLOW, highlightthickness=0, font=("Arial", 20, "bold"), text="0", fg=GREEN)
count_check.grid(column=1, row=4)
window.mainloop()
