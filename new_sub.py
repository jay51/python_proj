from tkinter import *
from datetime import datetime


##############this is the password window #################

password = Tk()

password.geometry("300x100")

user_holder = StringVar()
pass_holder = StringVar()
username = Entry(password , textvariable = user_holder).pack()
pass_word = Entry(password , textvariable = pass_holder).pack()

name = Label(password,text="user name" ).place(x=0,y=0)
keywrod = Label(password,text="password" ).place(x=0,y=20)




######################## the program ###################################

def the_hole_green_app():

    seales = 0


    food={"olive":[5,1.5],
    "bread":[100,1.5] ,
    "onions": [5,1.5],
    "bell papers":[5,1.5],
    "cucmber":[5,1.5],
    "spench":[5,1.5],
    "tomato":[5,2],
    "lettce": [5,1.5],
    "banana papers":[5,1.5]}


    sandwatchies={"BMT" : [0,6.40],
    "roastbeaf" : [0,6.79],
    "BLT" :[0, 5.49],
    "steak" : [0,7.10],
    "turky" :[0, 6.25] }




    app = Tk()


    # window size
    app.geometry("1000x600")
    app.title("SUBWAY")
    app.configure( background = "green")


    is_working = False

    ##################### the function to the checkboxes below ###################
    time =datetime.now()

    def make_sale():
        s_type = v.get()
        global seales

        if is_working == True:#to check to see if there's an emploey clocked in
            if s_type in sandwatchies:
                seales += ( 1 * sandwatchies[s_type][1])
                sandwatchies[s_type][0] += 1
                for item in food:
                    if item == "bread":
                            food[item][0] -= 1
                    else: food[item][0] -=0.5 * 1
            else:return(None)
            print("sale was made succefly!")
            print(seales)

        else:
            print("someone got clock in!")
            return(None)

        time =datetime.now()
        # this part is to save the data and the time
        with open('seales_data', 'a') as f:
            data = f.write("seccefuly saved\n")
            data = f.write(s_type+" %d/%d/%d , %d:%d" %(time.year,time.month,time.day,time.hour,time.minute)+"\n")
            data = f.write("seales:%d" % seales)
    ##################### a checkbox ##################
    v = StringVar()

    checkbox = Checkbutton(app ,bg = "green", text = "" , variable = v,onvalue = "roastbeaf",  command = make_sale ).place(x=0,y=20)
    checkbox1 = Checkbutton(app ,bg = "green", text = "" , variable = v, onvalue = "BLT",  command = make_sale ).place(x=0,y=50)
    checkbox2 = Checkbutton(app ,bg = "green", text = "" , variable = v, onvalue = "steak",  command = make_sale ).place(x=0,y=80)
    checkbox3 = Checkbutton(app ,bg = "green", text = "" , variable = v, onvalue = "turky",  command = make_sale ).place(x=0,y=110)
    checkbox3 = Checkbutton(app ,bg = "green", text = "" , variable = v, onvalue = "BMT",  command = make_sale ).place(x=0,y=140)
    ###########################################################################



    ###################### the frames for the sandwatchies data  ###############

    frame_1=Frame(app , bg = "yellow" , width = 350 , height = 70).place(x=400, y=50)
    frame_2=Frame(app , bg = "yellow" , width = 350 , height = 70).place(x=400, y=100)
    frame_3=Frame(app , bg = "yellow" , width = 350 , height = 70).place(x=400, y=150)
    frame_4=Frame(app , bg = "yellow" , width = 350 , height = 70).place(x=400, y=200)
    frame_5=Frame(app , bg = "yellow" , width = 350 , height = 70).place(x=400, y=250)

    top_frame=Frame(app , bg = "blue", height = 10).pack(side="top" , fill="x")




    ########################## the listbox is going be in here with all it's functions and buttons #######################################



    label_frame = LabelFrame(app , text="emploey", padx=5, pady=5)
    label_frame.place(x=850,y=30)

    #entry box and string holder_2
    holder_2= StringVar()
    box_2 = Entry(label_frame , textvariable=holder_2)
    box_2.pack(side="right")
    #listbox and scrollbar
    # scrollbar = Scrollbar(app , orient=VERTICAL)
    listbox = Listbox(app, width=40)#yscrollcommand=scrollbar.set
    # scrollbar.config(command=listbox.yview)
    # scrollbar.pack(side=RIGHT, fill=Y)
    listbox.place(x=790,y=90)
    box_2.insert(END,"Name")#this is how u put string into any box that eccept text

    # this dic to check if the user is clocked in or out
    if_repeted={}
    def add_selected():
        global is_working
    #get the data from the entry box and add it to the listbox
        box_input= holder_2.get()
        #if emphty string do this
        if box_input == "":
            print("no string or integer. do nothing")
        #if string is in the dic , means the user is clocked in for so he is trying to clockout
        elif box_input in if_repeted:
            print("it's already there!/clocked out")
            listbox.insert(END,box_input,"clocked out   %d/%d/%d , %d : %d" %(time.year,time.month,time.day,time.hour,time.minute))
            del if_repeted[box_input]
            #this is to save the data for now
            with open('seales_data', 'a') as f:
                data = f.write(box_input+" clockedout "+"  %d/%d/%d , %d:%d" %(time.year,time.month,time.day,time.hour,time.minute)+"\n")

        #if the user is not clocked in clock him in
        else:

            listbox.insert(END, box_input+"             %d/%d/%d , %d : %d" %(time.year,time.month,time.day,time.hour,time.minute))
            if_repeted[box_input]=box_input

            is_working = True # to let me know that a worker is clockedin

            with open('seales_data', 'a') as f:
                data = f.write(box_input+" clockedin "+ "  %d/%d/%d , %d:%d" %(time.year,time.month,time.day,time.hour,time.minute)+"\n")

    def delete_selected():

        listbox.delete(ACTIVE)#uses the ACTIVE attrbute to locate the item selected and delete methode to delete it


    #the tow buttons to delete and add
    add = Button(app , text = "clockin/out", command=add_selected).place(x=920,y=260)
    delete = Button(app , text = "delete", command=delete_selected).place(x=870,y=260)


    #######################################################################################



    ############# the text area is going be here ##########################################p

    feedback_box = Text(app, state="normal",width=40, height=10).place(x=720,y=350)

    # feedback_box.insert(END,"would you like to helps us by leaving us your feedback !")









    ############ the buttons for the sandwatchies ###############################
    ROASTBEAF = Button(app , text="ROASTBEAF", fg ="black", cursor = "exchange",bg = "green", command= None ).place(x=20,y=20)
    BLT  = Button(app , text="BLT", fg ="black", bg = "green", command= None ).place(x=20,y=50)
    STEAK = Button(app ,  text="STEAK", fg ="black", bg = "green", command= None ).place(x=20,y=80)
    TURKY= Button(app , text="TURKY", fg ="black", bg = "green", command= None ).place(x=20,y=110)
    BMT = Button(app , text="BMT", fg ="black", bg = "green", command= None ).place(x=20,y=140)


    ################## HERE will be all the labels ##########################
    worrning = Label(app , text = "Entry an object" , bg = "green", font="Times 14 bold").place(x=400,y=320)





    ################ the entry box and it's value holder ################
    holder = StringVar()# To hold the data of the entry below.
    box = Entry(app , textvariable = holder , show="*").place(x=400, y=300)# the show to show *** insted of the password



    ################## the display function ####################
    def display_sandwatchies():

        y_axis = 50
        #assign the input to self.data
        entry = holder.get()
        #if the input is wqua
        if entry == "SUBWAY"  or entry == "Subway".lower() :
            text = "WELCOME TO SUBWAY!"
            label=Label(app , text = "subway sales: %d " % (seales) , font="Arial 16 underline").place(x=220,y=55)

            for sandwatch in sandwatchies :
                lab = ("%s :"%(sandwatch)," , ".join (map(str,sandwatchies[sandwatch]))+ "\n")
                label_1 = Label(app , text = lab ,bg="lightgreen",fg="red", font="Times 16 bold" ).place(x=400,y=y_axis)
                y_axis +=50
        else:
            text= "NOT a valid answer"

        worrning = Label(app , text = text , bg = "green", font="Times 14 bold").place(x=400,y=320)


    ######################## the SUBWAY butoon  belongs to the function above ###################################
    show_button = Button(app , text = "SUBWAY" , bg = "green" , command = display_sandwatchies).place(x=400,y=350)







    app.mainloop()

#############################################################


def if_password_true():
    if user_holder.get() == "neno":
        print("yes")
        password.quit()
        the_hole_green_app()
    else:print("no")

sign_in = Button(password , text ="sign in", command =if_password_true).pack(side="bottom")


# the password loop "not the main program loop"
password.mainloop()
