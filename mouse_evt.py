from tkinter import *

def left_click(event):
    print(f"좌측 버튼이 ({event.x},{event.x})")

def right_click(event):
    print(f"우측 버튼이 ({event.x},{event.x})")

root = Tk()

frame = Frame(root, width = 200, height = 200)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-3>", right_click)
frame.pack()

root.mainloop()