BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *





window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

window.mainloop()
