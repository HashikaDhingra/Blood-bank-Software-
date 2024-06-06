from tkinter import *
import home
from tkinter import messagebox
from tkinter.font import Font
from tkinter.ttk import Combobox
import showdonors
import db

class adddonors:
    def adddonors(self):

      dname=self.Donorname.get()
      dphone=self.donorphno.get()
      daddress=self.donoraddress.get()
      dmed=self.pastmedical.get()
      ddob=self.donordob.get()
      dgen=self.donorgen.get()
      dblood=self.userselectedcombo.get()
      data=(dname,dphone,daddress,dmed,ddob,dgen,dblood)
      if(db.donorProject(data)):
           messagebox.showinfo("Admin","Donor added")
           self.Donorname.set("")
           self.donorphno.set("")
           self.donoraddress.set("")
           self.pastmedical.set("")
           self.donordob.set("")
           self.donorgen.set("")
           self.userselectedcombo.set("")
      else:
          messagebox.showerror("Admin","issue in adding")

    def home(self):
            self.root.destroy()
            home.home();
       
    def showdonors(self):
            self.root.destroy()
            showdonors.showdonors()
         

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Add Donors")

        self.frame=Frame(self.root,width=1000,height=500,bg="blue")
        self.frame.place(x=0,y=0)

        self.bgimg=PhotoImage(file="Donor_Details.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=0,y=0,width=1000,height=500)

        homefont=Font(family="Times",size=13,weight="bold")
        self.label=Button(self.frame,text="Home",fg="#E93636",command=self.home,font=homefont,bg="white")
        self.label.place(x=30,y=35,height=40,width=120)

        medFont=Font(family="Times",size=15,weight="bold")

        self.label=Label(self.frame,text="Name:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=130,y=195,height=45,width=150)
        self.Donorname=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.Donorname,font=medFont)
        self.userentry.place(x=275,y=200,height=35,width=180)

        self.label=Label(self.frame,text="Phone number:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=480,y=195,height=45,width=160)
        self.donorphno=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.donorphno,font=medFont)
        self.userentry.place(x=650,y=200,height=35,width=180)

        self.label=Label(self.frame,text="Address:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=117,y=250,height=45,width=150)
        self.donoraddress=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.donoraddress ,font=medFont)
        self.userentry.place(x=275,y=253,height=35,width=180)

        self.label=Label(self.frame,text="Medical Issue:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=473,y=250,height=45,width=160)
        self.pastmedical=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.pastmedical,font=medFont)
        self.userentry.place(x=650,y=253,height=35,width=180)

        self.label=Label(self.frame,text="DOB:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=117,y=300,height=45,width=160)
        self.donordob=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.donordob,font=medFont)
        self.userentry.place(x=275,y=305,height=35,width=180)
 
        self.label=Label(self.frame,text="Gender:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=473,y=300,height=45,width=150)
        self.donorgen=StringVar()
        self.male=Radiobutton(self.frame,value="Male",text="Male",fg="#E93636",variable=self.donorgen,font=medFont)
        self.male.select()
        self.male.place(x=650,y=306,height=35,width=100)
        self.female=Radiobutton(self.frame,value="Female",text="Female",fg="#E93636" ,variable=self.donorgen,font=medFont)
        self.female.place(x=770,y=306,height=35,width=100)

        self.label=Label(self.frame,text="Blood Group:",fg="white",bg="#E93636",font=medFont)
        self.label.place(x=117,y=350,height=45,width=120)
        
        self.userselectedcombo = StringVar()
        self.bloodgroup = ["O+","O-","A+","B+","B-","A-","AB+","AB-"]
        
        self.bloodgrouplist = Combobox(self.frame,values=self.bloodgroup,textvariable=self.userselectedcombo,font=medFont)
        self.bloodgrouplist.place(x=273,y=355,width=183,height=35)
        self.bloodgrouplist.bind("<<ComboboxSelected>>")
        self.bloodgrouplist.set(self.bloodgroup[0])

        btnfont=Font(family="Times",size=12,weight="bold")

        self.adddonors=Button(self.frame,text="Add Donors", bg="pink",fg="#E93636",font=btnfont,command=self.adddonors)
        self.adddonors.place(x=380,y=420,width="140",height="50")

        self.showdonors=Button(self.frame,text="Show Donors", bg="white",fg="#E93636",font=btnfont,command=self.showdonors)
        self.showdonors.place(x=530,y=425,width="130",height="40")

        

       

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=adddonors();