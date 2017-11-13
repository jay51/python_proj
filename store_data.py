from tkinter import *
from datetime import datetime


app = Tk()

app. geometry("300x300")


v = StringVar()
E = Entry(app , textvariable=v ).pack()
###############################


def save_d():
    now = datetime.now()
    print("%d/%d/%d , %d:%d" %(now.year,now.month,now.day,now.hour,now.minute))
    d = v.get()
    with open('seales_data', 'a') as f:#OPEN a file and store the data from the entry box inside the file
        data = f.write(d+" %d/%d/%d , %d:%d" %(now.year,now.month,now.day,now.hour,now.minute)+"\n")
    Label(app, text ="seccefuly saved").place(x=5,y=5)


B = Button(app, text="save",command=save_d).pack()







app.mainloop()
