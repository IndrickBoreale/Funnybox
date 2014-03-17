import Tkinter		# Tkinter will be imported
from Tkinter import *		# From Tkinter, import everything (symbolised by "*")

root=Tk()		# A new GUI is created and named "root"

widget=Label(root)		# A widget is added, a label, inside "root"
widget.config(text='This is the best damn line of text you have ever read. Good for you.',bg='black',fg='red')		# The widget is given content in the form of red text on a black background
widget.pack(side=TOP,expand=YES,fill=BOTH)		# The widget is configured to stay in the same place even after resizing the window



def result():		# A function is defined as "result"
	print("The sum of 2+2 is ",2+2)		# The function is given properties. It is told to print "The sum of 2+2 is 4" when executed
win=Frame()		# A frame called "win" is created inside the "root" GUI
win.pack()		# The frame is prepared to be modified
Label(win,text='Click Add to get the sum or Quit to Exit').pack(side=TOP)		# A label is created for the top of the frame with some text
Button(win,text='Add',command=result).pack(side=LEFT)			# A button is created, named, positioned,and programmed to execute "result"
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)		# Same as before, but this button is programmed to close the GUI



widget2=Button(root,text="Pointless button. DO NOT PRESS.")		# Another widget is added inside root, this time a button, that will read "press"
widget2.pack(side=TOP,expand=YES,fill=NONE)		# The button will also remain in place after resizing the window


widget2.mainloop()		# This part just runs the part called "widget2", and keeps it prepared for command input
root.mainloop()			# Same here, but for "root"
win.mainloop()			# And here, but for "win"
