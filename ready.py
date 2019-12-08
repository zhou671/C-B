import tkinter
import numpy as np

class ready():
    def __init__(self,root):
        self.root = root
        self.buttonColor = '#%02x%02x%02x' % (255, 173, 51)
        self.QMQueue = []
        self.QMindex = None
        self.play = None
        self.cb = None
        self.QMprompt1 = None
        self.QMprompt2 = None
        self.QMprompt3 = None
        self.readyButton = tkinter.Button(self.root, text="Ready", width=25, command=self.nexttrans, font=('Helvetica', 20), bg=self.buttonColor)
        self.mycolor = '#%02x%02x%02x' % (255, 214, 153)


    def setpara(self, play, cb):
        self.play = play
        self.cb = cb
    

    def display(self):
        if len(self.QMQueue) == 0:
            k1 = list(np.random.choice(2, 2, replace=False))
            k2 = list(np.random.choice(2, 2, replace=False))
            self.QMQueue = [None] * 4
            self.QMQueue[1] = k1[0] * 2
            self.QMQueue[3] = k1[1] * 2
            self.QMQueue[0] = k2[0] * 2 + 1
            self.QMQueue[2] = k2[1] * 2 + 1

        self.QMindex = self.QMQueue.pop()
        self.QMprompt1 = tkinter.Label(self.root, text=self.play.names[self.QMindex]+' will be the Question Master.', bg=self.mycolor, font=('Helvetica', 20))
        self.QMprompt2 = tkinter.Label(self.root, text='Please give the computer to the Question Master', bg=self.mycolor, font=('Helvetica', 20))
        self.QMprompt3 = tkinter.Label(self.root, text=self.play.names[self.QMindex]+', press the button below when you ready.', bg=self.mycolor, font=('Helvetica', 20))

        self.QMprompt1.pack()
        self.QMprompt1.place(relx=0.25, rely=0.3)
        self.QMprompt2.pack()
        self.QMprompt2.place(relx=0.25, rely=0.4)
        self.QMprompt3.pack()
        self.QMprompt3.place(relx=0.25, rely=0.5)
        self.readyButton.pack()
        self.readyButton.place(relx=0.25, rely=0.6)

    def nexttrans(self):
        self.QMprompt1.pack_forget()
        self.QMprompt1.place_forget()
        self.QMprompt2.pack_forget()
        self.QMprompt2.place_forget()
        self.QMprompt3.pack_forget()
        self.QMprompt3.place_forget()
        self.readyButton.pack_forget()
        self.readyButton.place_forget()
        self.cb.setpara(self)
        self.cb.display()
      