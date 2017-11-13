from tkinter import *

class Subway:
    def __init__(self, tk):
        self.tk=tk
        self.tk.geometry("600x500+250+200")
        #this is the window frame where the content is going to show up
        self.frame = Frame(self.tk, height = 200, width = 200, bg= "blue").grid(column=1,pady = "20px")
        #this is the lable
        self.label = Label(self.tk, text = "the login page!" ).grid(row=1 , column=3)
        #this makes a button
        self.button = Button(self.tk, text = "cleck me!" , command = self.show_text).grid()
        self.text = Text(self.tk, width =20, height=10).grid(row=1,column=1)

        #this is a string holder to hold the entry data
        self.data = StringVar()
        #this is the entry box to take data from user .
        self.entry = Entry(self.frame,textvariable = self.data).grid()
        self.top_frame=Frame(tk,bg="blue").grid(row=1)
    

############## BUTTONS ON THE SIDE OF THE BLUE SCREEN ################
        self.B_1 = Button(self.frame,text = "BMT", command=self.click).grid()

    def click (self):
        message="hello there !"
        self.text.insert(0.0,message)
        self.label = Label(self.tk, text="NOT LOGGED IN").grid(row=1, column=3)












    def show_text(self):
        data = self.data.get()
        print(data)
        print(type(data))
        self.label.config(text= "yes")



app = Tk()
pos = Subway(app)
app.mainloop()
