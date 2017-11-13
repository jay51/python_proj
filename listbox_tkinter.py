from tkinter import *

master = Tk()

group = LabelFrame(master, text="Group", padx=5, pady=5)
group.pack(padx=10, pady=10)
v= StringVar()
w = Entry(group,textvariable=v)
w.pack()

listbox = Listbox(master)
listbox.pack()

def add_d():
#get the data from the entry box and add it to the listbox
    box_input= v.get()
    listbox.insert(END, box_input)
#add this list to the listbox
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

def delete_d():
    option_selected = listbox.curselection()#this is to get the location of the selected item
    print(option_selected)#and this to print it
    # listbox.delete(option_selected)# uses item location to delete the item
    listbox.delete(ACTIVE)#uses the ACTIVE attrbute to locate the item selected and delete


#the is the same as the above founction "delete items from listbox" but in lambda form
# b = Button(master, text="Delete",
        #    command=lambda listbox=listbox: listbox.delete(ACTIVE)).pack()


#the tow buttons to delete and add
add = Button(master , text = "Add", command=add_d).pack()
delete = Button(master , text = "delete", command=delete_d).pack()


### the scrollbar info , it's still not working ###############
'''
scrollbar = Scrollbar(app , orient=VERTICAL)
listbox = Listbox(, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
'''

master.mainloop()
