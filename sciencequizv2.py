#Science Quiz version 2
#sciencequizv2
#S.Chang Apr

from tkinter import *



class sciencequiz:
    def __init__(self, parent):

        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)

        self.titlelabel = Label(self.frame1, bg="black", fg="lightgrey", width=20, padx=30, pady=10, text="Welcome to the Science Quiz", font=("Helvetica", "14"))
        self.titlelabel.grid(columnspan=2)

        self.button1 = Button(self.frame1, text="Next", anchor=W, command=self.screen1)
        self.button1.grid(row=8, column=1)

        self.name = StringVar()
        self.NameEntry = Entry(self.frame1, width=15, textvariable=self.name)
        self.NameEntry.grid(row=1, column=1, sticky=W)
        
        self.age = IntVar() 
        self.AgeEntry = Entry(self.frame1, width=15, textvariable=self.age)
        self.AgeEntry.grid(row=2, column=1, sticky=W)

        self.warning = Label(self.frame1, text="Please enter your name", width=25)
        self.warning.grid(row=1, column=0, sticky=W)


        self.frame2 = Frame(parent)

        self.questions = Label(self.frame2, bg="black", fg="white", width=20, padx=30, pady=10, text="Questions", font=("Helvetica", "14"))
        self.questions.grid(columnspan=2)

        self.questionlabel = Label(self.frame2, text="", width=15, height=3)
        self.questionlabel.grid(row=1, column=0, sticky=W)

        self.home = Button(self.frame2, text="Home", anchor=W, command=self.home)
        self.home.grid(row=3, column=0)

    def home(self):
        
        self.NameEntry.delete(0, END)
        self.AgeEntry.delete(0, END)
        self.screen1()

    def screen1(self):

        self.frame2.grid_remove()
        self.frame1.grid(row=0, column=0)

        try:
            if self.name.get() == "Please enter your name":
                self.warning.configure(text = "Please enter your name")
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.warning.configure(text = "Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()

            elif self.age.get() == "":
                self.warning.configure(text = "Please enter a number")
                self.AgeEntry.delete(0, END)
            elif self.age.get() > 12:
                self.warning.configure(text = "You are too old to play this game!")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <= 0:
                self.warning.configure(text = "Please enter a number greater than 0")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <=7:
                self.warning.configure(text = "Oh No! You are too young to play this game!")

            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.screen2()

        except:
            self.warning.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()
        

    def screen2(self):
        global frame1
        global frame2
        
        frame1.grid_remove()
        


if __name__ == "__main__":
    root= Tk()
    frames = sciencequiz(root)
    root.title("Science Quiz v2")
    root.geometry("600x300+850+0")
    root.mainloop()