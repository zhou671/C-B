import tkinter
from data import *


class scoreBoard():
    def __init__(self, root):
        self.root = root
        self.mycolor = '#%02x%02x%02x' % (255, 214, 153)
        self.buttonColor = '#%02x%02x%02x' % (255, 173, 51)
        self.cb = None
        self.visited = 0
        self.records = None
        self.reportHisBut = tkinter.Button(self.root, bg=self.buttonColor, text="Report results", width=25, font=('Helvetica', 20), anchor=tkinter.W, command = self.hisBut)
        self.winningPrompt = None
        self.nextRd = tkinter.Button(self.root, bg=self.buttonColor, text="Next Round", width=25, font=('Helvetica', 20), anchor=tkinter.W, command=self.nextRound)
        self.result = False
        self.goBack = tkinter.Button(self.root, bg=self.buttonColor, text="Go Back", width=10, font=('Helvetica', 20), anchor=tkinter.W, command=self.backMain)
        self.curQ = None
        self.curA = [None] * 3
        self.curCA = None
        self.Qindex = None
        self.index= None
        self.QMlabel = None
        self.Catch = None
        self.choice = None
        self.QMteam = None
        self.back = tkinter.Button(self.root, bd = 0, bg=self.mycolor, text="<<Back", width=10, font=('Helvetica', 20), anchor=tkinter.W, command=self.back)
        self.next = tkinter.Button(self.root, bd = 0, bg=self.mycolor, text="Next>>", width=10, font=('Helvetica', 20), anchor=tkinter.W, command=self.next)

    def back(self):
        if self.index == 0:
            return
        self.index -= 1
        self.question()

    def next(self):
        if self.index == len(self.records) - 1:
            return
        self.index += 1
        self.question()

    def setpara(self, cb):
        self.cb = cb
        self.records = cb.records
        self.QMteam = cb.QMteam
    
    def display(self):
        self.reportHisBut.pack()
        self.reportHisBut.place(relx = 0.3, rely=0.4)
        if self.visited % 2 == 1:
            string = None
            if self.cb.score[0] > self.cb.score[1]:
                string = "Red team wins!"
            else:
                string = "Blue team wins!"
            self.winningPrompt = tkinter.Label(self.root, bg=self.mycolor, text=string, width=25, font=('Helvetica', 20), anchor=tkinter.W)
            self.winningPrompt.pack()
            self.winningPrompt.place(relx = 0.3, rely=0.7)
            self.result = False
        else:
            self.nextRd.pack()
            self.nextRd.place(relx = 0.3, rely=0.7)

        self.visited += 1

    def nextRound(self):
        self.nextRd.pack_forget()
        self.nextRd.place_forget()
        self.reportHisBut.pack_forget()
        self.reportHisBut.place_forget()
        self.cb.rdy.display()

    def hisBut(self):
        self.index= 0
        if self.winningPrompt != None:
            self.winningPrompt.pack_forget()
            self.winningPrompt.place_forget()
        self.nextRd.pack_forget()
        self.nextRd.place_forget()
        self.reportHisBut.pack_forget()
        self.reportHisBut.place_forget()
        self.nextRd.pack_forget()
        self.nextRd.place_forget()
        self.question()
        self.back.pack()
        self.next.pack()
        self.back.place(relx = 0.45, rely = 0.9)
        self.next.place(relx = 0.85, rely = 0.9)
        self.goBack.pack()
        self.goBack.place(relx = 0.65, rely = 0.9)


    def question(self):
        if self.curCA != None and self.QMlabel != None and self.Catch != None and self.choice != None:
            self.curCA.pack_forget()
            self.QMlabel.pack_forget()
            self.Catch.pack_forget()
            self.choice.pack_forget()

            self.curCA.place_forget()
            self.QMlabel.place_forget()
            self.Catch.place_forget()
            self.choice.place_forget()

        self.Qindex = self.records[self.index]['Qid']

        for i in range(0, len(TriviaA[self.Qindex])):
            if self.curA[i] != None:
                self.curA[i].pack_forget()
                self.curA[i].place_forget()
        
        if self.curQ != None:
            for i in range(0, len(self.curQ)):
                if self.curQ[i] != None:
                    self.curQ[i].pack_forget()
                    self.curQ[i].place_forget()

        if len(TriviaQ[self.Qindex]) > 55:
            self.curQ = [None] * 2
            self.curQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex][0:55], width=55,font=('Helvetica', 20), anchor=tkinter.W)
            self.curQ[1] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex][55:len(TriviaQ[self.Qindex])], width=55,font=('Helvetica', 20), anchor=tkinter.W)
        else:
            self.curQ = [None]
            self.curQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex], width=55,font=('Helvetica', 20), anchor=tkinter.W)

        for i in range(0, len(TriviaA[self.Qindex])):
            ch = chr(ord('A') + i)
            self.curA[i] = tkinter.Label(self.root, bg=self.mycolor, text=ch + ". " + TriviaA[self.Qindex][i], width=25,font=('Helvetica', 20), anchor=tkinter.W)

        self.curCA = tkinter.Label(self.root, bg=self.mycolor, text="Correct Answer is: " + chr(ord('A') + TriviaCA[self.Qindex]), width=25,font=('Helvetica', 20), anchor=tkinter.W)
        self.QMlabel = tkinter.Label(self.root, fg=self.cb.play.colors[self.QMteam], bg=self.mycolor, text="Question Master decide the question is: " + str(self.records[self.index]['QM']), width=50,font=('Helvetica', 20), anchor=tkinter.W)
        self.Catch = tkinter.Label(self.root, fg=self.cb.play.colors[self.QMteam + 1], bg=self.mycolor, text="Whether catchers catched: " + str(self.records[self.index]['Catch']), width=25,font=('Helvetica', 20), anchor=tkinter.W)
        self.choice = tkinter.Label(self.root, fg=self.cb.play.colors[self.QMteam], bg=self.mycolor, text="Teammate's Answer" + chr(ord('A') + self.records[self.index]['Teammate']), width=20,font=('Helvetica', 20), anchor=tkinter.W)

        for i in range(0, len(self.curQ)):
            self.curQ[i].pack()
            self.curQ[i].place(relx=0.1, rely=0.25 + 0.1 * i)

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack()
            self.curA[i].place(relx=0.1, rely=0.45 + 0.1 * i)

        self.curCA.pack()
        self.curCA.place(relx=0.1, rely=0.75)

        self.QMlabel.pack()
        self.Catch.pack()
        self.choice.pack()

        self.QMlabel.place(relx=0.1, rely=0.05)
        self.Catch.place(relx=0.1, rely=0.15)
        self.choice.place(relx=0.1, rely=0.85)


    def backMain(self):
        if self.curCA != None and self.QMlabel != None and self.Catch != None and self.choice != None:
            self.curCA.pack_forget()
            self.QMlabel.pack_forget()
            self.Catch.pack_forget()
            self.choice.pack_forget()

            self.curCA.place_forget()
            self.QMlabel.place_forget()
            self.Catch.place_forget()
            self.choice.place_forget()

        self.Qindex = self.records[self.index]['Qid']

        for i in range(0, len(TriviaA[self.Qindex])):
            if self.curA[i] != None:
                self.curA[i].pack_forget()
                self.curA[i].place_forget()
        
        if self.curQ != None:
            for i in range(0, len(self.curQ)):
                if self.curQ[i] != None:
                    self.curQ[i].pack_forget()
                    self.curQ[i].place_forget()
                    
        self.back.pack_forget()
        self.next.pack_forget()
        self.back.place_forget()
        self.next.place_forget()
        self.goBack.pack_forget()
        self.goBack.place_forget()

        self.reportHisBut.pack()
        self.reportHisBut.place(relx = 0.3, rely=0.4)
        if self.visited % 2 == 0:
            string = None
            if self.cb.score[0] > self.cb.score[1]:
                string = "Red team win!"
            else:
                string = "Blue team win!"
            self.winningPrompt = tkinter.Label(self.root, bg=self.mycolor, text=string, width=25, font=('Helvetica', 20), anchor=tkinter.W)
            self.winningPrompt.pack()
            self.winningPrompt.place(relx = 0.3, rely=0.7)
            self.result = False
        else:
            self.nextRd.pack()
            self.nextRd.place(relx = 0.3, rely=0.7)
        

        
