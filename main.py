from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
import sqlite3
from PIL import ImageTk

root = Tk()
root.title("Library Management System")
root.geometry("1100x650")
root.resizable(0, 0)

#images
homebg=ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bb1.png')
logobg=ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/logo.png')
logbg=ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/log.png')
backimg= PhotoImage(file='/home/ak/Downloads/sabi/Back1.png')
addimg=ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bt1.png')
issimg=ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bt2.png')
srimg =ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bt7.png')
lgimg =ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bt8.png')
stimg =ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bt3.png')
rtimg =ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/bt4.png')
userimg =ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/user.png')
passimg =ImageTk.PhotoImage(file='/home/ak/Downloads/sabi/pass.png')

def addbook():
    bookfrm=Frame(root).place(x=0,y=100)
    label1=Label(bookfrm,bg='white',width=1100,height=600).place(x=0,y=100)
    detailfrm=LabelFrame(bookfrm,bg='lightblue',width=350,height=400).place(x=20,y=180)
    
    bookid=StringVar()
    title=StringVar()
    author=StringVar()
    edition=StringVar()
    qty=StringVar()

    def clear():
        bookid.set("")
        title.set("")
        author.set("")
        edition.set("")
        qty.set("")
    
    def add():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute(
                "INSERT INTO books values(?,?,?,?,?)",
                (bookid.get(),title.get(),author.get(),edition.get(),qty.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Book  Added Successfully")
    def update():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute(
                "UPDATE books set title=?,author=?,Edition=?,qty=? where "
                "id=?",
                (title.get(),author.get(),edition.get(),qty.get(),bookid.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Book Details Updated Successfully")
    def delete():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM books where id=?",
                        (bookid.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Book Deleted Successfully")
    backbtn=Button(detailfrm,command=home,image=backimg,bg='white',activebackground='white',highlightbackground='white',bd=0).place(x=30,y=110)
    addbtn=Button(bookfrm,bg='#0f624c',highlightbackground='#0f624c',highlightthickness=2,bd=0,font=("",10,'bold'),fg='white',text='Add Book',width=15,command=add).place(x=400,y=580,height=40)
    updatebtn=Button(bookfrm,bg='#0f624c',highlightbackground='#0f624c',highlightthickness=2,bd=0,font=("",10,'bold'),fg='white',text='Update Book',width=15,command=update).place(x=600,height=40,y=580)
    deletebtn=Button(bookfrm,bg='#0f624c',highlightbackground='#0f624c',highlightthickness=2,bd=0,font=("",10,'bold'),fg='white',text='Delete Book',width=15,command=delete).place(x=800,height=40,y=580)
    clearbtn=Button(detailfrm,bg='#0f624c',highlightbackground='#0f624c',highlightthickness=2,bd=0,font=("",10,'bold'),fg='white',text='Clear',width=15,command=clear).place(x=120,y=520,height=40)

    label=Label(detailfrm,text="Book ID :",font=("",10,'bold'),bg='lightblue',width=10).place(x=25,y=230)
    label=Label(detailfrm,text="Title :",font=("",10,'bold'),bg='lightblue',width=10).place(x=25,y=280)
    label=Label(detailfrm,text="Author :",font=("",10,'bold'),bg='lightblue',width=10).place(x=25,y=330)
    label=Label(detailfrm,text="Edition :",font=("",10,'bold'),bg='lightblue',width=10).place(x=25,y=380)
    label=Label(detailfrm,text="Quantity :",font=("",10,'bold'),bg='lightblue',width=12).place(x=22,y=430)
    idtxt=Entry(detailfrm,textvariable=bookid,width=20,justify='center',font=("",10,'bold'),highlightcolor='#0f624c',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=230,height=25)
    titletxt=Entry(detailfrm,textvariable=title,width=20,justify='center',font=("",10,'bold'),highlightcolor='#0f624c',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=280,height=25)
    authtxt=Entry(detailfrm,textvariable=author,width=20,justify='center',font=("",10,'bold'),highlightcolor='#0f624c',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=330,height=25)
    edtxt=Entry(detailfrm,textvariable=edition,width=20,justify='center',font=("",10,'bold'),highlightcolor='#0f624c',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=380,height=25)
    qtytxt=Entry(detailfrm,textvariable=qty,width=20,justify='center',font=("",10,'bold'),highlightcolor='#0f624c',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=430,height=25)

    
    def book_info(ev):
        viewInfo = book_tree.focus()
        dn_data = book_tree.item(viewInfo)
        row = dn_data['values']
        bookid.set(row[0])
        title.set(row[1])
        author.set(row[2])
        edition.set(row[3])
        qty.set(row[4])

    def show_all():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("select * from books")
        rows = cur.fetchall()
        book_tree.delete(*book_tree.get_children())
        for row in rows:
            book_tree.insert('', END, values=row)
        conn.commit()
        conn.close()
    scrollbary = Scrollbar(detailfrm, orient=VERTICAL)
    book_tree = ttk.Treeview(detailfrm)
    book_tree.place(x=400, y=180, width=570, height=400)
    book_tree.configure( yscrollcommand=scrollbary.set)
    book_tree.configure(selectmode="extended")
    scrollbary.configure(command=book_tree.yview)
    scrollbary.place(x=970, y=180, width=10, height=400)
    book_tree.configure(columns=("id","Title","Author","Edition"))
    book_tree.heading("id", text="Id", anchor=N)
    book_tree.heading("Title", text="Title",anchor=CENTER)
    book_tree.heading("Author", text="Author",anchor=CENTER)
    book_tree.heading("Edition", text="Edition",anchor=CENTER)

    book_tree.column("#0", stretch=NO, minwidth=0, width=0)
    book_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=CENTER)
    book_tree.column("#2", stretch=NO, minwidth=0, width=170, anchor=CENTER)
    book_tree.column("#3", stretch=NO, minwidth=0, width=170, anchor=CENTER)
    book_tree.column("#4", stretch=NO, minwidth=0, width=180, anchor=CENTER)
    book_tree.bind("<ButtonRelease-1>", book_info)
    show_all()  

def issuebook():

    lc=Label(root,bg='white',width=1000,height=600)
    lc.place(x=0,y=120)
    lc=Label(root,bg='#0f624c',width=50,height=2)
    lc.place(x=100,y=160)

    lc=Label(root,text='STUDENT  INFORMATION',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
    lc.place(x=170,y=170)

    lb=Label(root,text='Roll No :',bg='#fff',fg='black',font=('',10,'bold'))
    lb.place(x=120,y=235)
    em = Entry(root, width=20,bd=0,highlightthickness=2,highlightcolor='orange',highlightbackground='#0f624c',font=('',10, 'bold'))
    em.place(x=210, y=230,height=30)
    
    backbt = Button(root,width=60,bg='white',highlightbackground='white',activebackground='white',bd=0,image=backimg,command=home)
    backbt.place(x=20, y=110)
    book_id=StringVar()
    title=StringVar()

    def checkbk():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE id=? and title=?",[book_id.get(),title.get()])
        var=cur.fetchone()
        if var!=None:
            if var[4]==0:
                messagebox.showwarning('Error',var[1]+' Book is Not Available !')
            else :
                Qty=var[4]-1
                cur.execute("INSERT INTO store values(?,?,?,?,?)",[var[0],var[1],var[2],student_id,"Issued"])
                cur.execute("UPDATE books set qty=? where id=?",[Qty,var[0]])
                conn.commit()
                messagebox.showwarning('Success',var[1]+' Book Issued !')
                issuebook()
        else:
            messagebox.showwarning('Warning','YOUR DATA IS NOT FOUND !')
        conn.commit()
        conn.close()

    def checkst():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE id=?",[em.get()])
        var=cur.fetchone()
        if var!=None:
              global student_id
              student_id=var[0]
              lb1=Label(root,text='Name :',fg='black',bg='white',font=('',12,'bold'))
              lb1.place(x=100,y=400)
              lb2 = Label(root, text=var[1], fg='black', bg='white',font=('', 12, 'bold'))
              lb2.place(x=200, y=400)
              lb3 = Label(root, text='Course :',fg='black',bg='white', font=('', 12, 'bold'))
              lb3.place(x=100, y=440)
              lb4 = Label(root, text=var[3],fg='black',bg='white', font=('', 12, 'bold'))
              lb4.place(x=200, y=440)
              lb5 = Label(root, text='Year :', fg='black',bg='white', font=('', 12, 'bold'))
              lb5.place(x=100, y=480)
              lb6 = Label(root, text=var[4], fg='black',bg='white', font=('', 12, 'bold'))
              lb6.place(x=200, y=480)
              lb7 = Label(root, text='Contact :', fg='black',bg='white', font=('', 12, 'bold'))
              lb7.place(x=100, y=520)
              lb8 = Label(root, text=var[2],fg='black',bg='white', font=('', 12, 'bold'))
              lb8.place(x=200, y=520)


              fr=Frame(root,bg='#fff',bd=5,relief='flat',width=370,height=320)
              fr.place(x=490,y=155)
              ff=Frame(fr,bg='#0f624c',bd=2,relief='flat',width=400,height=35)
              ff.place(x=0,y=0)
              lb=Label(ff,text='ISSUE BOOK',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
              lb.place(x=150,y=5)
              tt=Label(fr,text='Book-ID',bg='#fff',fg='black',font=('',10,'bold'))
              tt.place(x=50,y=60)
              e1 = Entry(fr, width=20,bd=0,textvariable=book_id,highlightthickness=2,highlightcolor='orange',highlightbackground='#0f624c',font=('',10, 'bold'))
              e1.place(x=160, y=60)
              ttp = Label(fr, text='Title', bg='#fff', fg='black', font=('', 10, 'bold'))
              ttp.place(x=50, y=110)
              e2 = Entry(fr, width=20,bd=0,highlightthickness=2,highlightcolor='orange',highlightbackground='#0f624c',font=('',10, 'bold'), textvariable=title)
              e2.place(x=160, y=110)
              bt1 = Button(fr, text='Submit', width=18, bg='#0f624c', fg='#fff', font=('', 10,'bold'),command=checkbk,bd=5,relief='flat')
              bt1.place(x=80, y=160)

        else:
                messagebox.showwarning('Warning','These Student are not Registered !')
    bt = Button(root, text='Submit', width=14, bg='red', fg='#fff', font=('', 10, 'bold'),highlightbackground='red',highlightthickness=2,bd=0,command=checkst)
    bt.place(x=200,y=300)

def return_book():
    lc=Label(root,bg='white',width=1000,height=600)
    lc.place(x=0,y=120)
    lc=Label(root,bg='#0f624c',width=50,height=2)
    lc.place(x=350,y=160)

    lc=Label(root,text='STUDENT  INFORMATION',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
    lc.place(x=420,y=170)

    lb=Label(root,text='Roll No :',bg='#fff',fg='black',font=('',10,'bold'))
    lb.place(x=360,y=230)
    em = Entry(root, width=20,highlightthickness=2,bd=0,highlightcolor='orange',highlightbackground='#0f624c', font=('',10, 'bold'))
    em.place(x=460, y=230,height=30)
    
    backbt = Button(root,width=60,bg='white',highlightbackground='white',activebackground='white',bd=0,image=backimg,command=home)
    backbt.place(x=20, y=110)
    def check():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE id=?",[em.get()])
        var=cur.fetchone()
        cur.execute("SELECT * FROM store WHERE student_roll=?",[em.get()])
        varr=cur.fetchone()
        if var!=None and varr!=None:
              lb1=Label(root,text='Name :',fg='black',bg='white',font=('Arial',15,'bold'))
              lb1.place(x=60,y=400)
              lb2 = Label(root, text=var[1], fg='black', bg='white',font=('Arial', 15, 'bold'))
              lb2.place(x=150, y=400)
              lb3 = Label(root, text='Course :',fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb3.place(x=60, y=430)
              lb4 = Label(root, text=var[3],fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb4.place(x=150, y=430)
              lb5 = Label(root, text='Year :', fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb5.place(x=60, y=460)
              lb6 = Label(root, text=var[4], fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb6.place(x=150, y=460)
              lb7 = Label(root, text='Contact :', fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb7.place(x=60, y=490)
              lb8 = Label(root, text=var[2],fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb8.place(x=150, y=490)
              lb9 = Label(root, text='issued Book :', fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb9.place(x=60, y=520)
              lb10 = Label(root, text=varr[1],fg='black',bg='white', font=('Arial', 15, 'bold'))
              lb10.place(x=200, y=520)
              op=messagebox.askyesno('Warning','Confirm  return the Book !')
              if op:
                cur.execute("SELECT * FROM books WHERE id=?",[varr[0]])
                varb=cur.fetchone()
                Qty=varb[4]+1
                cur.execute("UPDATE store set status=? where student_roll=?",["Returned",varr[3]])
                cur.execute("UPDATE books set qty=? where id=?",[Qty,var[0]])
                conn.commit()
                messagebox.showwarning('Success',varr[1]+' Book Return !')
                return_book()
              else:
                messagebox.showwarning('Warning','Book Not returned !')
        conn.commit()
        conn.close()
    bt = Button(root, text='Submit', width=14, bg='red', fg='#fff', font=('', 10, 'bold'),highlightbackground='red',highlightthickness=2,bd=0,command=check)
    bt.place(x=450,y=300,height=40)

def search():
    bookfrm=Frame(root).place(x=0,y=0)
    label1=Label(bookfrm,bg='white',width=1000,height=600).place(x=0,y=100)
    search_book=StringVar()
    lc=Label(root,bg='#0f624c',width=50,height=2)
    lc.place(x=450,y=160)

    lc=Label(root,text='Search Book',bg='#0f624c',fg='#fff',font=('Arial',12,'bold'))
    lc.place(x=560,y=170)

    lb=Label(root,text='Enter Book Title :',bg='#fff',fg='black',font=('',10,'bold'))
    lb.place(x=460,y=230)
    backbtn=Button(bookfrm,command=home,image=backimg,bg='white',activebackground='white',highlightbackground='white',bd=0).place(x=40,y=110)
    searchtxt=Entry(bookfrm,width=20,bd=0,textvariable=search_book,highlightbackground='orange',highlightcolor='green',highlightthickness=2,font=("",10,'bold')).place(x=600,y=225,height=30)
    def Search():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("select * from books where title=?",[search_book.get()])
        rows = cur.fetchone()
        conn.commit()
        conn.close()
        detailfrm=LabelFrame(bookfrm,bg='#ffd580',width=350,height=400).place(x=20,y=180)

        label=Label(detailfrm,text="Book ID :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=230)
        label=Label(detailfrm,text="Title :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=280)
        label=Label(detailfrm,text="Author :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=330)
        label=Label(detailfrm,text="Edition :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=380)
        label=Label(detailfrm,text="Quantity :",font=("",10,'bold'),bg='#ffd580',width=12).place(x=22,y=430)
        idtxt=Label(detailfrm,text=rows[0],width=20,font=("",10,'bold'),bd=0).place(x=150,y=230,height=25)
        titletxt=Label(detailfrm,text=rows[1],width=20,font=("",10,'bold'),bd=0).place(x=150,y=280,height=25)
        authtxt=Label(detailfrm,text=rows[2],width=20,font=("",10,'bold'),bd=0).place(x=150,y=330,height=25)
        edtxt=Label(detailfrm,text=rows[3],width=20,font=("",10,'bold'),bd=0).place(x=150,y=380,height=25)
        qttxt=Label(detailfrm,text=rows[4],width=20,font=("",10,'bold'),bd=0).place(x=150,y=430,height=25)
        search_book.set("")
    searchbtn=Button(bookfrm,text='Search',font=('Arial', 10, 'bold'),fg='white',width=19,bg='#0f624c',command=Search,highlightbackground='#0f624c',highlightthickness=2,bd=0).place(x=560,y=300,height=35)

def student():
    bookfrm=Frame(root).place(x=0,y=100)
    label1=Label(bookfrm,bg='white',width=1100,height=600).place(x=0,y=100)
    detailfrm=LabelFrame(bookfrm,bg='#ffd580',width=350,height=400).place(x=20,y=180)

    studentid=StringVar()
    name=StringVar()
    mob=StringVar()
    dep=StringVar()
    year=StringVar()

    def clear():
        studentid.set("")
        name.set("")
        mob.set("")
        dep.set("")
        year.set("")
    
    def add():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute(
                "INSERT INTO student values(?,?,?,?,?)",
                (studentid.get(),name.get(),mob.get(),dep.get(),year.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Student Id  Added Successfully")
    def update():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute(
                "UPDATE student set name=?,mob=?,dep=?,year=? where "
                "id=?",
                (name.get(),mob.get(),dep.get(),year.get(),studentid.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Student Id Updated Successfully")
    def delete():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM student where id=?",
                        (studentid.get()))
        conn.commit()
        conn.close()
        show_all()
        clear()
        messagebox.showinfo("Success", "Student Id  Deleted Successfully")
    backbtn=Button(detailfrm,command=home,image=backimg,bg='white',activebackground='white',highlightbackground='white',bd=0).place(x=30,y=110)
    addbtn=Button(bookfrm,text='Add Student',highlightbackground='#0f624c',highlightthickness=2,bd=0,bg='#0f624c',font=("",10,'bold'),fg='white',width=15,command=add).place(x=400,y=580,height=40)
    updatebtn=Button(bookfrm,text='Update Student',highlightbackground='#0f624c',highlightthickness=2,bd=0,bg='#0f624c',font=("",10,'bold'),fg='white',width=15,command=update).place(x=600,y=580,height=40)
    deletebtn=Button(bookfrm,text='Delete Student',highlightbackground='#0f624c',highlightthickness=2,bd=0,bg='#0f624c',font=("",10,'bold'),fg='white',width=15,command=delete).place(x=800,y=580,height=40)
    clearbtn=Button(detailfrm,text='Clear',highlightbackground='#0f624c',highlightthickness=2,bd=0,bg='#0f624c',font=("",10,'bold'),fg='white',width=15,command=clear).place(x=120,y=520,height=40)

    label=Label(detailfrm,text="Roll No :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=230)
    label=Label(detailfrm,text="Name :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=280)
    label=Label(detailfrm,text="Mobile :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=330)
    label=Label(detailfrm,text="Course :",font=("",10,'bold'),bg='#ffd580',width=10).place(x=25,y=380)
    label=Label(detailfrm,text="year :",font=("",10,'bold'),bg='#ffd580',width=12).place(x=22,y=430)
    idtxt=Entry(detailfrm,textvariable=studentid,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=230,height=25)
    titletxt=Entry(detailfrm,textvariable=name,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=280,height=25)
    authtxt=Entry(detailfrm,textvariable=mob,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=330,height=25)
    edtxt=Entry(detailfrm,textvariable=dep,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=380,height=25)
    qtytxt=Entry(detailfrm,textvariable=year,width=20,justify='center',font=("",10,'bold'),highlightcolor='#c70039',highlightthickness=2,bd=0,highlightbackground='gray').place(x=150,y=430,height=25)

    
    def book_info(ev):
        viewInfo = book_tree.focus()
        dn_data = book_tree.item(viewInfo)
        row = dn_data['values']
        studentid.set(row[0])
        name.set(row[1])
        mob.set(row[2])
        dep.set(row[3])
        year.set(row[4])

    def show_all():
        conn = sqlite3.connect("/home/ak/Downloads/sabi/library.db")
        cur = conn.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        book_tree.delete(*book_tree.get_children())
        for row in rows:
            book_tree.insert('', END, values=row)
        conn.commit()
        conn.close()
    scrollbary = Scrollbar(detailfrm, orient=VERTICAL)
    book_tree = ttk.Treeview(detailfrm)
    book_tree.place(x=400, y=180, width=570, height=400)
    book_tree.configure( yscrollcommand=scrollbary.set)
    book_tree.configure(selectmode="extended")
    scrollbary.configure(command=book_tree.yview)
    scrollbary.place(x=970, y=180, width=10, height=400)
    book_tree.configure(columns=("id","name","mob","course"))
    book_tree.heading("id", text="Id", anchor=N)
    book_tree.heading("name", text="Name",anchor=CENTER)
    book_tree.heading("mob", text="Mobile",anchor=CENTER)
    book_tree.heading("course", text="Course",anchor=CENTER)

    book_tree.column("#0", stretch=NO, minwidth=0, width=0)
    book_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=CENTER)
    book_tree.column("#2", stretch=NO, minwidth=0, width=170, anchor=CENTER)
    book_tree.column("#3", stretch=NO, minwidth=0, width=170, anchor=CENTER)
    book_tree.column("#4", stretch=NO, minwidth=0, width=180, anchor=CENTER)
    book_tree.bind("<ButtonRelease-1>", book_info)
    show_all()  

def home():
    label1=Label(root,bg='white',width=1000,height=650).place(x=0,y=0)
    label2=Label(root,bg='#0f624c',width=1000,height=6).place(x=-50,y=0)
    label3=Label(root,text="Dashboard",font=("",25,'bold'),bg='white').place(x=170,y=140)
    label4=Label(root,image=homebg,bg='white',bd=0).place(x=570,y=170)
    label4=Label(root,image=logbg,bg='#0f624c',bd=0).place(x=100,y=10)
    label2=Label(root,bg='#0f624c',text='Library management System',fg='white',font=("",25,'bold')).place(x=300,y=20)
    
    date=StringVar()
    date.set(strftime('%x '))
    label2=Label(root,bg='white',text="Date : "+date.get(),font=("",12,'bold')).place(x=870,y=120)

    bt1=Button(root,text='Add Books',image=addimg,compound=LEFT,fg='#fff',bg='red',width=160,font=('Arial',15,'bold'),highlightthickness=2,highlightbackground='red',bd=0,command=addbook,cursor='hand2')
    bt1.place(x=40,y=250,height=55)
    

    bt2 = Button(root, text='Issue Books', image=issimg,compound=LEFT,fg='#fff', bg='red',highlightthickness=2,highlightbackground='red', font=('Arial', 15, 'bold'),width=160, bd=0,command=issuebook,cursor='hand2')
    bt2.place(x=40, y=380,height=55)
    
    bt3 = Button(root, text='Return Books', image=rtimg,compound=LEFT,fg='#fff', bg='red',highlightthickness=2,highlightbackground='red', font=('Arial', 15, 'bold'),width=160,bd=0,cursor='hand2',command=return_book)
    bt3.place(x=40, y=505,height=55)
    
    bt4 = Button(root, text='Add Students ', image=stimg,compound=LEFT,fg='#fff', bg='red',highlightthickness=2,highlightbackground='red', font=('Arial', 15, 'bold'),width=160,bd=0,cursor='hand2',command=student)
    bt4.place(x=300, y=250,height=55)
    
    bt5 = Button(root, text='Search Books',image=srimg,compound=LEFT, fg='#fff', bg='red',highlightthickness=2,highlightbackground='red', font=('Arial', 15, 'bold'),width=160,bd=0,cursor='hand2',command=search)
    bt5.place(x=300, y=380,height=55)
    
    bt6 = Button(root, text='  log Out', image=lgimg,compound=LEFT,fg='#fff', bg='red',highlightthickness=2,highlightbackground='red', font=('Arial', 15, 'bold'),width=160, bd=0,cursor='hand2',command=login)
    bt6.place(x=300, y=505,height=55)

def login():
    User=StringVar()
    Passw=StringVar()
    def log():
        if User.get()=="" and Passw.get()=="":
            messagebox.showerror("Error !","Fill the Details")
        else:
            if User.get()=="ak" and Passw.get()=="1234":
                home()
            else:
                messagebox.showerror("Error !","No Accounts Found!")
    label1=Label(root,bg='white',width=1000,height=650).place(x=0,y=0)

    label2=Label(root,bg='white',text='Library management System',fg='#0f624c',font=("",22,'bold')).place(x=300,y=50)
    
    label1=Label(root,bg='white',image=userimg).place(x=550,y=280)
    label1=Label(root,bg='white',image=passimg).place(x=550,y=350)
    label1=Label(root,bg='white',image=logobg).place(x=100,y=200)
    user=Entry(root,textvariable=User,highlightbackground='#0f624c',font=("",10,'bold'),highlightcolor='orange',highlightthickness=2,bd=0,width=24).place(x=600,y=280,height=32)
    password=Entry(root,textvariable=Passw,highlightbackground='#0f624c',font=("",10,'bold'),highlightcolor='orange',highlightthickness=2,bd=0,width=24).place(x=600,y=350,height=32)
    submit=Button(root,text='Login',cursor='hand2',bg='#0f624c',highlightthickness=2,bd=0,highlightbackground='#0f624c',fg='white',font=("",10,'bold'),width=27,command=log).place(x=550,y=430,height=38)

login()
root.mainloop()