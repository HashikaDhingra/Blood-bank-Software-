from tkinter import *
import home
from tkinter import messagebox
from tkinter.font import Font


class login:

    def submit(self):
        a=self.userdata.get()
        b=self.passdata.get()
        if(a=="donatories" and b=="123"):
            messagebox.showinfo("admin","login succesful")
            self.root.destroy()
            home.home();
        else:
           messagebox.showerror("admin","wrong username and password")
      
        

    def __init__(self):  
        self.root=Tk()
        self.root.geometry("1000x500+150+150")
        self.root.title("Blood Bank Management System")

        self.frame=Frame(self.root,width=1000,height=500,bg="pink")
        self.frame.place(x=0,y=0)

        self.bgimg=PhotoImage(file="loginpage.png")
        self.imgplace=Label(self.frame,image=self.bgimg)
        self.imgplace.place(x=0,y=0,width=1000,height=500)

        bigFont=Font(family="Times",size=15,weight="bold")
        
        self.label=Label(self.frame,text="Email",fg="white",font=bigFont,bg="#E93636")
        self.label.place(x=100,y=195,height=45,width=120)

        self.userdata=StringVar()
        self.userentry=Entry(self.frame,textvariable=self.userdata)
        self.userentry.place(x=230,y=200,height=40,width=250)
        
        
        self.label=Label(self.frame,text="Password",fg="white",bg="#E93636",font=bigFont)
        self.label.place(x=100,y=255,height=45,width=120)

        self.passdata=StringVar()
        self.userentry=Entry(self.frame,show="*",textvariable=self.passdata)
        self.userentry.place(x=230,y=260,height=40,width=250)

        medFont=Font(family="Times",size=13,weight="bold")
       

        self.btn=Button(self.frame,text="Login", bg="pink",fg="#E93636",font=medFont,command=self.submit)
        self.btn.place(x=120,y=325,width="360",height="50")
        

        


        

        
        
        self.root.mainloop();



if __name__=="__main__":    
    x=login();