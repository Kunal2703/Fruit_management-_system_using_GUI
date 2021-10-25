from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter import messagebox
import sqlite3 as db


def connection():
    connectObj = db.connect("Fruit_Management_System.db")
    cur = connectObj.cursor()
    sql = '''
    create table if not exists selling (
        date string,
        Fruits string,
        price number,
        quantity number,
        total number
        )
    '''
    cur.execute(sql)
    connectObj.commit()


connection()
window = Tk()
window.title("Fruit Store Management System")
tabs = ttk.Notebook(window)

#Sell frame

root = ttk.Frame(tabs)
root = Frame(tabs,bg="#FFEFDB")
root.pack(side=TOP, fill=X)
tabs.add(root, text='Sell')
#Left Image
load1 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/Apple.png")
resize_image1 = load1.resize((80,120),Image.ANTIALIAS)
new_image1 = ImageTk.PhotoImage(resize_image1)
img1 = Label(root,image = new_image1)
img1.place(x=1,y=0)

load2 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/guavas.jpg")
resize_image2 = load2.resize((80,120),Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resize_image2)
img2 = Label(root,image = new_image2)
img2.place(x=1,y=105)

load3 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/Grapes.jpg")
resize_image3 = load3.resize((80,120),Image.ANTIALIAS)
new_image3 = ImageTk.PhotoImage(resize_image3)
img3 = Label(root,image = new_image3)
img3.place(x=1,y=206)

#Right Image
load4 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/Banana.jpg")
resize_image4 = load4.resize((80,120),Image.ANTIALIAS)
new_image4 = ImageTk.PhotoImage(resize_image4)
img4 = Label(root,image = new_image4)
img4.place(x=1200,y=0)

load5 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/Orange.jpg")
resize_image5 = load5.resize((80,120),Image.ANTIALIAS)
new_image5 = ImageTk.PhotoImage(resize_image5)
img5 = Label(root,image = new_image5)
img5.place(x=1200,y=105)

load6 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/Pomegranate.jpg")
resize_image6 = load6.resize((80,120),Image.ANTIALIAS)
new_image6 = ImageTk.PhotoImage(resize_image6)
img6 = Label(root,image = new_image6)
img6.place(x=1200,y=206)

#stock Frame
root2 = ttk.Frame(tabs)
root2 = Frame(tabs,bg="#FFEFDB")
root2.pack(side=TOP, fill=X)
tabs.add(root2, text='Stock')

load = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/6FSMS_2.jpg")
resize_image = load.resize((650,520),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resize_image)
img = Label(root2,image = new_image)
img.place(x=600,y=1)

load7 = Image.open("/Users/kunalsingh/Desktop/Python_Internship/Python/Fruit Management System in Python/img_file/fruit-vegetables-summer-food-background-260nw-1142293649.jpg")
resize_image7 = load7.resize((1250,125),Image.ANTIALIAS)
new_image7 = ImageTk.PhotoImage(resize_image7)
img7 = Label(root2,image = new_image7)
img7.place(x=1,y=530)

tabs.pack(expand=1, fill="both")


def GenerateBill():
    connectObj = db.connect("Fruit_Management_System.db")
    cur = connectObj.cursor()

    global billarea
    if Fruit1_quantity.get() == 0 and Fruit2_quantity.get() == 0 and Fruit3_quantity.get() == 0 and Fruit4_quantity.get() == 0:
        messagebox.showerror("Error", "No Fruit purchased")
    else:
        billarea.delete('1.0', END)
        billarea.insert(END, "\t|| Fruit Store Management System ||")
        billarea.insert(END, "\n_________________________________________\n")
        billarea.insert(END, "\nDate\t Fruits\tPrice(Kg)\t   QTY\t Total")
        billarea.insert(END, "\n==========================================")

        price = IntVar()
        price2 = IntVar()
        price3 = IntVar()
        price4 = IntVar()

        print(dateE.get())
        price = price2 = price3 = price4 = 0

        if Fruit1_quantity.get() != 0:
            price = Fruit1_quantity.get() * p1price.get()
            print(price)
            billarea.insert(END, f"\n{dateE.get()}\t Apple \t{p1price.get()}\t {Fruit1_quantity.get()}\t {price}")

            sql = '''
            INSERT INTO Selling VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql, (dateE.get(), 'Apple', p1price.get(), Fruit1_quantity.get(), price))
            connectObj.commit()

        if Fruit2_quantity.get() != 0:
            price2 = (Fruit2_quantity.get() * p2price.get())
            print(price2)
            billarea.insert(END, f"\n{dateE.get()}\t Guava \t{p2price.get()}\t {Fruit2_quantity.get()}\t {price2}")

            sql = '''
            INSERT INTO Selling VALUES 
            (?, ?, ?, ?,?)
            '''
            print(dateE.get(), 'Guava', p2price.get(), Fruit2_quantity.get(), price2)
            cur.execute(sql, (dateE.get(), 'Guava', p2price.get(), Fruit2_quantity.get(), price2))
            connectObj.commit()

        if Fruit3_quantity.get() != 0:
            price3 = Fruit3_quantity.get() * p1price.get()
            print(price3)
            billarea.insert(END, f"\n{dateE.get()}\tGrapes \t{p3price.get()}\t {Fruit3_quantity.get()}\t {price3}")

            sql = '''
            INSERT INTO Selling VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql, (dateE.get(), 'Grapes', p3price.get(), Fruit3_quantity.get(), price3))
            connectObj.commit()

        if Fruit4_quantity.get() != 0:
            price4 = Fruit4_quantity.get() * p1price.get()
            billarea.insert(END, f"\n{dateE.get()}\tMango \t{p4price.get()}\t {Fruit4_quantity.get()}\t {price4}")

            sql = '''
            INSERT INTO Selling VALUES 
            (?, ?, ?, ?,?)
            '''
            cur.execute(sql, (dateE.get(), 'Mango', p4price.get(), Fruit4_quantity.get(), price4))
            connectObj.commit()

        Totalprice = IntVar()
        Totalprice = price + price2 + price3 + price4

        Totalquantity = IntVar()
        Totalquantity = Fruit1_quantity.get() + Fruit2_quantity.get() + Fruit3_quantity.get() + Fruit4_quantity.get()
        billarea.insert(END, f"\nTotal \t \t  \t{Totalquantity}\t {Totalprice}")


def view():
    connectObj = db.connect("Fruit_Management_System.db")
    cur = connectObj.cursor()

    sql = 'Select * from Selling'
    cur.execute(sql)

    rows = cur.fetchall()
    viewarea.insert(END, f"Date\t Fruits\t  Price of 1 Kg\t  Quantity in Kg\t  Price\n")

    for i in rows:
        allrows = ""
        for j in i:
            allrows += str(j) + '\t'
        allrows += '\n'
        viewarea.insert(END, allrows)


dateL = Label(root, text="Date", bg="#FF6103", width=12, font=('arial', 15, 'bold'))
dateL.grid(row=0, column=0, padx=7, pady=7)

dateE = DateEntry(root, width=12, font=('arial', 15, 'bold'))
dateE.grid(row=0, column=1, padx=7, pady=7)

l = Label(root, text="Fruits", font=('arial', 15, 'bold'), bg="#FFC125", width=12)
l.grid(row=1, column=0, padx=7, pady=7)

l = Label(root, text="Price(Kg)", font=('arial', 15, 'bold'), bg="#FFC125", width=12)
l.grid(row=1, column=1, padx=7, pady=7)

l = Label(root, text="Quantity in Kg", font=('arial', 15, 'bold'), bg="#FFC125", width=12)
l.grid(row=1, column=2, padx=7, pady=7)

#Product1-Apple
p1name = StringVar()
p1name.set('Apple')

p1price = IntVar()
p1price.set(120)

Fruit1_quantity = IntVar()
Fruit1_quantity.set(0)

l = Label(root, text=p1name.get(), font=('arial', 15, 'bold'),bg="#BFEFFF", width=12)
l.grid(row=2, column=0, padx=7, pady=7)

l = Label(root, text=p1price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=2, column=1, padx=7, pady=7)

t = Entry(root, textvariable=Fruit1_quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=2, column=2, padx=7, pady=7)

#Product2-Guava
p2name = StringVar()
p2name.set('Guava')

p2price = IntVar()
p2price.set(65)

Fruit2_quantity = IntVar()
Fruit2_quantity.set(0)

l = Label(root, text=p2name.get(), font=('arial', 15, 'bold'),bg="#BFEFFF", width=12)
l.grid(row=3, column=0, padx=7, pady=7)

l = Label(root, text=p2price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=3, column=1, padx=7, pady=7)

t = Entry(root, textvariable=Fruit2_quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=3, column=2, padx=7, pady=7)

#Product3-Grapes
p3name = StringVar()
p3name.set('Grapes')

p3price = IntVar()
p3price.set(150)

Fruit3_quantity = IntVar()
Fruit3_quantity.set(0)

l = Label(root, text=p3name.get(), font=('arial', 15, 'bold'),bg="#BFEFFF", width=12)
l.grid(row=4, column=0, padx=7, pady=7)

l = Label(root, text=p3price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=4, column=1, padx=7, pady=7)

t = Entry(root, textvariable=Fruit3_quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=4, column=2, padx=7, pady=7)

#Product2-Mango
p4name = StringVar()
p4name.set('Mango')

p4price = IntVar()
p4price.set(80)

Fruit4_quantity = IntVar()
Fruit4_quantity.set(0)

l = Label(root, text=p4name.get(), font=('arial', 15, 'bold'),bg="#BFEFFF", width=12)
l.grid(row=5, column=0, padx=7, pady=7)

l = Label(root, text=p4price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=5, column=1, padx=7, pady=7)

t = Entry(root, textvariable=Fruit4_quantity, font=('arial', 15, 'bold'), width=12)
t.grid(row=5, column=2, padx=7, pady=7)

#Bill--------------
billarea = Text(root)

submitbtn = Button(root, command=GenerateBill, text="Bill",
                   font=('arial', 15, 'bold'),fg = "black", bg="#308014",height=2, width=20)

submitbtn.grid(row=7, column=0, padx=7, pady=7)

viewbtn = Button(root, command=view, text="View All Selling Details",
                 font=('arial', 15, 'bold'), bg="#308014", height=2, width=20)

viewbtn.grid(row=7, column=2, padx=7, pady=7)

billarea.grid(row=9, column=0)
viewarea = Text(root)
viewarea.grid(row=9, column=2)


#Stock--------------------
def connection2():
    connectObj2 = db.connect("Fruit_Management_System.db")
    cur = connectObj2.cursor()
    sql = '''
    create table if not exists stocks (
        date string,
        Fruits string,
        price number,
        quantity number
        )
    '''
    cur.execute(sql)
    connectObj2.commit()


connection2()


def addStock():
    global dateE2, qty, name, price

    connectObj = db.connect("Fruit_Management_System.db")
    cur = connectObj.cursor()
    sql = '''
            INSERT INTO stocks VALUES 
            (?, ?, ?, ?)
            '''
    cur.execute(sql, (dateE2.get(), name.get(), price.get(), qty.get()))
    connectObj.commit()


def viewStock():
    connectObj = db.connect("Fruit_Management_System.db")
    cur = connectObj.cursor()

    sql = 'Select * from stocks'
    cur.execute(sql)

    rows = cur.fetchall()
    viewarea2.insert(END, f"Date \tFruits\t  Price\t  Quantity\t \n")

    for i in rows:
        allrows = ""
        for j in i:
            allrows += str(j) + '\t'
        allrows += '\n'
        viewarea2.insert(END, allrows)



dateL = Label(root2, text="Date", bg="#FF6103", width=12, font=('arial', 15, 'bold'))
dateL.grid(row=0, column=0, padx=7, pady=7)

dateE2 = DateEntry(root2, width=12, font=('arial', 15, 'bold'))
dateE2.grid(row=0, column=1, padx=7, pady=7)

l = Label(root2, text="Fruits", font=('arial', 15, 'bold'), bg="#BFEFFF", width=12)
l.grid(row=1, column=0, padx=7, pady=7)

l = Label(root2, text="Price", font=('arial', 15, 'bold'), bg="#BFEFFF", width=12)
l.grid(row=2, column=0, padx=7, pady=7)

l = Label(root2, text="Quantity in Kg", font=('arial', 15, 'bold'), bg="#BFEFFF", width=12)
l.grid(row=3, column=0, padx=7, pady=7)

name = StringVar()
price = IntVar()
qty = IntVar()

Name = Entry(root2, textvariable=name, font=('arial', 15, 'bold'), width=12)
Name.grid(row=1, column=1, padx=7, pady=7)

Price = Entry(root2, textvariable=price, font=('arial', 15, 'bold'), width=12)
Price.grid(row=2, column=1, padx=7, pady=7)

Qty = Entry(root2, textvariable=qty, font=('arial', 15, 'bold'), width=12)
Qty.grid(row=3, column=1, padx=7, pady=7)

addbtn = Button(root2, command=addStock, text="Add",
                font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

addbtn.grid(row=4, column=1, padx=7, pady=7)

viewarea2 = Text(root2)
viewarea2.grid(row=5, column=0, columnspan=2)

viewbtn2 = Button(root2, command=viewStock, text="View Stock",
                  font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

viewbtn2.grid(row=4, column=0, padx=7, pady=7)

mainloop()