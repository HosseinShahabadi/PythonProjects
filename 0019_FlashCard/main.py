from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except:
    data = pd.read_csv('./data/french_words.csv')

data = data.to_dict(orient='records')
to_learn = []
selected_data = None
flip_timer = None


def drawCard():
    global selected_data, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    selected_data = random.choice(data)

    canvas.itemconfig(canvas_img, image=img_card_front)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=selected_data['French'], fill='black')

    flip_timer = window.after(3000, flip_card)


def btn_wrong_clicked():
    drawCard()


def btn_right_clicked():
    global selected_data
    data.remove(selected_data)
    save = pd.DataFrame(data)
    save.to_csv('./data/words_to_learn.csv', index=False)
    drawCard()


def flip_card():
    global selected_data
    canvas.itemconfig(canvas_img, image=img_card_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=selected_data['English'], fill='white')

# --------------------------------- UI --------------------------------- #
window = Tk()
window.minsize(width=600, height=400)
window.resizable(0, 0)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")

img_card_back = PhotoImage(file='./images/card_back.png')
img_card_front = PhotoImage(file='./images/card_front.png')
img_right = PhotoImage(file='./images/right.png')
img_wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=img_card_front)
title = canvas.create_text(400, 133, text='', font=(FONT_NAME, 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=(FONT_NAME, 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

btn_wrong = Button(image=img_wrong, highlightthickness=0, command=btn_wrong_clicked)
btn_wrong.grid(row=1, column=0)
btn_right = Button(image=img_right, highlightthickness=0, command=btn_right_clicked)
btn_right.grid(row=1, column=1)

drawCard()
# --------------------------------- UI --------------------------------- #

window.mainloop()
