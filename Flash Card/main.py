BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict()
print(to_learn)

window = Tk()
window.title("Flashy")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthicknes=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=cross_image, highlightthicknes=0)
red_button.grid(row=1, column=0)

tick_button = PhotoImage(file="images/right.png")
green_button = Button(image=tick_button, highlightthicknes=0)
green_button.grid(row=1, column=1)



window.mainloop()