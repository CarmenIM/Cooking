import csv
import random
from tkinter import *


#Create an instance of tkinter frame
win= Tk()

#Set the geometry
win.geometry("750x280")

#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="SpringGreen2")

with open ("recipes.csv") as recipes:
    csv_reader = csv.reader(recipes)
    next(csv_reader)
    return(random.choice([line[0] + line[1] + line[2] for line in csv_reader]))



#Add a text in Canvas
canvas.create_text(300, 50, text= 50 , fill="black", font=('Helvetica 15 bold'))
canvas.pack()

# win.mainloop()