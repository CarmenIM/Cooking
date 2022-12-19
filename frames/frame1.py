# Multi-frame tkinter application v2.3
import tkinter as tk
from PIL import ImageTk

bg_colour = "#3d6466"

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Are you ready for your random recipe?", bg=bg_colour, fg="white", font=("Shanti", 14)).pack()
        tk.Button(self, text="SHUFFLE",command=lambda: master.switch_frame(PageOne)).pack()

        logo_img = ImageTk.PhotoImage(file="assets/images/RRecipe_logo.png")
        logo_widget = tk.Label(self, image=logo_img)
        logo_widget.image = logo_img
        logo_widget.pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


