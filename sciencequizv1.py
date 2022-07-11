#Science Quiz version 1
#sciencequizv1
#S.Chang Apr

from tkinter import *

def screen1():
    global frame1
    global frame2
    
    frame2.grid_remove()
    frame1 = LabelFrame(root, height="450", width="400", bg="grey")
    frame1.grid(row=0, column=0)

    titlelabel = Label(frame1, bg="black", fg="lightgrey", width=20, padx=30, pady=10, text="Welcome to the Science Quiz", font=("Helvetica", "14"))
    titlelabel.grid(columnspan=2)

    button1 = Button(frame1, text="Next", anchor=W, command=screen2)
    button1.grid(row=8, column=1)

def screen2():
    global frame1
    global frame2
    
    frame1.grid_remove()
    
    frame2 = LabelFrame(root, height="450", width="400", bg="green")
    frame2.grid(row=0, column=1)

    home = Button(frame2, text="Home", anchor=W, command=screen1)
    home.grid(row=3, column=0)

root= Tk()
root.title("Science Quiz v1")
root.geometry("600x300+850+0")
frame1= Frame(root)
frame2= Frame(root)
screen1()

root.mainloop()