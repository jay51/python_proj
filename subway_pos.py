from tkinter import *



class emp_1:


#the lists counten the num of sandwatchies sold and the price of each
    sandwatchies={"BMT" : [0,6.40],
  "roastbeaf" : [0,6.79],
  "BLT" :[0, 5.49],
  "steak" : [0,7.10],
  "turky" :[0, 6.25] }

#the list counten how much food we have and the price for that perteclier item.

    food={"olive":[5,1.5],
    "bread":[100,1.5] ,
    "onions": [5,1.5],
    "bell papers":[5,1.5],
    "cucmber":[5,1.5],
    "spench":[5,1.5],
    "tomato":[5,2],
    "lettce": [5,1.5],
    "banana papers":[5,1.5]}

    seales = 0
    num_of_emp = 0
    class_pay = 8
############################################################################
#the gui starts here .

    def __init__(self, fullname,gui):
        self.name=fullname
        self.seales=0
        self.gui = gui
        #i need to make a better frame than this one  and show all the data in that frame and also use
        #insert to show the data so i can use "end" to dellet the data one inserting a new one .
###################     THESE ARE THE FRAMES THAT ARE GOING BE USED##############################
        self.gui.geometry("1000x600")
###################### THIS IS THE ONE IN BLUE TO THE LEFT SIDE IN THE CORNER #############################
        self.frame_0=Frame(self.gui , bd=1 ,bg = "blue" ,width = 150 , height = 100 ,relief = "sunken").grid(row = 2, column = 1)
#############   THIS IS THE BIG ONE THAT PUSH THEM TO THE SIDE   #########################
        self.diff_frame = Frame(self.gui, bg = "orange", width =400,height=100 ).grid(row=4,column=2)
        #################  THESE ARE THE MAIN ONES TO SHOW THE DATA    ##############
        self.frame_1=Frame(self.gui ,bg = "yellow" ,width = 300 , height = 27).grid(row = 2,column = 3,ipady="27px" )#the yellow frame
        self.farme_2=Frame(self.gui, bg = "yellow",width = 300, height = 27).grid(row=3 ,column = 3,ipady="27px")
        self.farme_3=Frame(self.gui, bg = "yellow",width = 300, height = 27).grid(row=4 ,column = 3 ,ipady="27px")
        self.farme_4=Frame(self.gui, bg = "yellow",width = 300, height = 27).grid(row=5 ,column = 3 ,ipady="27px")
        self.farme_6=Frame(self.gui, bg = "yellow",width = 300, height = 27).grid(row=6 ,column = 3,ipady="27px" )
##################### the subway seales options #######################
        BMT = Button(self.frame_1 ,  text="BMT", fg ="black", bg = "green", command= None ).grid(row=1)
        ROASTBEAF = Button(self.frame_2 ,  text="ROASTBEAF", fg ="black", bg = "green", command= None ).grid(row=2)
        BLT  = Button(self.frame_3,  text="BLT", fg ="black", bg = "green", command= None ).grid(row=3)
        STEAK = Button(self.frame_4 ,  text="STEAK", fg ="black", bg = "green", command= None ).grid(row=4)
        TURKY= Button(self.farme_5 ,  text="TURKY", fg ="black", bg = "green", command= None ).grid(row=5)















###################     ALL THE FRAMES ARE GOING BE ABOVE ##############################
        self.label_0 = Label(self.frame_0 , text = "this is the farme -->").grid(row = 2,column=1)

        self.holder = StringVar()# To hold the data of the entry below.

        self.e = Entry(self.gui, textvariable =self.holder).grid(row=8,column=3)

        self.button_1 = Button(self.frame_0, text = "Subway Pos", bg = "green" , fg = "yellow", font = "Times 16 bold", command =self.display_sandwatchies).grid(row=9,column=3)#button
        self.L_1 = Label(self.gui, text="Enter a user to check the seales" , font="5").grid(row=10,column=3)
        self.gui.title("Welcome To Subway")#the title on top of the window.
        self.gui.configure(background = "green")#background color of entire window


###########################################################################

        self.sandwatchies = {"BMT" : [0,6.40],
  "roastbeaf" : [0,6.79],
  "BLT" :[0, 5.49],
  "steak" : [0,7.10],
  "turky" :[0, 6.25] }
        emp_1.num_of_emp +=1

# find the hors worked
    def hours_worked(self,start, end ):
        self.hours = start - end
        return(self.hours)
#find the pay
    def pay(self,hours=0):
        self.pay = self.hours * emp_1.class_pay
        return(self.pay)
# a method to count the cost of all sandwatchies each employ sold
# and count the total money_of_day
#and type of sandwatchies sold by all employes
#and the type  of sandwatchies each employ sold
#and count howmuch bread left
#and count the vagies left in the store

    def make_sale(self,number_of_sandwatchies,name_of):
        self.seales += (number_of_sandwatchies * self.sandwatchies[name_of][1])
        emp_1.seales += self.seales

        self.sandwatchies[name_of][0] += number_of_sandwatchies
        emp_1.sandwatchies[name_of][0] +=number_of_sandwatchies

        for item in emp_1.food:
            if item is "bread":
                emp_1.food[item][0] -= number_of_sandwatchies
            else: emp_1.food[item][0] -=0.5 * number_of_sandwatchies

        print("sale was made succefly!")


    def display_sandwatchies (self):
        row=2
        #assign the input to self.data
        self.data = str(self.holder.get())
        #if the input is wqua
        if self.data == "SUBWAY"  or self.data == "Subway".lower() :
            label=Label(self.gui,text = "subway sales:" + str(emp_1.seales),font="Arial 16 underline").grid(row= 2, column=2)

            for sandwatch in emp_1.sandwatchies:
                lab = ("%s :"%(sandwatch)," , ".join (map(str,emp_1.sandwatchies[sandwatch]))+ "\n")
                label_1 = Label(self.gui , text = lab ,bg="lightgreen",fg="red", font="Times 20 bold" ).grid(row = row, column= 3)
                row +=1
        else:
            self.L_1.config(text = "this is NOT a vaild answer!")
            print("this is not a valid answer!")




app=Tk()

me = emp_1("neno jay",app)





app.mainloop()
