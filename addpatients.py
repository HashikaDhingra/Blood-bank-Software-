from tkinter import *
import home
from tkinter import messagebox
from tkinter.ttk import Combobox
import db
import showpatients
from tkinter.font import Font



class addpatients:

    def addpatients(self):
         pname=self.userdata.get()
         pphone=self.phonedata.get()
         paddress=self.addressdata.get()
         pmed=self.issuedata.get()
         pdob=self.dobdata.get()
         pgen=self.genvar.get()
         pblood=self.userselectedcombo.get()
         data=(pname,pphone,paddress,pmed,pdob,pgen,pblood)
         if(db.insertProject(data)):
           messagebox.showinfo("Admin","Patient added")
           self.userdata.set("")
           self.phonedata.set("")
           self.addressdata.set("")
           self.issuedata.set("")
           self.dobdata.set("")
           self.genvar.set("")
           self.userselectedcombo.set("")
         else:
          messagebox.showerror("Admin","issue in adding")
   
    def home(self):
        self.root.destroy()
        home.home();
       
    def showpatients(self):
       self.root.destroy()
       showpatients.showpatients()

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Add Patients")

        self.frame=Frame(self.root,width=1000,height=500,bg="white")
        self.frame.place(x=0,y=0)

        self.bgimg=PhotoImage(file="PatientDetails.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=0,y=0,width=1000,height=500)
        
        homefont=Font(family="Times",size=13,weight="bold")
        self.label=Button(self.frame,text="Home",fg="#E93636",command=self.home,font=homefont,bg="white")
        self.label.place(x=30,y=35,height=40,width=120)

        medFont=Font(family="Times",size=15,weight="bold")
        self.label=Label(self.frame,text="Name:",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=130,y=195,height=45,width=150)
        self.userdata=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.userdata,font=medFont)
        self.userentry.place(x=275,y=200,height=35,width=180)


        self.label=Label(self.frame,text="Phone No. :",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=480,y=195,height=45,width=160)
        self.phonedata=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.phonedata,font=medFont)
        self.userentry.place(x=650,y=200,height=35,width=180)

        self.label=Label(self.frame,text="Address :",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=117,y=250,height=45,width=150)
        self.addressdata=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.addressdata ,font=medFont)
        self.userentry.place(x=275,y=253,height=35,width=180)

        self.label=Label(self.frame,text="Medical Issue:",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=473,y=250,height=45,width=160)
        self.issuedata=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.issuedata,font=medFont)
        self.userentry.place(x=650,y=253,height=35,width=180)

        self.label=Label(self.frame,text="DOB:",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=117,y=300,height=45,width=160)
        self.dobdata=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.dobdata,font=medFont)
        self.userentry.place(x=275,y=305,height=35,width=180)

        self.label=Label(self.frame,text="Gender:",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=473,y=300,height=45,width=120)
        self.genvar=StringVar()
        self.male=Radiobutton(self.frame,value="Male",text="Male",fg="#E93636",variable=self.genvar,font=medFont)
        self.male.select()
        self.male.place(x=650,y=306,height=35,width=100)
        self.female=Radiobutton(self.frame,value="Female",text="Female",fg="#E93636" ,variable=self.genvar,font=medFont)
        self.female.place(x=770,y=306,height=35,width=100)

        self.label=Label(self.frame,text="Blood Group:",fg="white",font=medFont,bg="#E93636")
        self.label.place(x=117,y=350,height=45,width=120)
        
        self.userselectedcombo = StringVar()
        self.bloodgroup = ["O+","O-","A+","B+","B-","A-","AB+","AB-"]
        
        self.bloodgrouplist = Combobox(self.frame,values=self.bloodgroup,textvariable=self.userselectedcombo,font=medFont)
        self.bloodgrouplist.place(x=273,y=355,width=183,height=35)
        self.bloodgrouplist.bind("<<ComboboxSelected>>")
        self.bloodgrouplist.set(self.bloodgroup[0])
        
        btnfont=Font(family="Times",size=12,weight="bold")

        self.addpatients=Button(self.frame,text="Add Patients", bg="pink",fg="#E93636",font=btnfont,command=self.addpatients)
        self.addpatients.place(x=380,y=420,width="140",height="50")

        self.showpatients=Button(self.frame,text="Show Patients", bg="white",fg="#E93636",font=btnfont,command=self.showpatients)
        self.showpatients.place(x=530,y=425,width="130",height="40")

        
       

       
        


        

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=addpatients();