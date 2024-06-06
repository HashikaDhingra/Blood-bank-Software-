from tkinter import *
import home
from tkinter import messagebox
from tkinter.font import Font
from tkintertable import TableCanvas
import db

class showblooddetails:

    

    def showInMobile(self,res):
        self.data = {}
        if(len(res)>0):
            for i in range(len(res)):
                self.data[i] = res[i]
            self.tb = TableCanvas(self.panel,data=self.data)
            self.tb.show()
            self.tb.redraw();
        else:
            messagebox.showerror("admin","blood group not found")
       
    def buttonop(self): 
        res = db.fetchdetailsbybloodgroup('o+')
        self.showInMobile(res)
       
    def buttonon(self): 
        res = db.fetchdetailsbybloodgroup('o-')
        self.showInMobile(res)
       
    def buttonap(self): 
        res = db.fetchdetailsbybloodgroup('a+')
        self.showInMobile(res)
    def buttonan(self): 
        res = db.fetchdetailsbybloodgroup('a-')
        self.showInMobile(res)
    def buttonbp(self): 
        res = db.fetchdetailsbybloodgroup('b+')
        self.showInMobile(res)
    def buttonbn(self): 
        res = db.fetchdetailsbybloodgroup('b-')
        self.showInMobile(res)
    def buttonabp(self): 
        res = db.fetchdetailsbybloodgroup('ab+')
        self.showInMobile(res)
    def buttonabn(self): 
        res = db.fetchdetailsbybloodgroup('ab-')
        self.showInMobile(res)

    def home(self):
        self.root.destroy()
        home.home();

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Show Blood Group Details")

        self.frame=Frame(self.root,width=1000,height=500,bg="#E93636")
        self.frame.place(x=0,y=0)

        self.frame2=Frame(self.root,width=650,height=65,bg="white")
        self.frame2.place(x=30,y=25)

        self.bgimg=PhotoImage(file="logo.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=880,y=20,width=120,height=75)


        medFont=Font(family="Times",size=13,weight="bold")

        self.label=Button(self.frame2,text="Home",fg="white",command=self.home,font=medFont,bg="#E93636")
        self.label.place(x=15,y=10,height=45,width=100)

        self.btn=Button(self.frame2,text="O+",fg="Red",font=medFont,command=self.buttonop,bg="pink")
        self.btn.place(x=130,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="O-",fg="Red",font=medFont,command=self.buttonon,bg="pink")
        self.btn.place(x=195,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="A+",fg="Red",font=medFont,command=self.buttonap,bg="pink")
        self.btn.place(x=260,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="A-",fg="Red",font=medFont,command=self.buttonan,bg="pink")
        self.btn.place(x=325,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="B+",fg="Red",font=medFont,command=self.buttonbp,bg="pink")
        self.btn.place(x=390,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="B-",fg="Red",font=medFont,command=self.buttonbn,bg="pink")
        self.btn.place(x=455,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="AB+",fg="Red",font=medFont,command=self.buttonabp,bg="pink")
        self.btn.place(x=520,y=10,width="50",height="45")

        self.btn=Button(self.frame2,text="AB-",fg="Red",font=medFont,command=self.buttonabn,bg="pink")
        self.btn.place(x=585,y=10,width="50",height="45")

        self.panel=PanedWindow(self.frame,bg="#E93636")
        self.panel.place(x=0,y=140,width=1000,height=400)


       
       
        


        

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=showblooddetails();