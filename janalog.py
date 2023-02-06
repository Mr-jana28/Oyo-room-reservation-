from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from janawel import welcome



class login:
    def __init__(self):
        self.win=Tk()
        self.win.title('hello')
        self.win.geometry('2000x900')
        self.win.config(bg='skyblue')
#----------image---------------------------------------------------------------------------------------
        urlf = Image.open("C:/Users/ELCOT/Downloads/dowloads/jana123-02-01 (2).jpeg")
        urlf = urlf.resize((1600,700),Image.Resampling.LANCZOS)
        self.photo16 = ImageTk.PhotoImage(urlf)
        frlb3 = Label(self.win,image=self.photo16,bg='black',width=1600,height=700)
        frlb3.place(x=0,y=0)
        
        url = Image.open("C:/Python311/Lib/idlelib/backcut.png")
        url = url.resize((150,50),Image.Resampling.LANCZOS)
        self.photo6 = ImageTk.PhotoImage(url)
        frlb3 = Label(self.win,image=self.photo6,bg='white',width=150,height=50)
        frlb3.place(x=630,y=150)
#-------------user name -----------------------------------------------------------------------------------------        
        def on_enter(e):
             self.user.delete(0, 'end')
        def on_leave(e):
            if self.user.get()=='':
                self.user.insert(0,'username')
                
        self.user=Entry(self.win,width=25,fg='black',font=('arial',15),bg='white')
        self.user.place(x=580, y=250)
        self.user.insert(0, 'username')
        self.user.bind('<FocusIn>',on_enter)
        self.user.bind('<FocusOut>',on_leave)
        Frame(self.win,width=280,height=2,bg='black').place(x=580,y=275)
#--------password---------------------------------------------------------------------------------------   
        def on_enter(e):
            self.password.delete(0, 'end')
        def on_leave(e):
            if self.password.get()=='':
                self.password.insert(0,'password')
                
        self.password=Entry(self.win,width=25,fg='black',font=('arial',15),bg='white',show='*')
        self.password.place(x=580, y=300)
        self.password.insert(0, 'password')
        self.password.bind('<FocusIn>',on_enter)
        self.password.bind('<FocusOut>',on_leave)

        Frame(self.win,width=280,height=2,bg='black').place(x=580,y=325)

#------------button----------------------------------------------------------------------------------
        self.but1=Button(self.win,text='LOGIN',font=('bold',10),bg='black',fg='white',padx=10,pady=5,command=self.signin)
        self.but1.place(x=665, y=350)

#-------nextwin function-----------------------------------------------------------------------------------
        
    def signin(self):
        username=self.user.get()
        Password=self.password.get()
        
        if username=='admin' and Password=='jana':
            screen=Toplevel()
            vr=welcome(screen)
        elif username!='admin':
            messagebox.showerror('invalid','invalid usename ')

        elif Password!='jana':
            messagebox.showerror('invalid','invalid password')

   
app=login()
