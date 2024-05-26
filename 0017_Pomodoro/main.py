from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✓'
windowTimer = None

# ---------------------------- TIMER RESET ----------------------------- #
def resetButtonClicked():
    global windowTimer
    global rep
    
    rep = 0
    check_marks = ''
    window.after_cancel(windowTimer)
    label_check_marks.config(text=check_marks)
    label_title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='25:00')

# ---------------------------- TIMER MECHANISM ------------------------- #
def startButtonClicked():
    global rep
    global check_marks
    rep += 1

    work_time_Sec = WORK_MIN * 60
    short_break_time_sec = SHORT_BREAK_MIN * 60
    long_break_time_sec = LONG_BREAK_MIN * 60

    if rep >= 9:
        check_marks = ''
        label_check_marks.config(text=check_marks)

    if rep % 8 == 0:
        check_marks += CHECK_MARK
        label_check_marks.config(text=check_marks)
        label_title.config(text='Break', fg=RED)
        count_down(long_break_time_sec)
    elif rep % 2:
        label_title.config(text='Work', fg=GREEN)
        count_down(work_time_Sec)
    else:
        check_marks += CHECK_MARK
        label_check_marks.config(text=check_marks)
        label_title.config(text='Break', fg=PINK)
        count_down(short_break_time_sec)

# ---------------------------- COUNTDOWN MECHANISM --------------------- #
def count_down(time: int):
    global rep
    minutes = time // 60
    seconds = time % 60
    if seconds <= 9:
        seconds = f'0{seconds}'

    if time >= 0:
        global windowTimer
        canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
        windowTimer = window.after(1000, count_down, time - 1)
    else:
        startButtonClicked()

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(0, 0)
rep = 0

label_title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
label_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='25:00', fill='white', font=(FONT_NAME, 26, 'bold'))
canvas.grid(row=1, column=1)

button_start = Button(text='Start', command=startButtonClicked, highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = Button(text='Reset', command=resetButtonClicked, highlightthickness=0)
button_reset.grid(row=2, column=2)

check_marks = ''
label_check_marks = Label(text=check_marks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
label_check_marks.grid(row=3, column=1)

window.mainloop()
