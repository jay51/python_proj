from tkinter import *

class kinter:
    def __init__(self, main):
        frame=Frame(main, width= 300 , height= 300)
        frame.pack()
        self.cleck_1 = Button(frame , text= "greatings" , command = self.print_message)
        self.cleck_1.pack()

    def print_message(self):
        print("the print message is working")
















root=Tk()

user_1=kinter(root)


root.mainloop()
