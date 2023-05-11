from tkinter import *
import pandas
from random import choice
import time
BACKGROUND_COLOR = "#B1DDC6"
#--------------------------CARD CREATION-------------------------------#
data = pandas.read_csv("data\GermanWords.csv")
cards = data.to_dict(orient="records")
rand_card = {}


def gen_word():
    right.config(state="disabled")
    wrong.config(state="disabled")
    global rand_card
    rand_card = choice(cards)
    card.itemconfig(canvas_image, image=front_image)
    card.itemconfig(language, text="German", fill="black")
    card.itemconfig(word, text=rand_card["german"], fill="black")
    window.after(3000, func=flip)

#--------------------------CARD FLIP-------------------------------#
def flip(): #flips card
    right.config(state="normal")
    wrong.config(state="normal")
    card.itemconfig(canvas_image, image=back_image)
    card.itemconfig(word, text=rand_card["english"], fill="white")
    card.itemconfig(language, text="English", fill="white")

def known_card(): #removes known words
    cards.remove(rand_card)
    df = pandas.DataFrame(cards)
    df.to_csv("data/GermanWords.csv", index=False)
    gen_word()
#--------------------------UI SETUP-------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = card.create_image(400, 250, image=front_image)
card.grid(column=1, row=1, columnspan=2)
language = card.create_text(400,150,text="German", font=("comic sans", 20, "italic"))
word = card.create_text(400,250,text="German", font=("comic sans", 40, "bold"))

#labels

#buttons
right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, command=known_card, highlightthickness=0)
right.grid(column=2, row=2)
wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, command=gen_word, highlightthickness=0)
wrong.grid(column=1, row=2)

gen_word()

window.mainloop()
