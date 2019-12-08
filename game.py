from player import *
import data
from start import *
from instruction import *
from c_b import *
from ready import *
from scoreBoard import *

import tkinter


mycolor = '#%02x%02x%02x' % (255, 214, 153)
root = tkinter.Tk()
root.title("C&B")
root.geometry("1000x550")
#root.wm_attributes('-transparent', True)
root.configure(bg=mycolor)


startFrame = start(root)
play = player(root)
inst = instruction(root)
rdy = ready(root)
cb = c_b(root)
sb = scoreBoard(root)

cb.setscorBoard(sb)
inst.setpara(startFrame)
startFrame.setpara(inst, play)
play.setpara(rdy)
rdy.setpara(play, cb)

startFrame.display()
 
root.mainloop()