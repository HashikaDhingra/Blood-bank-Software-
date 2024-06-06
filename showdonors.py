from tkinter import *
import home
from tkinter import messagebox
from tkintertable import TableCanvas
import db
from tkinter.font import Font
from tkinter.ttk import Combobox


class showdonors:

    def showdonors(self):
        self.data = {}
        res = db.showdonorDetail()
      
        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel,data=self.data)
        self.tb.show()
        self.tb.redraw();

    def fetchdonordetail(self,data):

        self.data = {}
        res = db.selectbyDonorName(self.userselectedcombo.get())

        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel, data=self.data)
        self.tb.show()
        self.tb.redraw();

    def deletedonorsviaName(self):

        if (messagebox.askyesno("admin","Do you want to delete Yes or not?") ):
            if (db.deletedonorsviaName(self.userselectedcombo.get()) ):
                messagebox.showinfo("Admin", "Donor Deleted")
            else:
                messagebox.showinfo("Admin", "Issue in Delete")

   
    def home(self):
        self.root.destroy()
        home.home();
        

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Show Donors")

        self.frame=Frame(self.root,width=1000,height=500,bg="#E93636")
        self.frame.place(x=0,y=0)

        self.frame2=Frame(self.root,width=565,height=65,bg="white")
        self.frame2.place(x=40,y=25)

        self.bgimg=PhotoImage(file="logo.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=880,y=20,width=120,height=75)

        medFont=Font(family="Times",size=11,weight="bold")

        self.btn=Button(self.frame2,text="Show Donors", bg="pink",fg="#E93636",font=medFont,command=self.showdonors)
        self.btn.place(x=290,y=10,width="120",height="45")

        self.label=Button(self.frame2,text="Home",fg="white",command=self.home,font=medFont,bg="#E93636")
        self.label.place(x=10,y=10,height=45,width=90)

       
       
        self.panel=PanedWindow(self.frame,bg="#E93636")
        self.panel.place(x=0,y=120,width=1000,height=400)

        self.userselectedcombo = StringVar()
        self.doname = []
        self.data = db.showdonorDetail();
        for i in range(len(self.data)):
            self.doname.append(self.data[i]['dname'])

        self.DonorList = Combobox(self.frame2,values=self.doname,textvariable=self.userselectedcombo)
        self.DonorList.place(x=120,y=13,width=150,height=40)
        self.DonorList.bind("<<ComboboxSelected>>",self.fetchdonordetail)
        self.DonorList.set(self.doname[0])

        self.deletepatients=Button(self.frame2,text="Delete Donors", bg="pink",fg="#E93636",font=medFont,command=self.deletedonorsviaName)
        self.deletepatients.place(x=430,y="10",width="120",height="45")
       
        
       

       
        


        

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=showdonors();