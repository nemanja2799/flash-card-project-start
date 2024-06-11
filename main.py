BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timmer
    window.after_cancel(flip_timmer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timmer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# window create
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timmer = window.after(3000, func=flip_card)

# image create
card_front_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_img = PhotoImage(file="images/card_back.png")

# text create
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("ariel", 60, "bold"))

# wrong button
wrong_button_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# right button
right_button_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
