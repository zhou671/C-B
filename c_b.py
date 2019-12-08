import tkinter
import numpy as np
import time
from data import *

class c_b():
    def __init__(self, root):
        self.root = root
        self.mycolor = '#%02x%02x%02x' % (255, 214, 153)
        self.score = [None] * 2
        self.score[0] = 0
        self.score[1] = 0
        self.questionSeq = []
        self.start = False
        self.catch = False
        self.timer = 60
        self.catchtime = 5
        self.catchtimer = None
        self.timePrompt = None
        self.curQ = None
        self.curA = [None] * 3
        self.curCA = None
        self.records = []
        self.Qindex = None
        self.prompt1 = None
        self.promtp2 = None
        self.QMindex = None
        self.play = None
        self.rdy = None
        self.curButton = None
        self.record = {
            "Qid": None,
            "Teammate": None,
            "QM": None,
            "Catch": None
        }
        self.answerButFuns = [self.button0, self.button1, self.button2]
        self.QMcorrectButton = tkinter.Button(self.root, bg=self.mycolor, text="Correct", width=10, font=('Helvetica', 20), anchor=tkinter.W, command = self.correctBut)
        self.QMwrongtButton = tkinter.Button(self.root, bg=self.mycolor, text="Wrong", width=10, font=('Helvetica', 20), anchor=tkinter.W, command = self.wrongBut)
        self.CatchcatchButton = tkinter.Button(self.root, bg=self.mycolor, text="Catch!", width=10, font=('Helvetica', 20), anchor=tkinter.W, command = self.catchBut)
        self.CatchpassButton = tkinter.Button(self.root, bg=self.mycolor, text="Pass", width=10, font=('Helvetica', 20), anchor=tkinter.W, command = self.passBut)
        self.QMteam = None
        self.redScore = None
        self.blueScore = None
        self.clock = False
        self.sb = None
        self.visited = 0

    def setscorBoard(self, sb):
        self.sb = sb

    def correctBut(self):
        self.record['QM'] = True
        self.prompt1.pack_forget()
        self.prompt1.place_forget()
        self.promtp2.pack_forget()
        self.promtp2.place_forget()
        self.QMcorrectButton.pack_forget()
        self.QMcorrectButton.place_forget()
        self.QMwrongtButton.pack_forget()
        self.QMwrongtButton.place_forget()

        self.prompt1 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Since you decide your teammate's answer is correct.", width=50, font=('Helvetica', 20), anchor=tkinter.W)
        self.promtp2 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Let the catcher decide whehter to catch or pass.", width=50, font=('Helvetica', 20), anchor=tkinter.W)

        self.prompt1.pack()
        self.prompt1.place(relx=0.1, rely=0.05)
        self.promtp2.pack()
        self.promtp2.place(relx=0.1, rely=0.15)

        self.CatchcatchButton.pack()
        self.CatchcatchButton.place(relx=0.1, rely=0.85)
        self.CatchpassButton.pack()
        self.CatchpassButton.place(relx=0.3, rely=0.85)
        self.catch = True
        self.start = False

    def wrongBut(self):
        self.record['QM'] = False
        self.prompt1.pack_forget()
        self.prompt1.place_forget()
        self.promtp2.pack_forget()
        self.promtp2.place_forget()
        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack_forget()
            self.curA[i].place_forget()

        for i in range(0, len(self.curQ)):
            self.curQ[i].pack_forget()
            self.curQ[i].place_forget()

        self.curCA.pack_forget()
        self.curCA.place_forget()
        self.QMcorrectButton.pack_forget()
        self.QMcorrectButton.place_forget()
        self.QMwrongtButton.pack_forget()
        self.QMwrongtButton.place_forget()

        self.nextTurn()

    def catchBut(self):
        self.record['Catch'] = True
        self.prompt1.pack_forget()
        self.prompt1.place_forget()
        self.promtp2.pack_forget()
        self.promtp2.place_forget()
        self.CatchcatchButton.pack_forget()
        self.CatchcatchButton.place_forget()
        self.CatchpassButton.pack_forget()
        self.CatchpassButton.place_forget()
        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack_forget()
            self.curA[i].place_forget()

        for i in range(0, len(self.curQ)):
            self.curQ[i].pack_forget()
            self.curQ[i].place_forget()

        self.curCA.pack_forget()
        self.curCA.place_forget()

        self.catch = False
        self.start = True
        self.catchtime = 5
        if self.record['Teammate'] == TriviaCA[self.Qindex]:
            self.score[self.QMteam] += 2
        else:
            self.score[(self.QMteam + 1) % 2] += 2
        self.nextTurn()

    def updateScore(self):
        self.redScore.pack_forget()
        self.redScore.place_forget()
        self.blueScore.pack_forget()
        self.blueScore.place_forget()
        self.redScore = tkinter.Label(self.root, fg='red', bg=self.mycolor, text=str(self.score[0]), width=5,font=('Helvetica', 20))
        self.blueScore = tkinter.Label(self.root, fg='blue', bg=self.mycolor, text=str(self.score[1]), width=5,font=('Helvetica', 20))
        self.redScore.pack()
        self.redScore.place(relx=0.9, rely=0.35)
        self.blueScore.pack()
        self.blueScore.place(relx=0.9, rely=0.45)

    def passBut(self):
        self.record['Catch'] = True
        self.prompt1.pack_forget()
        self.prompt1.place_forget()
        self.promtp2.pack_forget()
        self.promtp2.place_forget()
        self.CatchcatchButton.pack_forget()
        self.CatchcatchButton.place_forget()
        self.CatchpassButton.pack_forget()
        self.CatchpassButton.place_forget()
        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack_forget()
            self.curA[i].place_forget()

        for i in range(0, len(self.curQ)):
            self.curQ[i].pack_forget()
            self.curQ[i].place_forget()

        self.curCA.pack_forget()
        self.curCA.place_forget()
        self.catch = False
        self.start = True
        self.catchtime = 5
        self.score[self.QMteam] += 1
        self.nextTurn()

    def nextTurn(self):
        self.updateScore()
        self.records.append(self.record.copy())
        self.record = {
            "Qid": None,
            "Teammate": None,
            "QM": None,
            "Catch": None
        }
        if len(self.questionSeq) == 0:
            self.questionSeq = list(np.random.choice(23, 23, replace=False))
        self.Qindex = self.questionSeq.pop()
        print(self.Qindex)
        self.record['Qid'] = self.Qindex
        self.prompt1 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Read the question and answers aloud!", width=35, font=('Helvetica', 20), anchor=tkinter.W)
        self.promtp2 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Enter your teammate's choice.", width=35, font=('Helvetica', 20), anchor=tkinter.W)
        if len(TriviaQ[self.Qindex]) > 55:
            self.curQ = [None] * 2
            self.curQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex][0:55], width=55,font=('Helvetica', 20), anchor=tkinter.W)
            self.curQ[1] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex][55:len(TriviaQ[self.Qindex])], width=55,font=('Helvetica', 20), anchor=tkinter.W)
        else:
            self.curQ = [None]
            self.curQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex], width=55,font=('Helvetica', 20), anchor=tkinter.W)
        
        for i in range(0, len(TriviaA[self.Qindex])):
            ch = chr(ord('A') + i)
            self.curA[i] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaA[self.Qindex][i], width=25,font=('Helvetica', 20), anchor=tkinter.W)

        self.curButton = [None] * len(TriviaA[self.Qindex])
        for i in range(0, len(TriviaA[self.Qindex])):
            ch = chr(ord('A') + i)
            self.curButton[i] = tkinter.Button(self.root, bg=self.mycolor, text=ch, width=2, font=('Helvetica', 20), anchor=tkinter.W, command=self.answerButFuns[i])

        self.curCA = tkinter.Label(self.root, bg=self.mycolor, text="Correct Answer is: " + chr(ord('A') + TriviaCA[self.Qindex]), width=25,font=('Helvetica', 20), anchor=tkinter.W)

        self.prompt1.pack()
        self.prompt1.place(relx=0.1, rely=0.05)
        self.promtp2.pack()
        self.promtp2.place(relx=0.1, rely=0.15)
        for i in range(0, len(self.curQ)):
            self.curQ[i].pack()
            self.curQ[i].place(relx=0.1, rely=0.25 + 0.1 * i)

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack()
            self.curA[i].place(relx=0.2, rely=0.45 + 0.1 * i)

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curButton[i].pack()
            self.curButton[i].place(relx=0.1, rely=0.45 + 0.1 * i)

        self.curCA.pack()
        self.curCA.place(relx=0.1, rely=0.75)

    def button0(self):
        self.record['Teammate'] = 0
        self.bluffPhase()

    def button1(self):
        self.record['Teammate'] = 1
        self.bluffPhase()

    def button2(self):
        self.record['Teammate'] = 2
        self.bluffPhase()

    def bluffPhase(self):
        self.prompt1.pack_forget()
        self.prompt1.place_forget()
        self.promtp2.pack_forget()
        self.promtp2.place_forget()

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack_forget()
            self.curA[i].place_forget()

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curButton[i].pack_forget()
            self.curButton[i].place_forget()

        for i in range(0, len(TriviaA[self.Qindex])):
            ch = chr(ord('A') + i)
            self.curA[i] = tkinter.Label(self.root, bg=self.mycolor, text=ch + ". " + TriviaA[self.Qindex][i], width=25,font=('Helvetica', 20), anchor=tkinter.W)

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack()
            self.curA[i].place(relx=0.1, rely=0.45 + 0.1 * i)

        self.prompt1 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Decide whether your teammate's answer is correct or not.", width=50, font=('Helvetica', 20), anchor=tkinter.W)
        self.promtp2 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Remember, you can always bluff!", width=35, font=('Helvetica', 20), anchor=tkinter.W)

        self.prompt1.pack()
        self.prompt1.place(relx=0.1, rely=0.05)
        self.promtp2.pack()
        self.promtp2.place(relx=0.1, rely=0.15)

        self.QMcorrectButton.pack()
        self.QMcorrectButton.place(relx=0.1, rely=0.85)
        self.QMwrongtButton.pack()
        self.QMwrongtButton.place(relx=0.3, rely=0.85)

    def setpara(self, rdy):
        self.rdy = rdy
        self.QMindex = rdy.QMindex
        self.QMteam = rdy.QMindex % 2
        self.play = rdy.play

    def display(self):
        if len(self.questionSeq) == 0:
            self.questionSeq = list(np.random.choice(23, 23, replace=False))
        self.timer = 60
        self.catchtime = 5
        self.catchtimer = tkinter.Label(self.root, fg=self.play.colors[(self.QMindex+1)%2], bg=self.mycolor, text=str(self.timer), width=5,font=('Helvetica', 20))
        self.timePrompt = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text=str(self.catchtime), width=5,font=('Helvetica', 20))
        self.redScore = tkinter.Label(self.root, fg='red', bg=self.mycolor, text=str(self.score[0]), width=5,font=('Helvetica', 20))
        self.blueScore = tkinter.Label(self.root, fg='blue', bg=self.mycolor, text=str(self.score[1]), width=5,font=('Helvetica', 20))
        self.timePrompt.pack()
        self.timePrompt.place(relx=0.9, rely=0.05)
        self.catchtimer.pack()
        self.catchtimer.place(relx=0.9, rely=0.15)
        self.redScore.pack()
        self.redScore.place(relx=0.9, rely=0.35)
        self.blueScore.pack()
        self.blueScore.place(relx=0.9, rely=0.45)
        
        self.update_clock()
        
        if self.visited % 2 == 0:
            self.score = [None] * 2
            self.score[0] = 0
            self.score[1] = 0
            
        self.visited += 1
        self.record = {
            "Qid": None,
            "Teammate": None,
            "QM": None,
            "Catch": None
        }
        self.catch = False
        self.start = True
        self.Qindex = self.questionSeq.pop()
        self.record['Qid'] = self.Qindex
        self.prompt1 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Read the question and answers aloud!", width=35, font=('Helvetica', 20), anchor=tkinter.W)
        self.promtp2 = tkinter.Label(self.root, fg=self.play.colors[self.QMindex], bg=self.mycolor, text="Enter your teammate's choice.", width=35, font=('Helvetica', 20), anchor=tkinter.W)
        if len(TriviaQ[self.Qindex]) > 55:
            self.curQ = [None] * 2
            self.curQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex][0:55], width=55,font=('Helvetica', 20), anchor=tkinter.W)
            self.curQ[1] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex][55:len(TriviaQ[self.Qindex])], width=55,font=('Helvetica', 20), anchor=tkinter.W)
        else:
            self.curQ = [None]
            self.curQ[0] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaQ[self.Qindex], width=55,font=('Helvetica', 20), anchor=tkinter.W)
        
        for i in range(0, len(TriviaA[self.Qindex])):
            ch = chr(ord('A') + i)
            self.curA[i] = tkinter.Label(self.root, bg=self.mycolor, text=TriviaA[self.Qindex][i], width=25,font=('Helvetica', 20), anchor=tkinter.W)

        self.curButton = [None] * len(TriviaA[self.Qindex])
        for i in range(0, len(TriviaA[self.Qindex])):
            ch = chr(ord('A') + i)
            self.curButton[i] = tkinter.Button(self.root, bg=self.mycolor, text=ch, width=2, font=('Helvetica', 20), anchor=tkinter.W, command=self.answerButFuns[i])

        self.curCA = tkinter.Label(self.root, bg=self.mycolor, text="Correct Answer is: " + chr(ord('A') + TriviaCA[self.Qindex]), width=25,font=('Helvetica', 20), anchor=tkinter.W)

        self.prompt1.pack()
        self.prompt1.place(relx=0.1, rely=0.05)
        self.promtp2.pack()
        self.promtp2.place(relx=0.1, rely=0.15)
        for i in range(0, len(self.curQ)):
            self.curQ[i].pack()
            self.curQ[i].place(relx=0.1, rely=0.25 + 0.1 * i)

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curA[i].pack()
            self.curA[i].place(relx=0.2, rely=0.45 + 0.1 * i)

        for i in range(0, len(TriviaA[self.Qindex])):
            self.curButton[i].pack()
            self.curButton[i].place(relx=0.1, rely=0.45 + 0.1 * i)

        self.curCA.pack()
        self.curCA.place(relx=0.1, rely=0.75)

    def update_clock(self):
        if self.start:
            self.timer -= 1
            if self.timer == 0:
                self.prompt1.pack_forget()
                self.prompt1.place_forget()
                self.promtp2.pack_forget()
                self.promtp2.place_forget()

                for i in range(0, len(TriviaA[self.Qindex])):
                    self.curA[i].pack_forget()
                    self.curA[i].place_forget()

                for i in range(0, len(TriviaA[self.Qindex])):
                    self.curButton[i].pack_forget()
                    self.curButton[i].place_forget()

                for i in range(0, len(self.curQ)):
                    self.curQ[i].pack_forget()
                    self.curQ[i].place_forget()

                self.CatchcatchButton.pack_forget()
                self.CatchcatchButton.place_forget()
                self.CatchpassButton.pack_forget()
                self.CatchpassButton.place_forget()
                self.curCA.pack_forget()
                self.curCA.place_forget()
                self.QMcorrectButton.pack_forget()
                self.QMcorrectButton.place_forget()
                self.QMwrongtButton.pack_forget()
                self.QMwrongtButton.place_forget()
                self.redScore.pack_forget()
                self.redScore.place_forget()
                self.blueScore.pack_forget()
                self.blueScore.place_forget()
                self.timePrompt.pack_forget()
                self.timePrompt.place_forget()
                self.catchtimer.pack_forget()
                self.catchtimer.place_forget()
                self.catch = False
                self.start = False
                self.sb.setpara(self)
                self.sb.display()
                return

        if self.catch:
            self.catchtime -= 1
            if self.catchtime == 0:
                self.passBut()
        self.timePrompt.configure(text=str(self.timer))
        self.catchtimer.configure(text=str(self.catchtime))
        self.root.after(1000, self.update_clock)

    