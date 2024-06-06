from tkinter import *
import home
from tkinter import messagebox
import addpatients
import showpatients
import adddonors
import showdonors
import showblooddetails
import showbloodstock
import issueblood
import donateblood



class home:

    def addpatients(self):
        self.root.destroy()
        addpatients.addpatients()

    def showpatients(self):
        self.root.destroy()
        showpatients.showpatients()

    def  adddonors(self):
        self.root.destroy()
        adddonors.adddonors()

    def showdonors(self):
        self.root.destroy()
        showdonors.showdonors()

    def showbloodgroup(self):
        self.root.destroy()
        showblooddetails.showblooddetails()
    
    def showbloodstock(self):
        self.root.destroy()
        showbloodstock.showbloodstock()
    
    def issueblood(self):
        self.root.destroy()
        issueblood.issueblood()
    
    def donateblood(self):
        self.root.destroy()
        donateblood.donateblood()
    

    

    
    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Home")

        self.frame=Frame(self.root,width=1000,height=500,bg="blue")
        self.frame.place(x=0,y=0)

        self.bgimg=PhotoImage(file="homepage.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=0,y=0,width=1000,height=500)

        self.menubar=Menu(self.root)
        self.patient=Menu(self.menubar)
        self.menubar.add_cascade(label="Patient",menu=self.patient)
        self.patient.add_command(label="Add Patients",command=self.addpatients)
        self.patient.add_command(label="Show Patients",command=self.showpatients)

        self.Donor=Menu(self.menubar)
        self.menubar.add_cascade(label="Donor",menu=self.Donor)
        self.Donor.add_command(label="Add Donors",command=self.adddonors)
        self.Donor.add_command(label="Show Donors",command=self.showdonors)

        self.BloodGroup=Menu(self.menubar)
        self.menubar.add_cascade(label="Blood Group",menu=self.BloodGroup)
        self.BloodGroup.add_command(label="Show Blood Group",command=self.showbloodgroup)
        self.BloodGroup.add_command(label="Show Blood Stock",command=self.showbloodstock)
        
        self.Camps=Menu(self.menubar)
        self.menubar.add_cascade(label="Camps",menu=self.Camps)
        
        self.Camps.add_command(label="Donated Blood ",command=self.donateblood)
        self.Camps.add_command(label="Issued Blood",command=self.issueblood)

        self.root.config(menu=self.menubar)

        
       

        


        

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=home();