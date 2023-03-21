from tkinter import *

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=400, height=400, background="white")

# Define the size of each square
square_size = 50

# Create the squares
for row in range(8):
    for col in range(8):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        if (row+col) % 2 == 0:
            color = "white"
        else:
            color = "black"
        tahvel.create_rectangle(x1, y1, x2, y2, fill=color)

tahvel.grid()

raam.mainloop()

