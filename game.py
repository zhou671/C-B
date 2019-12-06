import player
import data
import instruction

import tkinter


mycolor = '#%02x%02x%02x' % (255, 102, 102)
root = tkinter.Tk()
root.title("C&B")
root.geometry("1000x550")
#root.wm_attributes('-transparent', True)
root.configure(bg=mycolor)
ins = instruction.instruction(root)
ins.display()
 
root.mainloop()