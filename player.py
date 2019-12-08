import tkinter
import math

class player():
    def __init__(self, root):
        self.root = root
        self.names = [None] * 4
        self.hasName = [False] * 4
        self.team = [None] * 4
        self.namePrompt = [None] * 4
        self.nameEntry = [None] * 4
        self.nameButton = [None] * 4
        self.colors = ['red', 'blue', 'red', 'blue']
        self.buttonfuncs = [self.button0, self.button1, self.button2, self.button3]
        self.count = 0
        self.buttonColor = '#%02x%02x%02x' % (255, 173, 51)
        self.mycolor = '#%02x%02x%02x' % (255, 214, 153)
        self.erase = False

        for i in range(0,4):
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = "Enter your name:", font=('Helvetica', 20), anchor=tkinter.W)
            self.nameEntry[i] = tkinter.Entry(self.root, font=('Helvetica', 20))
            self.nameButton[i] = tkinter.Button(self.root, text="Confirm", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)

        self.teamRed = tkinter.Label(self.root, fg='red', bg=self.mycolor, text = "Team Red", font=('Helvetica', 20), anchor=tkinter.W)
        self.teamBlue = tkinter.Label(self.root, fg='blue', bg=self.mycolor, text = "Team Blue", font=('Helvetica', 20), anchor=tkinter.W)
        self.nextButton = tkinter.Button(self.root, bg=self.mycolor, bd = 0, text="Next>>", width=10,font=('Helvetica', 20), command=self.nexttrans)
        self.rdy = None

    def setpara(self, rdy):
        self.rdy = rdy

    def button0(self):
        i = 0
        if self.hasName[i]:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = False
            self.count -= 1
            if self.count == 3:
                self.erase = True
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = "Enter your name", font=('Helvetica', 20), anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="Confirm", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameEntry[i].pack()
            self.nameEntry[i].place(relx=i % 2 * 0.5, rely=0.3 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))
        else:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameEntry[i].pack_forget()
            self.nameEntry[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = True
            self.count += 1
            self.names[i] = self.nameEntry[i].get()
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = self.names[i] + " Ready!", font=('Helvetica', 20), width=25, anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="ReEnter your name", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))

        if self.erase:
            self.nextButton.pack_forget()
            self.nextButton.place_forget()
            self.erase = False

        if self.count == 4:
            self.nextButton.pack()
            self.nextButton.place(relx = 0.85, rely = 0.9)

    def button1(self):
        i = 1
        if self.hasName[i]:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = False
            self.count -= 1
            if self.count == 3:
                self.erase = True
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = "Enter your name", font=('Helvetica', 20), anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="Confirm", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameEntry[i].pack()
            self.nameEntry[i].place(relx=i % 2 * 0.5, rely=0.3 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))
        else:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameEntry[i].pack_forget()
            self.nameEntry[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = True
            self.count += 1
            self.names[i] = self.nameEntry[i].get()
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = self.names[i] + " Ready!", font=('Helvetica', 20), width=25, anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="ReEnter your name", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))

        if self.erase:
            self.nextButton.pack_forget()
            self.nextButton.place_forget()
            self.erase = False

        if self.count == 4:
            self.nextButton.pack()
            self.nextButton.place(relx = 0.85, rely = 0.9)

    def button2(self):
        i = 2
        if self.hasName[i]:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = False
            self.count -= 1
            if self.count == 3:
                self.erase = True
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = "Enter your name", font=('Helvetica', 20), anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="Confirm", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameEntry[i].pack()
            self.nameEntry[i].place(relx=i % 2 * 0.5, rely=0.3 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))
        else:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameEntry[i].pack_forget()
            self.nameEntry[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = True
            self.count += 1
            self.names[i] = self.nameEntry[i].get()
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = self.names[i] + " Ready!", font=('Helvetica', 20), width=25, anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="ReEnter your name", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))

        if self.erase:
            self.nextButton.pack_forget()
            self.nextButton.place_forget()
            self.erase = False

        if self.count == 4:
            self.nextButton.pack()
            self.nextButton.place(relx = 0.85, rely = 0.9)

    def button3(self):
        i = 3
        if self.hasName[i]:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = False
            self.count -= 1
            if self.count == 3:
                self.erase = True
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = "Enter your name", font=('Helvetica', 20), anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="Confirm", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameEntry[i].pack()
            self.nameEntry[i].place(relx=i % 2 * 0.5, rely=0.3 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))
        else:
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameEntry[i].pack_forget()
            self.nameEntry[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()
            self.hasName[i] = True
            self.count += 1
            self.names[i] = self.nameEntry[i].get()
            self.namePrompt[i] = tkinter.Label(self.root, fg=self.colors[i], bg=self.mycolor, text = self.names[i] + " Ready!", font=('Helvetica', 20), width=25, anchor=tkinter.W)
            self.nameButton[i] = tkinter.Button(self.root, text="ReEnter your name", width=25, command=self.buttonfuncs[i], font=('Helvetica', 20), bg=self.buttonColor)
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))

        if self.erase:
            self.nextButton.pack_forget()
            self.nextButton.place_forget()
            self.erase = False

        if self.count == 4:
            self.nextButton.pack()
            self.nextButton.place(relx = 0.85, rely = 0.9)


    def display(self):
        self.teamRed.pack()
        self.teamRed.place(relx = 0, rely = 0.1)
        self.teamBlue.pack()
        self.teamBlue.place(relx = 0.5, rely = 0.1)
        for i in range(0, 4):
            self.namePrompt[i].pack()
            self.namePrompt[i].place(relx=i % 2 * 0.5, rely=0.2 + 0.3 * math.floor(i / 2))
            self.nameEntry[i].pack()
            self.nameEntry[i].place(relx=i % 2 * 0.5, rely=0.3 + 0.3 * math.floor(i / 2))
            self.nameButton[i].pack()
            self.nameButton[i].place(relx=i % 2 * 0.5, rely=0.4 + 0.3 * math.floor(i / 2))
        return

    def nexttrans(self):
        self.teamRed.pack_forget()
        self.teamRed.place_forget()
        self.teamBlue.pack_forget()
        self.teamBlue.place_forget()
        for i in range(0,4):
            self.namePrompt[i].pack_forget()
            self.namePrompt[i].place_forget()
            self.nameButton[i].pack_forget()
            self.nameButton[i].place_forget()

        self.nextButton.pack_forget()
        self.nextButton.place_forget()
        self.rdy.display()
