from tkinter import *
import home
import db
from tkintertable import TableCanvas
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.font import Font


class donateblood:

    def home(self):
        self.root.destroy()
        home.home();
    
    def dblood(self):
        comGrp = self.bloodList.get()
        comQty = self.qty.get()
        q=int(comQty)
        # print(comGrp,type(comQty))
        dbQty=db.showqty(comGrp)
        # print(dbQty)
        Qty=dbQty[0]['qty']
        Qty=Qty+q
        db.updateQty(comGrp,Qty)
        messagebox.showinfo("Admin","Updated Stock")

    def fetchbloodgroup(self,data):
        self.data = {}
        res = db.selectbybloodgroup(self.userselectedcombo.get())

        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel, data=self.data)
        self.tb.show()
        self.tb.redraw();

    def fetchdonordetail(self,data):

        self.data = {}
        res = db.selectbyPatientName(self.userselectedcombo.get())

        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel, data=self.data)
        self.tb.show()
        self.tb.redraw();
          
          


    
        

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Donate Blood")

        self.frame=Frame(self.root,width=1000,height=500,bg="#E93636")
        self.frame.place(x=0,y=0)

        self.bgimg=PhotoImage(file="DonateBlood.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=0,y=0,width=1000,height=500)
        
        homefont=Font(family="Times",size=13,weight="bold")
        self.label=Button(self.frame,text="Home",fg="#E93636",command=self.home,font=homefont,bg="white")
        self.label.place(x=30,y=35,height=40,width=120)
       
        medFont=Font(family="Times",size=15,weight="bold")
        self.donorname=Label(self.frame,text="Donor Name",fg="white",bg="#E93636",font=medFont)
        self.donorname.place(x=300,y=150,width=150,height=100)

        
        self.userselectedcombo = StringVar()
        self.doname = []
        self.data = db.showdonorDetail();
        for i in range(len(self.data)):
            self.doname.append(self.data[i]['dname'])

        self.DonorList = Combobox(self.frame,values=self.doname,textvariable=self.userselectedcombo)
        self.DonorList.place(x=450,y=183,width=190,height=35)
        self.DonorList.bind("<<ComboboxSelected>>",self.fetchdonordetail)
        self.DonorList.set(self.doname[0])
        
        medFont=Font(family="Times",size=15,weight="bold")
        self.bloodgroup=Label(self.frame,text="Donor Blood Group",fg="white",bg="#E93636",font=medFont)
        self.bloodgroup.place(x=250,y=240,height=50,width=200)


        self.userselectedcombo = StringVar()
        self.bgname = []
        self.data = db.showbloodgroup();
        for i in range(len(self.data)):
            self.bgname.append(self.data[i]['bgroup'])

        self.bloodList = Combobox(self.frame,values=self.bgname,textvariable=self.userselectedcombo)
        self.bloodList.place(x=450,y=245,width=190,height=35)
        self.bloodList.bind("<<ComboboxSelected>>",self.fetchbloodgroup)
        
        medFont=Font(family="Times",size=15,weight="bold")
        self.qtylabel=Label(self.frame,text="Quantity",fg="white",bg="#E93636",font=medFont)
        self.qtylabel.place(x=300,y=300,height=50,width=150)


        self.quantity=["1","2","3","4","5","6","7","8","9","Custom"];
        self.qty = Combobox(self.frame,values=self.quantity)
        self.qty.place(x=450,y=310,width=190,height=35)

        btnfont=Font(family="Times",size=12,weight="bold")
        self.btn=Button(self.frame,text="Submit", bg="pink",fg="#E93636",command=self.dblood,font=btnfont)
        self.btn.place(x=410,y=370,width="150",height="40")
        
        self.root.mainloop();



if __name__=="__main__":    
    x=donateblood();
    
        
