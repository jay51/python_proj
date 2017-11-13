from tkinter import *
from tkinter import ttk


root = Tk()
# the label object can take more attrbute like "bg"=back ground color
#and  "fg" for the text color
label_1 = Label(root, text="top", bg = "black", fg = "blue")
label_2 = Label(root, text="acrose the x line ",bg="black" , fg= "blue")
label_3 = Label(root , text = "side all the way down " , bg="green" )
#the pack method can have more attrbute like the "fill" to indecute where
#where to fill the screen and "side " to put the content on a side
#"fill" can take only one of the two attrbutes (x or y)
# "side" can take one of the attrbutes (left, top...)
label_1.pack()
label_2.pack(fill="x")
label_3.pack(side="left", fill="y")


# this is the frame that is  a small space where contet can go
#i made two frames "top"and "bottom" to put contect in
#and least we have to pack it to display it on screen
top_frame= Frame(root,width=300,height=300)
top_frame.pack(side="top")
bottum_frame=Frame(root)
bottum_frame.pack(side="bottom")
#create two buttons on the two frames i have created previcely "top"and"bottm"
#one button on top frame and one on buttom frame
button_1= Button(top_frame,text="zero", fg="blue")
button_1.pack(side="right")

button_1= Button(bottum_frame,text="one", fg="blue")
button_1.pack(side="left")



root.mainloop()


################################################################################



root=Tk()
#this is a new window,it will open right after i close the first one

#a simple function to see if the entry is working

def hello_world():
    label=Label(root,text=entry_1.get())
    label.grid()





label_1 = Label(root, text="Name:")
label_2 = Label(root, text="password:")


#this is the same code as the first window but we packing it on the screen with
# grid method
label_2.grid(row="1")
label_1.grid(row="0")
# this is for an entery box to put data in

entry_1=Entry(root,)
entry_2=Entry(root,)
# and to pack them with the grid method
entry_1.grid(row="0",column="1")
entry_2.grid(row="1",column="1")

#amd this is to make a check box

check_box = Checkbutton(root, text="stay sigined in !")
#and the attrbute inside grid "columnspan" is to connect to colunms
#and palece the boutton in the midle of the two

check_box.grid(columnspan="2")

#and now im going to add a button and link that button to a simple function
def print_name1():
    print("hello world")

cleck_1 = Button(root , text= "greatings" , command = print_name1)
cleck_1.grid()

# this is another way to link a button
# the function must take an event attrbute
def print_name(event):
    print("neno")

button_1 = Button(root, text = " name " )
#the bind method take the code for the button and the function name
button_1.bind("<Button-1>",print_name)
button_1.grid()


root.mainloop()

###########################################################################














root_12= Tk()

holder = StringVar()
e = Entry(root_12, textvariable=holder)
e.pack()
label = Text(root_12,width=20,height=10, state = "disabled").pack()
def get_tx():
    print(e.get())


b_1 = Button(root_12, text= "get text", command=get_tx).pack()













root_12.mainloop()
