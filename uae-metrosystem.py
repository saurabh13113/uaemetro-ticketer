import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import turtle
import mysql.connector as mys
from tkinter import ttk


#TURTLE LOADING SCREEN
colors = [ "red","purple","cyan","lime","orange","yellow"]
win=turtle.Screen()
turtle.bgcolor("black")
pen=turtle.Turtle()
for x in range(100):
    pen.pencolor(colors[x % 6])
    pen.width(x/100 + 1)
    pen.forward(x)
    pen.left(59)
    pen.speed(5000)
    
turtle.color('red')     
#turtle.done()
pen.hideturtle()
pen.penup()
pen.setposition(x=25,y=250)
arg=("WELCOME TO THE E-METRO SYSTEM!")
pen.write(arg,align='center', font=('Comic Sans MS',25,'bold'))
turtle.hideturtle()
turtle.exitonclick()


#WELCOME SCREEN
def welcome():
    root=Tk()
    root.geometry("600x400")
    root.title("E-METRO SYSTEM")
    root['background'] = 'dark turquoise'
    root.iconbitmap("C:/Users/saura/Desktop/gui/uae.ico")
    
    def opeen(): #CUSTOMER OR ADMIN
        cancel()
        root=Tk()
        root.geometry("300x250")
        root.title("ABU DHABI TERMINAL")
        root['background'] = 'Olive Drab1'
        root.iconbitmap("C:/Users/saura/Desktop/gui/uae.ico")
        
        btncust=Button(root,text="CUSTOMER",command=booking,borderwidth=10,font='Times 9')
        btnadmin=Button(root,text="ADMINISTRATOR",command=login,borderwidth=10,bg="red2",activebackground='Royalblue1',font='Times 9 bold')
        
        btncust.place(x=70,y=50,width=150,height=50)
        btnadmin.place(x=50,y=150,width=200,height=50)
       
    def cancel():
        root.destroy()
        
    btncont=Button(root,text="CONTINUE",command=opeen,borderwidth=10,activebackground='blue',font='sans 9 bold',bg="red3")
    btncanc=Button(root,text="CANCEL",command=cancel,borderwidth=10)
    lblwelc=Label(root,text="WELCOME TO THE EMETRO SYSTEM;\n THE FASTEST MODE OF LAND TRANSPORT CONNECTING ALL 7 EMIRATES",bg="red",font='sans 8 bold',borderwidth=10,relief="groove")
    img1=ImageTk.PhotoImage(Image.open("C:/Users/saura/Desktop/gui/metr.png"))
    lblimag=Label(root,image=img1,borderwidth=5,relief="solid")

    lblimag.place(x=200,y=120)
    lblwelc.place(x=50,y=50)
    btncont.place(x=350,y=300,height=50)
    btncanc.place(x=150,y=300,height=50)
    root.mainloop()
    
#ADMIN LOGIN SCREEN
def login():
    def clear():
        euser.delete(0,END)
        epass.delete(0,END)
        disc.delete(0,END)
        etype.delete(0,END)
        menudest.delete(0,END)
        
    def submit():
        username=euser.get()
        pasw=epass.get()
        
        if username=="admin" or username=="ADMIN" and pasw=="1998": 
            messagebox.showinfo("Login ", "LOGIN SUCCESSFUL")
            root.destroy()
            booking2()
        else:
            r=messagebox.askyesno("LOGIN DENIED","ENTERED PASSWORD/ID IS INCORRECT.DO YOU WISH TO RETRY?")
            

                          
    root=Tk()
    root.geometry("400x200")
    root.title("ADMINISTRATOR LOGIN")
    root['background'] = 'orchid2'
    root.iconbitmap("C:/Users/saura/Desktop/gui/uae.ico")
    lbluser=Label(root,text="USERNAME:",font="Helvetica 10")
    lblpass=Label(root,text="PASSWORD:",fg="red",font="Helvetica 10")
    euser=Entry(root,borderwidth=10,font="bold")
    epass=Entry(root,borderwidth=10,font="bold",show="*")
    btnclear=Button(root,text="CLEAR",command=clear,bd=4)
    btnlog=Button(root,text="LOGIN",command=submit,bd=4,activebackground='Royalblue2',bg="red")

    lbluser.grid(row=1,column=0,padx=10,pady=10)
    euser.grid(row=1,column=1,padx=10,pady=10)
    lblpass.grid(row=2,column=0,padx=10)
    epass.grid(row=2,column=1,padx=10,pady=0)
    btnclear.place(x=100,y=130,width=80,height=40)
    btnlog.place(x=200,y=130,width=80,height=40)
    root.mainloop()
    
def rates():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("TICKET RATES")
    root['background'] = 'thistle2'
    ttk.Label(root,text ="TICKET RATES",background="light slate blue",font = ("Times New Roman Bold", 20)).pack()
    frame = Frame(root)
    frame.pack()
    tree = ttk.Treeview(frame, columns = (1,2), height = 100, show = "headings")
    tree.pack(side = 'right')
    tree.heading(1, text = "DESTINATION")
    tree.heading(2, text = "PRICE")
    tree.column(1, width = 130)
    tree.column(2, width = 130)
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side = 'right', fill = 'y')
    rs=[("DUBAI","100"),("SHARJAH","150"),("AJMAN","200"),("RAS AL KHAIMAH","250"),("FUJAIRAH","300"),("UMM AL QUWAIN","400"),("---------------","-------"),("SENIOR CITIZEN","25 % OFF"),("GOVT WORKER","50% OFF")]             
    for val in rs:
        tree.insert('', 'end', values = (val[0], val[1]))
        
#CUSTOMER BOOKING
def booking():
    rates()
    def clear1():
        ename.delete(0,END)
        eno.delete(0,END)
        menudest.delete(0,END)
        edisc.delete(0,END)
        etype.delete(0,END)
        
    def submit1():#CUSTOMER BILL PRINT
        global typ
        global pricE
        name=ename.get()
        se=str(menudest.get())
        typ=str(etype.get())
        nos=int(eno.get())
        disc=str(edisc.get())
        
        if se=="DUBAI" or se=="Dubai":
            r=100
        elif se=="Sharjah" or se=="SHARJAH":
            r=150
        elif se=="Ajman" or se=="AJMAN":
            r=200
        elif se=="Fujairah" or se=="FUJAIRAH":
            r=300
        elif se=="Ras Al Khaimah" or se=="RAS AL KHAIMAH":
            r=250
        elif se=="Umm Al Quwain" or se=="UMM AL QUWAIN":
            r=400
            
        if typ=="ONE-WAY" or typ=="one-way" or typ=="ONEWAY":
            ttyp=1
        elif typ=="TWO-WAY" or typ=="twoway" or typ=="TWOWAY":
            ttyp=2
            
        pricE=r*nos*ttyp
        disC="NO DISCOUNT"
        if disc=="SENIOR CITIZEN" or disc=="SENIOR CITIZEN":
            pricE=(r*nos*ttyp)*0.75
            disC="SENIOR CITIZEN"
        elif disc=="GOVERNMENT WORKER" or disc=="government worker" or disc=="GOVT WORKER":
            pricE=(r*nos*ttyp)*0.50
            disC="GOV. EMPLOYEE"
   
            
        #print(disc,typ,s,d)
        price=str(pricE)
        messagebox.showinfo("BILL","YOUR TOTAL BILL IS "+price +"AED. PLEASE PAY AT NEAREST COUNTER")
        
        try:
            myconn=mys.connect(host='localhost',user="root",\
                                passwd="adis",database="emetro")
            mycur=myconn.cursor()
        
            query="show tables";
            mycur.execute("insert into uaemetro values\
                                    ('{}','{}',{},'{}','{}',{})".format(name,se,nos,typ,disC,pricE))
            myconn.commit()
        except Exception as e:
            print(e)
        
        
    root=Tk()
    root.geometry("600x600")
    root.title("TICKET BOOKING")
    root['background'] = 'turquoise3'
    root.iconbitmap("C:/Users/saura/Desktop/gui/uae.ico")
    #s=tk.IntVar()
    #d=tk.IntVar()
    #s.set(1)
    #d.set(1)
    
    lbldest=Label(root,text="DESTINATION:",font="Helvetica 15")
    menudest=Entry(root,borderwidth=8)
    lblname=Label(root,text="NAME:",font="Helvetica 15")
    ename=Entry(root,borderwidth=8)
    lblno=Label(root,text="NUMBER OF TICKETS:",font="Helvetica 15")
    eno=Entry(root,borderwidth=8)
    lbltype=Label(root,text="TICKET TYPE:",font="Helvetica 15")
    lbltype1=Label(root,text="[ONE-WAY/TWO-WAY]",font="Helvetica 10")

    etype=Entry(root,borderwidth=8)
    #rdtype1=Radiobutton(root,text="ONE-WAY",variable=s,value=1)
    #rdtype2=Radiobutton(root,text="TWO-WAY",variable=s,value=2)
    lbldisc=Label(root,text="DISCOUNT:",font="Helvetica 15")
    edisc=Entry(root,borderwidth=8)
    #rdtype3=Radiobutton(root,text="GOVERNMENT WORKER",variable=d,value=3)
    #rdtype4=Radiobutton(root,text="SENIOR CITIZEN",variable=d,value=2)
    #rdtype5=Radiobutton(root,text="NO DISCOUNT",variable=d,value=1)
    btnclear=Button(root,text="CLEAR",command=clear1,bd=4,bg="brown2",font='sans 12 bold')
    btnsub=Button(root,text="PRINT",command=submit1,bd=4,activebackground='red',bg='#ffb3fe',font='Times 12 bold')
   
    lbldest.place(x=50,y=110)
    menudest.place(x=350,y=100,width=150,height=50)
    lblname.place(x=50,y=50)
    ename.place(x=350,y=50)
    lblno.place(x=50,y=180)
    eno.place(x=350,y=180,width=70)
    lbltype.place(x=50,y=250)
    lbltype1.place(x=50,y=280)
    etype.place(x=350,y=250)
    #rdtype1.place(x=350,y=250)
    #rdtype2.place(x=350,y=275)
    lbldisc.place(x=50,y=325)
    edisc.place(x=350,y=325,width=200)
    #rdtype3.place(x=350,y=325)
    #rdtype4.place(x=350,y=350)
    #rdtype5.place(x=350,y=375)
    btnclear.place(x=100,y=475,width=150,height=50)
    btnsub.place(x=350,y=475,width=150,height=50)
    root.mainloop()
    
#ADMIN BOOKING
def booking2():
    rates()
    def clear2():
        ename.delete(0,END)
        eno.delete(0,END)
        menudest.delete(0,END)
        edisc.delete(0,END)
        etype.delete(0,END)
        
    def submit2():#ADMIN BILL PRINT
        global typ
        global pricE
        name=ename.get()
        se=str(menudest.get())
        typ=str(etype.get())
        nos=int(eno.get())
        disc=str(edisc.get())
        
        if se=="DUBAI" or se=="Dubai":
            r=100
        elif se=="Sharjah" or se=="SHARJAH":
            r=150
        elif se=="Ajman" or se=="AJMAN":
            r=200
        elif se=="Fujairah" or se=="FUJAIRAH":
            r=300
        elif se=="Ras Al Khaimah" or se=="RAS AL KHAIMAH":
            r=250
        elif se=="Umm Al Quwain" or se=="UMM AL QUWAIN":
            r=400
            
        if typ=="ONE-WAY" or typ=="one-way" or typ=="ONEWAY":
            ttyp=1
        elif typ=="TWO-WAY" or typ=="twoway" or typ=="TWOWAY":
            ttyp=2
            
        pricE=r*nos*ttyp
        disC="NO DISCOUNT"
        if disc=="SENIOR CITIZEN" or disc=="SENIOR CITIZEN":
            pricE=(r*nos*ttyp)*0.75
            disC="SENIOR CITIZEN"
        elif disc=="GOVERNMENT WORKER" or disc=="government worker" or disc=="GOVT WORKER":
            pricE=(r*nos*ttyp)*0.50
            disC="GOV. EMPLOYEE"
   
            
        #print(disc,typ,s,d)
        price=str(pricE)
        messagebox.showinfo("BILL","YOUR TOTAL BILL IS "+price +"AED. PLEASE PAY AT NEAREST COUNTER")
        
        try:
            myconn=mys.connect(host='localhost',user="root",\
                                passwd="adis",database="emetro")
            mycur=myconn.cursor()
        
            query="show tables";
            mycur.execute("insert into uaemetro values\
                                    ('{}','{}',{},'{}','{}',{})".format(name,se,nos,typ,disC,pricE))
            myconn.commit()
        except Exception as e:
            print(e)
    '''       
    def rates():
        root = tk.Tk()
        root.geometry("400x400")
        root.title("TICKET RATES")
        root['background'] = 'thistle2'
        ttk.Label(root,text ="TICKET RATES",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2), height = 100, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "DESTINATION")
        tree.heading(2, text = "PRICE")
        tree.column(1, width = 130)
        tree.column(2, width = 130)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')
        rs=[("DUBAI","100"),("SHARJAH","150"),("AJMAN","200"),("RAS AL KHAIMAH","250"),("FUJAIRAH","300"),("UMM AL QUWAIN","400")]
             
        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1]))
    '''
            
    def display(): #DISPLAY ALL CUSTOMERS 
        try:
            myconn = mys.connect(host='localhost', user="root",\
                         passwd="adis", database="emetro")
            
            mycur = myconn.cursor()
            query = "select * from uaemetro ORDER BY name"
            mycur.execute(query)
            rs = mycur.fetchall()
            root = tk.Tk() 
            root.geometry("900x700")
            root.title("CUSTOMER REGISTER")
            root['background'] = 'black'
            ttk.Label(root,text ="CUSTOMER REGISTER",background="aquamarine2",font = ("Times New Roman Bold", 20)).pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6), height = 100, show = "headings")
            tree.pack(side = 'right')
            tree.heading(1, text = "NAME.")
            tree.heading(2, text = "DESTINATION")
            tree.heading(3, text = "TICKETS")
            tree.heading(4, text = "TICKET TYPE")
            tree.heading(5, text = "DISCOUNT")
            tree.heading(6, text = "PRICE")
            tree.column(1, width = 130)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 130)
            tree.column(5, width = 130)
            tree.column(5, width = 130)
            tree.column(6, width = 130)
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side = 'right', fill = 'y')

            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5]))
        except Exception as e:
            print(e)
               
    def update(): #UPDATE A CUSTOMER
        global typ
        global pricE
        name=ename.get()
        se=str(menudest.get())
        typ=str(etype.get())
        nos=int(eno.get())
        disc=str(edisc.get())
        
        if se=="DUBAI" or se=="Dubai":
            r=100
        elif se=="Sharjah" or se=="SHARJAH":
            r=150
        elif se=="Ajman" or se=="AJMAN":
            r=200
        elif se=="Fujairah" or se=="FUJAIRAH":
            r=300
        elif se=="Ras Al Khaimah" or se=="RAS AL KHAIMAH":
            r=250
        elif se=="Umm Al Quwain" or se=="UMM AL QUWAIN":
            r=400
        
        if typ=="ONE-WAY" or typ=="one-way" or typ=="ONEWAY":
            ttyp=1
        elif typ=="TWO-WAY" or typ=="twoway" or typ=="TWOWAY":
            ttyp=2
           
           
        pricE=r*nos*ttyp
        disC="NO DISCOUNT"
        if disc=="SENIOR CITIZEN" or disc=="SENIOR CITIZEN":
            pricE=(r*nos*ttyp)*0.75
            disC="SENIOR CITIZEN"
        elif disc=="GOVERNMENT EMPLOYEE" or disc=="Government employee":
            pricE=(r*nos*ttyp)*0.50
            disC="GOV. EMPLOYEE"
   
            
        #print(disc,typ,pricE)
        price=str(pricE)
        messagebox.showinfo("BILL","YOUR NEW TOTAL BILL IS "+price +"AED. PLEASE PAY AT NEAREST COUNTER")
        messagebox.showinfo("INFORMATION","CUSTOMER RECORD SUCCESFULLLY UPDATED")

            
        try:
            myconn=mys.connect(host='localhost',user="root",\
                            passwd="adis",database="emetro")
            mycur=myconn.cursor()
            query="update uaemetro set tno={},disc='{}',price={},dest='{}',type='{}'\
                    where name='{}'".format(nos,disC,price,se,typ,name);
            mycur.execute(query)
            myconn.commit()
            
        
        except Exception as e:
            print(e)
        display()  
    
    def delete(): #TO DELETE A CUSTOMER RECORD
        try:
            myconn=mys.connect(host='localhost',user="root",\
                                passwd="adis",database="emetro")
            mycur=myconn.cursor()
            cname=ename.get()
            query="delete from uaemetro where name='{}'".format(cname);
            mycur.execute(query)
            myconn.commit()
            display()
        
        except Exception as e:
            print(e)
        messagebox.showinfo("INFORMATION","CUSTOMER RECORD SUCCESFULLLY DELETED")
        
    
    def search(): #SEARCH BY CUST NAME
        name = ename.get()
        try:
            myconn=mys.connect(host='localhost',user="root",\
                            passwd="adis",database="emetro")
            if myconn.is_connected():
                mycur=myconn.cursor()
                name = ename.get()
                query="select * from uaemetro where name='{}'".format(name);
                mycur.execute(query)
                r=mycur.fetchall()
                
                for row in r:
                    if row!=None:
                        messagebox.showinfo("INFORMATION","CUSTOMER RECORD SUCCESFULLLY FOUND")
                        menudest.insert(END,row[1])
                        edisc.insert(END,row[4])
                        etype.insert(END,row[3])
                        eno.insert(END,row[2])
                        print("NAME  ","DEST","QUANTITY","TYPE","DISCOUNT","PRICE",sep="\t")
                        print(row[0],row[1],row[2]," ",row[3],row[4],row[5],sep="\t")
                    else:
                        messagebox.showinfo("INFORMATION","CUSTOMER RECORD NOT FOUND")
                        
        except Exception as e:
            print(e)
        
    ''' 
        try:
            myconn=mys.connect(host='localhost',user="root",\
                            passwd="adis",database="emetro")
            if myconn.is_connected():
                print("CONNECTION SUCCESFUL \n")
            mycur=myconn.cursor()
            query="select * from uaemetro";
            mycur.execute(query)
            lst1=mycur.fetchall()
            print(lst1)
            total_rows = len(lst1)
            total_columns =6 
  
            class Table: 
      
                def __init__(self,root): 
          
        # code for creating table 
                    for i in range(total_rows): 
                        for j in range(total_columns): 
                  
                            font=('Arial',15,'bold')
                            self.e = Entry(root, width=20, fg='red',font=font,bg="cyan")
                        
                      
                  
                            self.e.grid(row=i, column=j) 
                            self.e.insert(END, lst1[i][j]) 
            root = Tk() 
            t = Table(root) 
            root.mainloop()
        except Exception as e:
            print(e)
    '''
    
    
        
    root=Tk()
    root.geometry("600x700")
    root.title("TICKET BOOKING")
    root['background'] = 'turquoise3'
    root.iconbitmap("C:/Users/saura/Desktop/gui/uae.ico")
    #s=tk.IntVar()
    #d=tk.IntVar()
    #s.set(1)
    #d.set(1)
    
    lbldest=Label(root,text="DESTINATION:",font="Helvetica 15")
    menudest=Entry(root,borderwidth=8)
    lblname=Label(root,text="NAME:",font="Helvetica 15")
    ename=Entry(root,borderwidth=8)
    lblno=Label(root,text="NUMBER OF TICKETS:",font="Helvetica 15")
    eno=Entry(root,borderwidth=8)
    lbltype=Label(root,text="TICKET TYPE:",font="Helvetica 15")
    lbltype1=Label(root,text="[ONE-WAY/TWO-WAY]",font="Helvetica 10")

    etype=Entry(root,borderwidth=8)
    #rdtype1=Radiobutton(root,text="ONE-WAY",variable=s,value=1)
    #rdtype2=Radiobutton(root,text="TWO-WAY",variable=s,value=2)
    lbldisc=Label(root,text="DISCOUNT:",font="Helvetica 15")
    edisc=Entry(root,borderwidth=8)
    #rdtype3=Radiobutton(root,text="GOVERNMENT WORKER",variable=d,value=3)
    #rdtype4=Radiobutton(root,text="SENIOR CITIZEN",variable=d,value=2)
    #rdtype5=Radiobutton(root,text="NO DISCOUNT",variable=d,value=1)
    
    btnclear=Button(root,text="CLEAR",command=clear2,bd=4,bg="brown1",font='sans 12 bold')
    btnsearch=Button(root,text="SEARCH",command=search,bd=4,bg="Rosybrown1",font='sans 12 bold')
    btndisplay=Button(root,text="DISPLAY",command=display,bd=4,bg="Rosybrown1",font='sans 12 bold')
    btnsub=Button(root,text="PRINT",command=submit2,bd=4,activebackground='red',bg='#ffb3fe',font='Times 12 bold')
    btnupdate=Button(root,text="UPDATE",command=update,bd=4,bg="Rosybrown1",font='sans 12 bold')
    btndelete=Button(root,text="DELETE",command=delete,bd=4,bg="Rosybrown1",font='sans 12 bold')

   
    lbldest.place(x=50,y=110)
    menudest.place(x=350,y=100,width=150,height=50)
    lblname.place(x=50,y=50)
    ename.place(x=350,y=50)
    lblno.place(x=50,y=180)
    eno.place(x=350,y=180,width=70)
    lbltype.place(x=50,y=250)
    lbltype1.place(x=50,y=280)
    etype.place(x=350,y=250)
    #rdtype1.place(x=350,y=250)
    #rdtype2.place(x=350,y=275)
    lbldisc.place(x=50,y=325)
    edisc.place(x=350,y=325,width=200)
    #rdtype3.place(x=350,y=325)
    #rdtype4.place(x=350,y=350)
    #rdtype5.place(x=350,y=375)

    btnclear.place(x=100,y=610,width=150,height=50)
    btnsub.place(x=350,y=610,width=150,height=50)
    btnsearch.place(x=100,y=450,width=150,height=50)
    btndisplay.place(x=350,y=450,width=150,height=50)
    btnupdate.place(x=100,y=530,width=150,height=50)
    btndelete.place(x=350,y=530,width=150,height=50)

    root.mainloop()

#booking2()
welcome()


 
 
 
 
   
