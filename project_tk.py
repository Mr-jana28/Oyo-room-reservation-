from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mc
from tkcalendar import DateEntry


        
class pass1:
    def __init__(self,win,hotel,price,address,contact):
        self.win=win
        self.win.title('oyo page')
        self.win.geometry('2000x900')
        self.win.config(bg='white')
        self.hotel=hotel
        self.price=price
        self.address=address
        self.contact=contact
        self.valu=['select value','101','102','103','104','105']
        self.valu1=['select value','Aadhar card','Driving licence','Voter ID card','passport']
        self.valu2=['select value','Singleroom','Doubleroom']
        self.name_var=StringVar()
        self.phonenumber_var=StringVar()
        self.checkin_var=StringVar()
        self.Currentlocation_var=StringVar()
        self.Numberofpersons_var=StringVar()
        self.City_var=StringVar()
        self.Pincode_var=StringVar()
        self.checkout_var=StringVar()
        self.CustomerRef=StringVar()
        self.Numberofdays=StringVar()
        self.Idprooftypes=StringVar()
        self.Numberofkids=StringVar()
        self.Anyspecialrequest=StringVar()
        self.Numberofrooms=StringVar()
#--------oyo label-------------------------------------------------------------------------------------        
        url= Image.open('C:/Users/ELCOT/Downloads/dowloads/output (3).jpg ')
        url=url.resize((130,80),Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(url)
        l1= Label(win,image=self.photo,bd=0)
        l1.place(x=600,y=0,width=130,height=80)
#---------frame-----------------------------------------------------------------------------------------
        self.f=Frame(self.win,bd=0,highlightbackground='black',highlightthickness=1,width=1360,height=600,relief=RAISED)
        self.f.place(x=0,y=60)
        
#----------personal details-----------------------------------------------------------------------------
        self.lb4=Label(self.f,text='Personal Details', font=('Microsoft Yahei UI Light',13,'bold'),bg='black',fg='white')
        self.lb4.place(x=430, y=8)
        self.lb2=Label(self.f,text='Name',font=('Hk Grotesk',12,'bold'),fg='black')
        self.lb2.place(x=70, y=50)
        self.lb5=Label(self.f,text='Current location',font=('Hk Grotesk',12,'bold'),fg='black')
        self.lb5.place(x=40, y=100)
        self.lb7=Label(self.f,text='Id-proof types',font=('Hk Grotesk',12,'bold'),fg='black')
        self.lb7.place(x=500, y=150)
        self.lb3=Label(self.f,text='Phone number',font=('Hk Grotesk',12,'bold'),fg='black')
        self.lb3.place(x=500, y=50)
        self.r1=Label(self.f,text='City',font=('Hk Grotesk',12,'bold'),fg='black')
        self.r1.place(x=580, y=100)
        self.p1=Label(self.f,text='Pincode',font=('arial',12,'bold'),fg='black')
        self.p1.place(x=40, y=150)

#------------booking details-------------------------------------------------------------------------
        
        self.bok=Label(self.f,text='Booking details',font=('Microsoft Yahei UI Light',12,'bold'),bg='black',fg='white')
        self.bok.place(x=430, y=250)
        self.lb6=Label(self.f,text='check-in Date',font=('arial',12,'bold'),fg='black')
        self.lb6.place(x=50, y=300)
        self.lb11=Label(self.f,text='Number of persons',font=('arial',12,'bold'),fg='black')
        self.lb11.place(x=40, y=400)
        self.numb1=Label(self.f,text='Number of kids',font=('arial',12,'bold'),fg='black')
        self.numb1.place(x=480, y=400)
        self.lb6=Label(self.f,text='Any special request',font=('arial',12,'bold'),fg='black')
        self.lb6.place(x=480, y=500)
        self.dp=Label(self.f,text='check-out Date',font=('arial',12,'bold'),fg='black')
        self.dp.place(x=480, y=300)
        self.rooms=Label(self.f,text='Number of rooms',font=('arial',12,'bold'),fg='black')
        self.rooms.place(x=40, y=500)
        
#-----------------------------entry--------------------------------------------------------------------
        self.nam=Entry(self.f,font=('bold',15),textvariable=self.name_var, bd=5)
        self.nam.place(x=200,y= 50)
        self.cur=Entry(self.f,font=('bold',15),width=20,textvariable=self.Currentlocation_var,bd=5)
        self.cur.place(x=200, y=100)
        self.pin=Entry(self.f,font=('bold',15),textvariable=self.Pincode_var,bd=5)
        self.pin.place(x=200 ,y=150)
        self.avi=Entry(self.f,font=('bold',15),width=20,textvariable=self.Numberofpersons_var,bd=5)
        self.avi.place(x=200, y=400)
        self.num=Entry(self.f,font=('bold',15),width=20,textvariable=self.Numberofkids,bd=5)
        self.num.place(x=650, y=400)

#---------right-------------------------------------------------------------------------
    
        self.ph=Entry(self.f,font=('bold',15),textvariable=self.phonenumber_var,bd=5)
        self.ph.place(x=650, y=50)
        self.cit=Entry(self.f,font=('bold',15),textvariable=self.City_var,bd=5)
        self.cit.place(x=650, y=100)
        self.id=ttk.Combobox(self.f,value=self.valu1,font=('bold',15),textvariable=self.Idprooftypes,width=19)
        self.id.current(0)
        self.id.place(x=650, y=150)
        self.r6rom=Entry(self.f,font=('bold',15),textvariable=self.Anyspecialrequest,width=20,bd=5)
        self.r6rom.place(x=650, y=500)
        self.room=ttk.Combobox(self.f,value=self.valu2,font=('bold',15),width=19,textvariable=self.Numberofrooms)
        self.room.current(0)
        self.room.place(x=200, y=500)
#--------------------button-----------------------------------------------------------------------------
        self.bt1=Button(self.f,text='Book now & pay at hotel ',font=('arial',12,'bold'),bg='green',fg='white',command=self.jana)
        self.bt1.place(x=800, y=550)

        c2=Button(win,text='<< Previous ',font=('arial',12,'bold'),bg='red',width=15,fg='white',command=win.destroy)
        c2.place(x=30,y=610)
         
#----------------------------calendar----------------------------------------------------------        
        self.ari=DateEntry(self.f,width=8,selectmode='day',font=('arial',12,'bold'),background='darkblue',foreground='white')
        self.ari.place(x=200 ,y=300)
        
        self.dep=DateEntry(self.f,width=8,selectmode='day',font=('arial',12,'bold'),background='darkblue',foreground='white')
        self.dep.place(x=650 ,y=300)
#---------------room facilites-------------------------------------------------------------------------
        self.l1=Label(self.f,text='Rules & restrictions ',font=('Microsoft Yahei UI Light',18,'bold'),fg='black')
        self.l1.place(x=990, y=30)
        self.l1=Label(self.f,text='* Mandatory to wear mask ', font=('arial',10,'bold'),fg='black')
        self.l1.place(x=1020, y=80)
        self.l1=Label(self.f,text='* Guests can check in using  ', font=('arial',10,'bold'),fg='black')
        self.l1.place(x=1020, y=100)
        self.l1=Label(self.f,text=' any local outstation ID proof', font=('arial',8,'bold'),fg='black')
        self.l1.place(x=1025, y=120)
        self.l1=Label(self.f,text=' (PAN card not accepted)', font=('arial',10,'bold'),fg='black')
        self.l1.place(x=1025, y=140)
        self.pay1=Label(self.f,text=' Payment facilites',font=('Microsoft Yahei UI Light',18,'bold'),fg='black')
        self.pay1.place(x=990, y=170) 
        self.l1=Label(self.f,text=' * Debit card ', font=('arial',10,'bold'),fg='black',width=13)
        self.l1.place(x=1015, y=210)
        self.l1=Label(self.f,text=' * Credit card ', font=('arial',10,'bold'),fg='black',width=15)
        self.l1.place(x=1010, y=240)
        self.l6=Label(self.f,text=' * Cash and mobile payment',font=('arial',10,'bold'),fg='black')
        self.l6.place(x=1030, y=270)
        self.l1=Label(self.f,text=' Room facilities ', font=('Microsoft Yahei UI Light',18,'bold'),fg='black',width=15)
        self.l1.place(x=980, y=310)
        self.l7=Label(self.f,text=' * Free wifi facilities ', font=('arial',10,'bold'),fg='black')
        self.l7.place(x=1020, y=350)
        self.l2=Label(self.f,text=' * En-suite bathrooms',font=('arial',10,'bold'),fg='black')
        self.l2.place(x=1020, y=380)
        self.l3=Label(self.f,text=' * Air conditioning or fan cooling system ',font=('arial',10,'bold'),fg='black')
        self.l3.place(x=1020, y=410)
        self.l4=Label(self.f,text=' * Free parking',font=('arial',10,'bold'),fg='black')
        self.l4.place(x=1020, y=440)
        self.l5=Label(self.f,text=' * Kitchen facilites',font=('arial',10,'bold'),fg='black')
        self.l5.place(x=1020, y=470)
   
        
#---------------new win-------------------------------------------------------------------------------
        
    def jana(self):
        
        self.diff = ((self.dep.get_date())-(self.ari.get_date())).days
        self.amount=int( self.price)*int(self.diff)
        root=Tk()
        root.title('bill page')
        root.geometry('2000x900')
        root.config(bg='white')
        b1=Label(root,text='Bill details',font=('Hk Grotesk',15,'bold'),bg='white',fg='red')
        b1.pack()
        
        f1=Frame(root,highlightbackground='black',highlightthickness=5,width=480,height=320,bd=5,relief=RAISED)
        f1.place(x=10, y=40)
        scrol=Scrollbar(f1,orient=VERTICAL)
        scrol1=Scrollbar(f1,orient=HORIZONTAL)
        scrol1.pack(side=BOTTOM,fill=X)
        scrol.pack(side=LEFT,fill=Y)
        textarea=Text(f1,font=('arial',13),yscrollcommand=scrol.set,width=180,height=28)
        textarea.pack(fill=BOTH)
        textarea.config(state='normal')
        scrol.config(command=textarea.yview)
        

        if self.nam.get()=='' or self.ari.get()=='' or self.num.get()=='' or self.avi.get()=='' or self.cur.get()=='' or self.pin.get()==''  or self.cit.get()=='' or self.id.get()=='' or self.ph.get()=='' or self.dep.get()=='':
            messagebox.showerror('error','Incompleted error',parent=self.win)
            
        elif self.nam.get()!='@':
            textarea.delete(1.0,END)
            textarea.insert(END,f'='*150)  
            textarea.insert(END,f'\n\n\t\t\t\t\t\t\tCustomer Details')
            textarea.insert(END,'\n')
            textarea.insert(END,f'-'*230) 
            textarea.insert(END,f'\n\n\t\t\t\tName: {self.nam.get()}')
            textarea.insert(END,f'\t\t\t\t\tPhone number :{self.ph.get()}')
            textarea.insert(END,f'\n\n\t\t\t\tId prof type :{self.id.get()}')
            textarea.insert(END,f'\t\t\t\t\tAddress: {self.cur.get()}')
            textarea.insert(END,f'\n\n\t\t\t\tcity: {self.cit.get()}') 
            textarea.insert(END,f'\t\t\t\t\tpincode: {self.pin.get()}')
            textarea.insert(END,'\n\n\n')
            textarea.insert(END,f'='*150)
            textarea.insert(END,'\n\n')
            textarea.insert(END,f'\t\t\t\t\t\t\t OYO Room reservation details')
            textarea.insert(END,'\n')
            textarea.insert(END,f'-'*230) 
            textarea.insert(END,f'\n\n\t\t\t\tNumber of persons: {self.avi.get()}')
            textarea.insert(END,f'\t\t\t\t\tNumber of kids: {self.num.get()}')
            textarea.insert(END,f'\n\n\t\t\t\tcheck in date : {self.ari.get()}')
            textarea.insert(END,f'\t\t\t\t\tcheck out date: {self.dep.get()}')
            textarea.insert(END,f'\n\n\t\t\t\tNumber of rooms: {self.room.get()}')
            textarea.insert(END,f'\t\t\t\t\t Special request: {self.r6rom.get()}')
            textarea.insert(END,f'\n\t\t\t\t\t\t\t Perday Price: {self.price}') #{self.price}')
            textarea.insert(END,'\n')
            textarea.insert(END,f'='*150)
            #textarea.insert(END,'\n')
            textarea.insert(END,f'\n\t\t\t\t\t\t\tTotal amout: {self.amount} ')#{self.price}')
            textarea.insert(END,'\n')
            textarea.insert(END,f'='*150)
            textarea.insert(END,'\n')
            textarea.insert(END,f'\t\t\t\t\t\t\tHotel Details')#{}')
            textarea.insert(END,f'\n\n\t\t\t\t Hotel name: {self.hotel} ')
            textarea.insert(END,f'\t\t\t\t\tHotel Contact no : {self.contact}')
            textarea.insert(END,f'\n\n\t\t\t\t Hotel Location:{self.address}')
            textarea.insert(END,'\n')
            textarea.insert(END,f'='*150)
            textarea.insert(END,'\n')
            textarea.insert(END,f'\n\t\t\t\t\t\t\t Successfully Room Reserved')
            textarea.insert(END,'\n')
            textarea.insert(END,f'='*150)
            textarea.insert(END,'\n')
            textarea.insert(END,f'\n\n\t\t\t\t\t\t\t\tThank you')          
            textarea.config(state='disabled')
            e_phonenumber = self.phonenumber_var.get()
            e_name = self.name_var.get()
            e_numberofperson = self.Numberofpersons_var.get()
            e_number_kids=self.Numberofkids.get()
            e_checkin=self.ari.get()
            e_checkout=self.dep.get()
            e_id_proof=self.Idprooftypes.get()
            e_number_rooms=self.Numberofrooms.get()
            e_anyspecialrequest=self.Anyspecialrequest.get()
        
            conn = mc.connect(host="localhost",user="root", password="",  database="project3")
            cur = conn.cursor()
            cur.execute("insert into customerdetails1(name, phonenumber, id_proof, checkin ,checkout, number_persons, number_kids, number_rooms, anyspecial_request) values('"+e_name+"', '"+e_phonenumber+"','"+e_id_proof+"','"+e_checkin+"','"+e_checkout+"','"+e_numberofperson+"','"+e_number_kids+"','"+e_number_rooms+"','"+e_anyspecialrequest+"')")
            messagebox.showinfo('info','data insert',parent=root)
            conn.close()
#---------file-----------------------------------------------------------------------------------------
        def bill():
            f= open('oyobill.txt','w+')
            f.write(f'='*200)  
            f.write(f'\n\n\t\t\t\t\t\t\tCustomer Details')
            f.write(f'\n\n\t\t\t\tName: {self.nam.get()}')
            f.write(f'\t\t\t\t\tPhone number :{self.ph.get()}')
            f.write(f'\n\n\t\t\t\tId prof type :{self.id.get()}')
            f.write(f'\t\t\tAddress: {self.cur.get()}')
            f.write(f'\n\n\t\t\t\tcity: {self.cit.get()}') 
            f.write(f'\t\t\t\t\tpincode: {self.pin.get()}')
            f.write('\n\n\n')
            f.write(f'='*200)
            f.write('\n\n')
            f.write(f'\t\t\t\t\t\t\t OYO Room reservation details')
            f.write(f'\n\n\t\t\t\tNumberofpersons: {self.avi.get()}')
            f.write(f'\t\t\t\t\tNumber of kids: {self.num.get()}')
            f.write(f'\n\n\t\t\t\tcheck in date : {self.ari.get()}')
            f.write(f'\t\t\t\t\tcheck out date: {self.dep.get()}')
            f.write(f'\n\n\t\t\t\tNumber of rooms: {self.room.get()}')
            f.write(f'\t\t\t\tSpecial request: {self.r6rom.get()}')
            f.write(f'\n\t\t\t\t\t\t\t Price: {self.price}') #{self.price}')
            f.write('\n')
            f.write(f'='*200)
            f.write('\n')
            f.write(f'\n\t\t\t\t\t\t\tTotal amout: {self.amount} ')#{self.price}')
            f.write('\n')
            f.write(f'='*200)
            f.write('\n')
            f.write(f'\t\t\t\t\t\t\tHotel Details')#{}')
            f.write(f'\n\n\t\t\t\t Hotel name: {self.hotel} ')
            f.write(f'\t\t\t\t\tHotel Contact no : {self.contact}')
            f.write(f'\n\n\t\t\t\t Hotel Location:{self.address}')
            f.write('\n')
            f.write(f'='*200)
            f.write('\n')
            f.write(f'\n\t\t\t\t\t\t\t Successfully Room Reserved')
            f.write('\n')
            f.write(f'='*200)
            f.write('\n')
            f.write(f'\n\n\t\t\t\t\t\t\t Thank you')
            f.close()
            
                
#-----------------button-----------------------------------------------------------------------------------------------                
        label1=Button(root,text='bill Download',font=('arial',12,'bold'),bg='green',command=bill,fg='white',width=15,height='2')
        label1.place(x=700, y=620)
        c1=Button(root,text='EXIT',font=('arial',12,'bold'),bg='red',fg='white',width=10,height='2',command=root.destroy)
        c1.place(x=300,y=620)
         

if __name__=="__main__":
    win=Tk()
    obj=pass1(win)




