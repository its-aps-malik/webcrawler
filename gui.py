from tkinter import *


root = Tk()


newframe = Frame(root)
newframe.pack(side=TOP)

new2frame = Frame(root)
new2frame.pack(side=BOTTOM)

button1 = Button(new2frame, text="crawl", bg="Red")
button2 = Button(newframe, text="box", bg="Blue")

lable1 = Label(newframe, text="Enter the text : ")

button1.pack()
button2.pack()
lable1.pack()


root.mainloop()