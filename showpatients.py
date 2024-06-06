from tkinter import *
import home
from tkinter import messagebox
from tkintertable import TableCanvas
import db
from tkinter.font import Font
from tkinter.ttk import Combobox



class showpatients:

    def fetchpatientdetail(self,data):

        self.data = {}
        res = db.selectbyPatientName(self.userselectedcombo.get())

        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel, data=self.data)
        self.tb.show()
        self.tb.redraw();

    def deletePatientsvianame(self):

        if (messagebox.askyesno("admin","Do you want to delete Yes or not?") ):
            if (db.deletePatientsviaName(self.userselectedcombo.get()) ):
                messagebox.showinfo("Admin", "Patient Deleted")
            else:
                messagebox.showinfo("Admin", "Issue in Delete")
    def updatePatientsvianame(self):

        if (messagebox.askyesno("admin","Do you want to update Yes or not?") ):
            if True:
                    self.data = {}
                    res = db.showProject()
                    for i in range(len(res)):
                        self.data[i] = res[i]
                    self.tb = TableCanvas(self.panel,data=self.data)
                    self.tb.show()
                    self.tb.redraw()
                    self.btn=Button(self.frame,text="Update Patients", bg="pink",fg="#E93636",command=self.updateindb)
                    self.btn.place(x=450,y=400,width="125",height="45")


    def showpatients(self):      
        self.data = {}
        res = db.showProject()
       
        for i in range(len(res)):
            self.data[i] = res[i]
        self.tb = TableCanvas(self.panel,data=self.data)
        self.tb.show()
        self.tb.redraw()

    def home(self):
        self.root.destroy()
        home.home();

        

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Show Patients")

       

        self.frame=Frame(self.root,width=1100,height=500,bg="#E93636")
        self.frame.place(x=0,y=0)

        self.frame2=Frame(self.root,width=565,height=65,bg="white")
        self.frame2.place(x=40,y=25)

        self.bgimg=PhotoImage(file="logo.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=880,y=20,width=120,height=75)

        medFont=Font(family="Times",size=11,weight="bold")

        self.label=Button(self.frame2,text="Home",fg="White",command=self.home,font=medFont,bg="#E93636")
        self.label.place(x=10,y=10,height=45,width=90)
        

        self.btn=Button(self.frame2,text="Show Patients", bg="pink",fg="#E93636",font=medFont,command=self.showpatients)
        self.btn.place(x=290,y=10,width="120",height="45")
         
        self.panel=PanedWindow(self.frame,bg="#E93636")
        self.panel.place(x=0,y=100,width=1000,height=300)

        self.userselectedcombo = StringVar()
        self.ptname = []
        self.data = db.showProject();
        for i in range(len(self.data)):
            self.ptname.append(self.data[i]['PatientName'])

        self.patientList = Combobox(self.frame2,values=self.ptname,textvariable=self.userselectedcombo)
        self.patientList.place(x=120,y=13,width=150,height=40)
        self.patientList.bind("<<ComboboxSelected>>",self.fetchpatientdetail)
        self.patientList.set(self.ptname[0])
       
        
        self.deletepatients=Button(self.frame2,text="Delete Patients", bg="pink",fg="#E93636",font=medFont,command=self.deletePatientsvianame)
        self.deletepatients.place(x=430,y="10",width="120",height="45")
        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=showpatients();