from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from project_tk import pass1

 
class welcome:
    def __init__(self,win):
        self.win=win
        self.win.title('welcome to OYO')
        self.win.geometry('2000x900')
        self.win.config(bg='white')
        #self.hotelname=''
        #self.address=''
        #self.contact=''
        #self.price=None
        
        global photo
        url= Image.open('C:/Users/ELCOT/Downloads/dowloads/output (2).jpg')
        url=url.resize((130,80),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(url)
        l1= Label(self.win,image=photo,bd=0,width=130,height=80,bg='white')
        l1.place(x=580,y=0)
       
#----------------------------------------------------------------------------------------------------------       
        f1=Frame(self.win,bg='black')
        mycanvas = Canvas(f1,bg='black')
        mycanvas.pack(side=LEFT,fill=BOTH,expand=1)
        yscroll=ttk.Scrollbar(f1,orient='vertical', command=mycanvas.yview)
        yscroll.pack(side=RIGHT, fill='y')
        mycanvas.configure(yscrollcommand=yscroll.set)        
        mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion= mycanvas.bbox('all')))
        myframe=Frame(mycanvas,bg='white')
        mycanvas.create_window((0,0),window=myframe, anchor="nw",height =5050,width =1350)       
        f1.pack(fill="both",expand="1",padx=5,pady=60)
#------------heading------------------------------------------------------------------------
        
        global photo11
        urla = Image.open('sup.jpeg')
        urla = urla.resize((300,200),Image.Resampling.LANCZOS)
        photo11 = ImageTk.PhotoImage(urla)
        frlb2 = Label(myframe,image=photo11,bg='white',width=300,height=200)
        frlb2.place(x=950,y=120)
        
        global photo12
        urlb = Image.open("C:/Users/ELCOT/Downloads/dowloads/janasbi.jpg")
        urlb = urlb.resize((330,200),Image.Resampling.LANCZOS)
        photo12 = ImageTk.PhotoImage(urlb)
        frlb3 = Label(myframe,image=photo12,bg='white',width=330,height=200)
        frlb3.place(x=940,y=350)
        

        global photo13
        urlc= Image.open('offer.jpeg')
        urlc=urlc.resize((300,150),Image.Resampling.LANCZOS)
        photo13=ImageTk.PhotoImage(urlc)
        l1= Label(myframe,image=photo13,width=300,height=150,bg='black')
        l1.place(x=550,y=150)
        
        global photoi
        ulc= Image.open('thank.png')
        ulc=ulc.resize((200,100),Image.Resampling.LANCZOS)
        photoi=ImageTk.PhotoImage(ulc)
        l1= Label(myframe,image=photoi,width=200,height=100,bg='white')
        l1.place(x=550,y=3600)

        global photo14
        urld= Image.open('heading1.jpeg')
        urld=urld.resize((300,250),Image.Resampling.LANCZOS)
        photo14=ImageTk.PhotoImage(urld)
        l2= Label(myframe,image=photo14,width=300,height=150)
        l2.place(x=100,y=150)

        global photoh1
        urd= Image.open('C:/Users/ELCOT/Downloads/dowloads/recomand.jpg')
        urd=urd.resize((300,300),Image.Resampling.LANCZOS)
        photoh1=ImageTk.PhotoImage(urd)
        l2= Label(myframe,image=photoh1,width=300,height=300,bg='white')
        l2.place(x=550,y=310)
        
        global photoh2
        ud= Image.open('C:/Users/ELCOT/Downloads/dowloads/homead.jpeg')
        ud=ud.resize((330,200),Image.Resampling.LANCZOS)
        photoh2=ImageTk.PhotoImage(ud)
        l2= Label(myframe,image=photoh2,width=330,height=200,bg='white')
        l2.place(x=80,y=340)

#------------normalrooms-------------------------------------------------------------
        global photo15  
        urle = Image.open('room1.jpg')
        urle = urle.resize((500,250),Image.Resampling.LANCZOS)
        photo15 = ImageTk.PhotoImage(urle)
        lbroom = Label(myframe,image=photo15,bg='white',width=500,height=250)
        lbroom.place(x=50,y=600)
        
        room1='''OYO The dolphin park hotel\n
        Address: vembuliamman kovil treet
        \t\tvirugambakam chennai\n
        Contact:04423622284\n
        \tper day
        \tprice:1000
        '''
        self.text=Text(myframe,height=10,width=40,font=('arial',8,'bold'))
        self.text.place(x=50,y=860 )
        self.text.insert('end',room1)
        self.text.config(state='disabled')
     

        global photo16
        urlf = Image.open("C:/Users/ELCOT/Downloads/dowloads/IMG-20221213-WA0030.jpg")
        urlf = urlf.resize((500,250),Image.Resampling.LANCZOS)
        photo16 = ImageTk.PhotoImage(urlf)
        frlb3 = Label(myframe,image=photo16,bg='white',width=500,height=250)
        frlb3.place(x=50,y=1100)
        
        room2='''OYO Maple tree hotels room\n
        Address: NGO colony 
        \t\tvadapalani chennai\n
        Contact:0876445434\n
        \tPer day
        \tprice:1200
        '''
        text=Text(myframe,height=10,width=40,font=('arial',8,'bold'))
        text.place(x=50,y=1360 )
        text.insert('end',room2)
        text.config(state='disabled')

        global photo17
        urlg= Image.open('C:/Users/ELCOT/Downloads/dowloads/c0854096522179b0.jpg')
        urlg=urlg.resize((500,250),Image.Resampling.LANCZOS)
        photo17=ImageTk.PhotoImage(urlg)
        l1= Label(myframe,image=photo17,width=500,height=250,bg='white')
        l1.place(x=50,y=1600)

        room3='''OYO tree trend earth rooms\n
        Address: visalakshi nagar 
        \t\t Guidy chennai\n
        Contact:04424745133\n
        \tPer day
        \tprice:1000
        '''

        text=Text(myframe,height=10,width=40,font=('arial',8,'bold'))
        text.place(x=50,y=1860 )
        text.insert('end',room3)
        text.config(state='disabled')

    
        global photo19
        urli = Image.open('C:/Users/ELCOT/Downloads/dowloads/b737637c4d5ab2f0.jpg')
        urli = urli.resize((500,250),Image.Resampling.LANCZOS)
        photo19 = ImageTk.PhotoImage(urli)
        frlb2 = Label(myframe,image=photo19,bg='white',width=500,height=250)
        frlb2.place(x=700,y=600)

        room4='''\tOYO Lemon tree hotel \n
        Address: Mount poonamalle road 
        \t\tManapakkam chennai\n
        Contact:04440407777\n
        \tPer day
        \tprice:1000
        '''

        text=Text(myframe,height=10,width=40,font=('arial',8,'bold'))
        text.place(x=700,y=860 )
        text.insert('end',room4)
        text.config(state='disabled')

      
        global photo20
        urlj = Image.open("C:/Users/ELCOT/Downloads/dowloads/788d43e7ed328e2a.jpg")
        urlj = urlj.resize((500,250),Image.Resampling.LANCZOS)
        photo20 = ImageTk.PhotoImage(urlj)
        frlb3 = Label(myframe,image=photo20,bg='white',width=500,height=250)
        frlb3.place(x=700,y=1100)
        
        room5='''OYO Canyon sun\n
        Address: Arunachalam Road
        \t\tsaligramam chennai\n
        Contact:04448536222\n
        \tPer day
        \tprice:1200
        '''

        text=Text(myframe,height=10,width=40,font=('arial',8,'bold'))
        text.place(x=700,y=1360 )
        text.insert('end',room5)
        text.config(state='disabled')

        global photo21
        urlk= Image.open('C:/Users/ELCOT/Downloads/dowloads/212058fb44465973.webp')
        urlk=urlk.resize((500,250),Image.Resampling.LANCZOS)
        photo21=ImageTk.PhotoImage(urlk)
        l1= Label(myframe,image=photo21,width=500,height=250,bg='white')
        l1.place(x=700,y=1600)


        room6='''OYO Hotel kings rooms\n
        Address: Avvaiyar street
        \t\tEkkatuthangal chennai\n
        Contact:0987654567\n
        \tPer day
        \tprice:1000
        '''

        text=Text(myframe,height=10,width=40,font=('arial',8,'bold'))
        text.place(x=700,y=1860 )
        text.insert('end',room6)
        text.config(state='disabled')
#---------------luxuis----------------------------------------------------------------------------------
        global photo18
        urlh= Image.open('C:/Users/ELCOT/Downloads/dowloads/tumblr_387eb194f4f4d6f6234ee97ce68f6157_0e791fbc_1280.jpg')
        urlh=urlh.resize((600,300),Image.Resampling.LANCZOS)
        photo18=ImageTk.PhotoImage(urlh)
        l2= Label(myframe,image=photo18,width=600,height=300)
        l2.place(x=10,y=2300)

        global photo33
        urh= Image.open('C:/Users/ELCOT/Downloads/dowloads/Screenshot_2022-12-15-09-10-25-529_com.android.chrome-01.jpeg')
        urh=urh.resize((350,150),Image.Resampling.LANCZOS)
        photo33=ImageTk.PhotoImage(urh)
        l2= Label(myframe,image=photo33,width=350,height=150,bg='white')
        l2.place(x=10,y=2600)
        
        global photo2
        url2 = Image.open("C:/Users/ELCOT/Downloads/dowloads/5d2de2da0814f.jpeg")
        url2 = url2.resize((600,300),Image.Resampling.LANCZOS)
        photo2 = ImageTk.PhotoImage(url2)
        frlb3 = Label(myframe,image=photo2,bg='white')
        frlb3.place(x=10,y=2900,width=600,height=300)

        global photo32
        ur2 = Image.open("C:/Users/ELCOT/Downloads/dowloads/Screenshot_2022-12-15-09-10-12-144_com.android.chrome-01.jpeg")
        ur2 = ur2.resize((350,150),Image.Resampling.LANCZOS)
        photo32 = ImageTk.PhotoImage(ur2)
        frlb3 = Label(myframe,image=photo32,bg='white')
        frlb3.place(x=10,y=3210,width=350,height=150)
        
        global photo3
        url3= Image.open('C:/Users/ELCOT/Downloads/dowloads/w-doha-qatar-suite.jpg')
        url3=url3.resize((600,300),Image.Resampling.LANCZOS)
        photo3=ImageTk.PhotoImage(url3)
        l1= Label(myframe,image=photo3,width=600,height=300,bg='white')
        l1.place(x=700,y=2300)

        global photo31
        ur3= Image.open('C:/Users/ELCOT/Downloads/dowloads/hotel2.jpeg')
        ur3=ur3.resize((350,150),Image.Resampling.LANCZOS)
        photo31=ImageTk.PhotoImage(ur3)
        l1= Label(myframe,image=photo31,width=350,height=150,bg='white')
        l1.place(x=700,y=2610)

        global photo4
        url4= Image.open('C:/Users/ELCOT/Downloads/dowloads/like.jpg')
        url4=url4.resize((600,300),Image.Resampling.LANCZOS)
        photo4=ImageTk.PhotoImage(url4)
        l2= Label(myframe,image=photo4,width=600,height=300)
        l2.place(x=700,y=2900)

        global photo41
        ur4= Image.open('C:/Users/ELCOT/Downloads/dowloads/hotel3.jpeg')
        ur4=ur4.resize((350,150),Image.Resampling.LANCZOS)
        photo41=ImageTk.PhotoImage(ur4)
        l2= Label(myframe,image=photo41,width=350,height=150,bg='white')
        l2.place(x=700,y=3210)


#-------------label--------------------------------------------------------------

        self.l1=Button(myframe,text='Booking',font=('Hk Grotesk',12,'bold'),command=self.hotel1,bg='green',fg='white',width=15)
        self.l1.place(x=60, y=1010)

        self.l2=Button(myframe,text='Booking',font=('Hk Grotesk',12,'bold'),bg='green',command=self.hotel2,fg='white',width=15)
        self.l2.place(x=60, y=1520)

        self.l3=Button(myframe,text='Booking',font=('Hk Grotesk',12,'bold'),command=self.hotel3,bg='green',fg='white',width=15)
        self.l3.place(x=60, y=2010)
        
        self.l4=Button(myframe,text='Booking',font=('Hk Grotesk',12,'bold'),command=self.hotel4,bg='green',fg='white',width=15)
        self.l4.place(x=710, y=1010)
        
        self.l5=Button(myframe,text='Booking',font=('Hk Grotesk',12,'bold'),command=self.hotel5,bg='green',fg='white',width=15)
        self.l5.place(x=710, y=1510)
        
        self.l6=Button(myframe,text='Booking',font=('Hk Grotesk',12,'bold'),command=self.hotel6,bg='green',fg='white',width=15)
        self.l6.place(x=710, y=2010)

#---------------------------------------------label----------------------------------------------------------
        
        self.la1=Label(myframe,text=' * Pick your favourite oyo room  ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        self.la1.place(x=30, y=40)
        self.la2=Label(myframe,text=' Offers %', font=('Hk Grotesk',15,'bold'),bg='white',fg='black',width=13)
        self.la2.place(x=60, y=120)
        self.la3=Label(myframe,text='* Currently Available rooms ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        self.la3.place(x=30, y=550)
        #self.la4=Label(myframe,text='  Refer & Earn  ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        #self.la4.place(x=950, y=350)
        self.la5=Label(myframe,text='  New users ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        self.la5.place(x=550, y=120)
        self.la7=Label(myframe,text='  Relax and feel peace in you ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        self.la7.place(x=550, y=40)
        self.la8=Label(myframe,text=' * facilities design to live with joy ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        self.la8.place(x=30, y=320)
        self.la9=Label(myframe,text='  The finest place at the best price  ', font=('Hk Grotesk',15,'bold'),bg='white',fg='black')
        self.la9.place(x=900, y=40)
        self.la10=Label(myframe,text='  currently not available', font=('Hk Grotesk',8,'bold'),bg='white',fg='black')
        self.la10.place(x=560, y=2240)
        self.la11=Label(myframe,text='  luxury rooms  ', font=('Hk Grotesk',20,'bold'),bg='white',fg='black')
        self.la11.place(x=530, y=2200)
        self.la6=Label(myframe,text=' Thank you ', font=('arial',15,'bold'),bg='white',fg='black',width=15)
        self.la6.place(x=550, y=3550)
        
    def hotel1(self):
        self.hotelname='OYO The dolphin park hotel'
        self.address='vembuliamman kovil street virugambakam chennai'
        self.contact='04423622284'
        self.price='1000'
        screen1=Toplevel(self.win)
        obj=pass1(screen1,self.hotelname,self.price,self.address,self.contact)

    def hotel2(self):
        self.hotelname='OYO Maple tree hotels room'
        self.address=' NGO colony vadapalani chennai' 
        self.contact='0876445434'
        self.price='1200'
        screen1=Toplevel(self.win)
        obj=pass1(screen1,self.hotelname,self.price,self.address,self.contact)

        
    def hotel3(self):
        self.hotelname='OYO tree trend earth rooms'
        self.address=' visalakshi nagar Guidy chennai'
        self.contact='04424745133'
        self.price='1000'
        screen1=Toplevel(self.win)
        obj=pass1(screen1,self.hotelname,self.price,self.address,self.contact)
        

    def hotel4(self):
        self.hotelname='OYO Lemon tree hotel '
        self.address=' Mount poonamalle road Manapakkam chennai' 
        self.contact='04440407777'
        self.price='1000'
        screen1=Toplevel(self.win)
        obj=pass1(screen1,self.hotelname,self.price,self.address,self.contact)
        

    def hotel5(self):
        self.hotelname='OYO Canyon sun'
        self.address=' Arunachalam Road saligramam chennai'
        self.contact='04448536222'
        self.price='1200'
        screen1=Toplevel(self.win)
        obj=pass1(screen1,self.hotelname,self.price,self.address,self.contact)
        

    def hotel6(self):
        self.hotelname='OYO Hotel kings rooms'
        self.address=' Avvaiyar street Ekkatuthangal chennai'
        self.contact='0987654567'
        self.price='1000'
        screen1=Toplevel(self.win)
        obj=pass1(screen1,self.hotelname,self.price,self.address,self.contact)

    
        
       
       
if __name__=="__main__":
    win=Tk()
    obj=welcome(win)
      


