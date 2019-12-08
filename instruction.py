import tkinter
from data import *

class instruction():
    def __init__(self, root):
        self.root = root
        self.mycolor = '#%02x%02x%02x' % (255, 214, 153)
        self.frame = 0
        
        self.nextButton = tkinter.Button(self.root, bg=self.mycolor, bd = 0, text="Next>>", width=10,font=('Helvetica', 20), command=self.nexttrans)

        # frame1
        self.QMlabel = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Question Master", width=30,font=('Helvetica', 20))
        self.TMlabel = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Teammate", width=25,font=('Helvetica', 20))
        self.c1label = tkinter.Label(self.root, fg="blue", bg=self.mycolor, text="Catcher1", width=25,font=('Helvetica', 20))
        self.c2label = tkinter.Label(self.root, fg="blue", bg=self.mycolor, text="Catcher2", width=25,font=('Helvetica', 20))
        self.team1label = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Team Red", width=25,font=('Helvetica', 20))
        self.team2label = tkinter.Label(self.root, fg="blue", bg=self.mycolor, text="Team Blue", width=25,font=('Helvetica', 20))
        
        # frame2
        self.prompt4A = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Read the question and answers aloud!", width=35, font=('Helvetica', 20), anchor=tkinter.W)
        self.prompt5A = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Enter your teammate's choice.", width=35, font=('Helvetica', 20), anchor=tkinter.W)
        if len(TriviaQ[13]) > 50:
            self.exampleQ = [None] * 2
            self.exampleQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[13][0:50], width=50,font=('Helvetica', 20), anchor=tkinter.W)
            self.exampleQ[1] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[13][50:len(TriviaQ[13])], width=50,font=('Helvetica', 20), anchor=tkinter.W)
        else:
            self.exampleQ = [None]
            self.exampleQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[13], width=50,font=('Helvetica', 20), anchor=tkinter.W)
        
        self.exmapleA = [None] * len(TriviaA[13])
        for i in range(0, len(TriviaA[13])):
            ch = chr(ord('A') + i)
            self.exmapleA[i] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaA[13][i], width=25,font=('Helvetica', 20), anchor=tkinter.W)

        self.exampleButton = [None] * len(TriviaA[13])
        for i in range(0, len(TriviaA[13])):
            ch = chr(ord('A') + i)
            self.exampleButton[i] = tkinter.Button(self.root, bg=self.mycolor, text=ch, width=2, font=('Helvetica', 20), anchor=tkinter.W)

        self.exampleCA = tkinter.Label(self.root, bg=self.mycolor, text="Correct Answer is: " + chr(ord('A') + TriviaCA[13]), width=25,font=('Helvetica', 20), anchor=tkinter.W)

        # frame3
        self.prompt4QM = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Decide whether your teammate's answer is correct or not.", width=50, font=('Helvetica', 20), anchor=tkinter.W)
        self.prompt5QM = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Remember, you can always bluff!", width=35, font=('Helvetica', 20), anchor=tkinter.W)

        self.QMcorrectButton = tkinter.Button(self.root, bg=self.mycolor, text="Correct", width=10, font=('Helvetica', 20), anchor=tkinter.W)
        self.QMwrongtButton = tkinter.Button(self.root, bg=self.mycolor, text="Wrong", width=10, font=('Helvetica', 20), anchor=tkinter.W)

        # frame4
        self.prompt4Cat = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="Since you decide your teammate's answer is correct, ", width=40, font=('Helvetica', 20), anchor=tkinter.W)
        self.prompt5Cat = tkinter.Label(self.root, fg="red", bg=self.mycolor, text="let the catcher decide whehter to catch or pass.", width=40, font=('Helvetica', 20), anchor=tkinter.W)
        self.CatchcatchButton = tkinter.Button(self.root, bg=self.mycolor, text="Catch!", width=10, font=('Helvetica', 20), anchor=tkinter.W)
        self.CatchpassButton = tkinter.Button(self.root, bg=self.mycolor, text="Pass", width=10, font=('Helvetica', 20), anchor=tkinter.W)

        self.play = None

    def setpara(self, play):
        self.play=play

    def displayf1(self):
        self.QMlabel.pack()
        self.TMlabel.pack()
        self.c1label.pack()
        self.c2label.pack()
        self.team1label.pack()
        self.team2label.pack()

        self.QMlabel.place(relx=0.1, rely=0.4)
        self.TMlabel.place(relx=0.1, rely=0.6)
        self.c1label.place(relx=0.5, rely=0.4)
        self.c2label.place(relx=0.5, rely=0.6)
        self.team1label.place(relx=0.1, rely=0.2)
        self.team2label.place(relx=0.5, rely=0.2)
        
        self.nextButton.pack()
        self.nextButton.place(relx = 0.85, rely = 0.9)

    def cleanf1(self):
        self.QMlabel.pack_forget()
        self.TMlabel.pack_forget()
        self.c1label.pack_forget()
        self.c2label.pack_forget()
        self.team1label.pack_forget()
        self.team2label.pack_forget()

        self.QMlabel.place_forget()
        self.TMlabel.place_forget()
        self.c1label.place_forget()
        self.c2label.place_forget()
        self.team1label.place_forget()
        self.team2label.place_forget()

    def displayf2(self):
        self.prompt4A.pack()
        self.prompt4A.place(relx=0.1, rely=0.05)
        self.prompt5A.pack()
        self.prompt5A.place(relx=0.1, rely=0.15)
        for i in range(0, len(self.exampleQ)):
            self.exampleQ[i].pack()
            self.exampleQ[i].place(relx=0.1, rely=0.25 + 0.1 * i)

        for i in range(0, len(TriviaA[13])):
            self.exmapleA[i].pack()
            self.exmapleA[i].place(relx=0.15, rely=0.45 + 0.1 * i)

        for i in range(0, len(TriviaA[13])):
            self.exampleButton[i].pack()
            self.exampleButton[i].place(relx=0.1, rely=0.45 + 0.1 * i)

        self.exampleCA.pack()
        self.exampleCA.place(relx=0.1, rely=0.75)

    def displayf3(self):
        self.prompt4A.pack_forget()
        self.prompt4A.place_forget()
        self.prompt5A.pack_forget()
        self.prompt5A.place_forget()

        for i in range(0, len(TriviaA[13])):
            self.exmapleA[i].pack_forget()
            self.exmapleA[i].place_forget()

        for i in range(0, len(TriviaA[13])):
            self.exampleButton[i].pack_forget()
            self.exampleButton[i].place_forget()

        for i in range(0, len(TriviaA[13])):
            ch = chr(ord('A') + i)
            self.exmapleA[i] = tkinter.Label(self.root, bg=self.mycolor, text=ch + ". " + TriviaA[13][i], width=25,font=('Helvetica', 20), anchor=tkinter.W)

        for i in range(0, len(TriviaA[13])):
            self.exmapleA[i].pack()
            self.exmapleA[i].place(relx=0.1, rely=0.45 + 0.1 * i)

        self.prompt4QM.pack()
        self.prompt4QM.place(relx=0.1, rely=0.05)
        self.prompt5QM.pack()
        self.prompt5QM.place(relx=0.1, rely=0.15)

        self.QMcorrectButton.pack()
        self.QMcorrectButton.place(relx=0.1, rely=0.85)
        self.QMwrongtButton.pack()
        self.QMwrongtButton.place(relx=0.3, rely=0.85)

    def displayf4(self):
        self.prompt4QM.pack_forget()
        self.prompt4QM.place_forget()
        self.prompt5QM.pack_forget()
        self.prompt5QM.place_forget()
        self.QMcorrectButton.pack_forget()
        self.QMcorrectButton.place_forget()
        self.QMwrongtButton.pack_forget()
        self.QMwrongtButton.place_forget()

        self.prompt4Cat.pack()
        self.prompt4Cat.place(relx=0.1, rely=0.05)
        self.prompt5Cat.pack()
        self.prompt5Cat.place(relx=0.1, rely=0.15)

        self.CatchcatchButton.pack()
        self.CatchcatchButton.place(relx=0.1, rely=0.85)
        self.CatchpassButton.pack()
        self.CatchpassButton.place(relx=0.3, rely=0.85)

    def clean(self):
        self.CatchcatchButton.pack_forget()
        self.CatchcatchButton.place_forget()
        self.CatchpassButton.pack_forget()
        self.CatchpassButton.place_forget()
        
        self.prompt4Cat.pack_forget()
        self.prompt4Cat.place_forget()
        self.prompt5Cat.pack_forget()
        self.prompt5Cat.place_forget()

        for i in range(0, len(TriviaA[13])):
            self.exmapleA[i].pack_forget()
            self.exmapleA[i].place_forget()

        self.nextButton.pack_forget()
        self.nextButton.place_forget()
        for i in range(0, len(self.exampleQ)):
            self.exampleQ[i].pack_forget()
            self.exampleQ[i].place_forget()

        self.exampleCA.pack_forget()
        self.exampleCA.place_forget()

    def nexttrans(self):
        if self.frame == 0:
            self.frame += 1
            self.cleanf1()
            self.displayf2()
            return

        if self.frame == 1:
            self.frame += 1
            self.displayf3()
            return
    
        if self.frame == 2:
            self.frame += 1
            self.displayf4()
            return

        if self.frame == 3:
            self.clean()
            self.play.display()