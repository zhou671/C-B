import tkinter
from PIL import Image, ImageTk

class start():
    def __init__(self, root):
        self.buttonColor = '#%02x%02x%02x' % (255, 173, 51)
        self.root = root
        self.logoImage = tkinter.PhotoImage(file="./logo.gif")
        self.CBlogo = tkinter.Label(self.root, image=self.logoImage)
        self.CBlogo.image = self.logoImage
        self.playButton = tkinter.Button(self.root, text = "Play", bg=self.buttonColor, width=10, font=('Helvetica', 20), command=self.playtrans)
        self.instButton = tkinter.Button(self.root, text = "Instruction", bg=self.buttonColor, width=10, font=('Helvetica', 20), command=self.insttrains)

        self.inst = None
        self.play = None

    def setpara(self, inst, play):
        self.inst = inst
        self.play = play

    def display(self):
        self.CBlogo.pack()
        self.CBlogo.place(relx=0.3, rely=0.2)
        self.playButton.pack()
        self.playButton.place(relx=0.3, rely=0.6) 
        self.instButton.pack()
        self.instButton.place(relx=0.5, rely=0.6)

    def clean(self):
        self.CBlogo.pack_forget()
        self.CBlogo.place_forget()
        self.playButton.pack_forget()
        self.playButton.place_forget()
        self.instButton.pack_forget()
        self.instButton.place_forget()

    def playtrans(self):
        self.clean()
        self.play.display()

    def insttrains(self):
        self.clean()
        self.inst.displayf1()
