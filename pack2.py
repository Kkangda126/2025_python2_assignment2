from tkinter import *

root = Tk()
root.geometry("300x200")

button1 = Button(root, text="버튼1", bg="navy", fg="white")
button2 = Button(root, text="버튼2", bg="lightgreen", fg="black")
button3 = Button(root, text="버튼3", bg="blue", fg="white")
button1.pack(side=LEFT, padx=10)
button2.pack(side=LEFT, padx=10)
button3.pack(side=LEFT, padx=10)

root.mainloop()