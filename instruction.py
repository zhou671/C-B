import tkinter
from PIL import Image, ImageTk


class instruction():
    def __init__(self, root):
        self.root = root
        self.logoImage = tkinter.PhotoImage(file="./logo.gif")
        self.CBlogo = tkinter.Label(self.root, image=self.logoImage)
        self.CBlogo.image = self.logoImage
        self.

    def display(self):
        self.CBlogo.pack()
        self.CBlogo.place(relx=0.3, rely=0.2)

    def clean(self):
        self.CBlogo.pack_forget()
        self.CBlogo.place_forget()
