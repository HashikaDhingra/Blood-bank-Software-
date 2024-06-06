from tkinter import *
import home
from tkinter import messagebox
import db
from tkintertable import TableCanvas
from tkinter.font import Font


class showbloodstock:

    def showstock(self):
        self.data = {}
        res = db.showbloodstock()
       
        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel,data=self.data)
        self.tb.show()
        self.tb.redraw();

    def home(self):
        self.root.destroy()
        home.home();    

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Show Blood Stock")

        self.frame=Frame(self.root,width=1000,height=500,bg="#E93636")
        self.frame.place(x=0,y=0)

        self.bgimg=PhotoImage(file="logo.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=880,y=20,width=120,height=75)

        medFont=Font(family="Times",size=13,weight="bold")

        self.btn=Button(self.frame,text="Show Stocks", bg="pink",fg="#E93636",font =medFont,command=self.showstock)
        self.btn.place(x=220,y=27,width="150",height="50")
       
        self.panel=PanedWindow(self.frame,bg="#E93636")
        self.panel.place(x=0,y=140,width=1000,height=400)

        
        

        self.label=Button(self.frame,text="Home",fg="Red",command=self.home,font=medFont,bg="white")
        self.label.place(x=100,y=30,height=45,width=100)
       
        


        

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=showbloodstock();