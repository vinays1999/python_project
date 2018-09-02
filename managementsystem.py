from tkinter import *
import time
import datetime
from tkinter import Tk
import csv
import os

root = Tk()
root.geometry("1600x1000+1+1")
root.title("Management System")

Tops = Frame(root, width=1600, height=100, relief=SUNKEN)
Tops.pack(side=TOP)
Left = Frame(root, width=750, height=950, relief=SUNKEN)
Left.pack(side=LEFT)
Right = Frame(root, width=790, height=950, relief=SUNKEN)
Right.pack(side=RIGHT)

# ================================TOP==============================

localtime = time.asctime(time.localtime(time.time()))

lblnfo = Label(Tops, font=('arial', 45, 'bold'), text="Management System", fg="black", bd=10, anchor='w')
lblnfo.grid(row=0, column=0)
lbltime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="steel blue", bd=10, anchor='w')
lbltime.grid(row=1, column=0)

# ================================LEFT=============================

v = StringVar()
c_name = StringVar()
r_name = StringVar()
item = StringVar()
weight = StringVar()
price = StringVar()
interest = StringVar()
gs = StringVar()
dd = IntVar()
dd.set("dd")
mm = IntVar()
mm.set("mm")
yyyy = IntVar()
yyyy.set('yyyy')

TF = os.path.exists('data.csv')

if TF == False:
    with open('data.csv', 'w') as csvfile:
        fieldname = ['name', 'Rname', 'date', 'G/S', 'item', 'weight', 'price', 'interest']
        filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldname)
        filewriter.writeheader()


def radiofunc():
    gs.set(v.get())


def submit():
    name = c_name.get()
    Rname = r_name.get()
    gs_gs = gs.get()
    gs_item = item.get()
    gs_wgt = weight.get()
    gs_pr = price.get()
    gs_int = interest.get()
    day = int(dd.get())
    month = int(mm.get())
    year = int(yyyy.get())

    date = datetime.date(year, month, day)

    with open('data.csv', 'a') as csvfile:
        fieldname = ['name', 'Rname', 'date', 'G/S', 'item', 'weight', 'price', 'interest']
        appand_data = csv.DictWriter(csvfile, fieldnames=fieldname, delimiter=',')
        appand_data.writerow({'name': name,
                              'Rname': Rname,
                              'date': date,
                              'G/S': gs_gs,
                              'item': gs_item,
                              'weight': gs_wgt,
                              'price': gs_pr,
                              'interest': gs_int
                              })

    c_name.set('')
    r_name.set("")
    item.set("")
    weight.set("")
    price.set("")
    interest.set("")
    gs.set("")
    dd.set("dd")
    mm.set("mm")
    yyyy.set("yyyy")


lblname = Label(Left, font=('arial', 25, 'bold'), text="Name", fg="black", bd=10, anchor='w')
lblname.grid(row=0, column=0)
entryname = Entry(Left, font=('arial', 20, 'bold'), textvariable=c_name, fg="black", bd=6)
entryname.grid(row=0, column=1, columnspan=4)

lblreference = Label(Left, font=('arial', 25, 'bold'), text="Reference", fg="black", bd=10, anchor='w')
lblreference.grid(row=1, column=0)
entryreference = Entry(Left, font=('arial', 20, 'bold'), textvariable=r_name, fg="black", bd=6)
entryreference.grid(row=1, column=1, columnspan=4)

lbldate = Label(Left, font=('arial', 25, 'bold'), text="Date", fg="black", bd=10, anchor='w')
lbldate.grid(row=2, column=0)
entrydd = Entry(Left, font=('arial', 20, 'bold'), textvariable=dd, fg="black", width=5, bd=6)
entrydd.grid(row=2, column=1)
entrymm = Entry(Left, font=('arial', 20, 'bold'), textvariable=mm, fg="black", width=5, bd=6)
entrymm.grid(row=2, column=3)
entryyyy = Entry(Left, font=('arial', 20, 'bold'), textvariable=yyyy, fg="black", width=5, bd=6)
entryyyy.grid(row=2, column=4)

lblitem = Label(Left, font=('arial', 25, 'bold'), text="Item", fg="black", bd=10, anchor='w')
lblitem.grid(row=3, column=0)
entryitem = Entry(Left, font=('arial', 20, 'bold'), textvariable=item, width=6, fg="black", bd=6)
entryitem.grid(row=3, column=1)

goldbutton = Radiobutton(Left, variable=v, font=('arial', 20, 'bold'), value='GOLD', text='Gold', width=5,
                         command=radiofunc) \
    .grid(row=3, column=3)
silverbutton = Radiobutton(Left, variable=v, font=('arial', 20, 'bold'), value='SILVER', text='Silver', width=5,
                           command=radiofunc).grid(row=3, column=4)

lblweight = Label(Left, font=('arial', 25, 'bold'), text="weight", fg="black", bd=10, anchor='w')
lblweight.grid(row=4, column=0)
entryweight = Entry(Left, font=('arial', 20, 'bold'), textvariable=weight, fg="black", bd=6)
entryweight.grid(row=4, column=1, columnspan=4)

lblprice = Label(Left, font=('arial', 25, 'bold'), text="Price", fg="black", bd=10, anchor='w')
lblprice.grid(row=5, column=0)
entryprice = Entry(Left, font=('arial', 20, 'bold'), textvariable=price, fg="black", bd=6)
entryprice.grid(row=5, column=1, columnspan=4)

lblinterest = Label(Left, font=('arial', 25, 'bold'), text="Interest", fg="black", bd=10, anchor='w')
lblinterest.grid(row=6, column=0)
entryinterest = Entry(Left, font=('arial', 20, 'bold'), textvariable=interest, fg="black", bd=6)
entryinterest.grid(row=6, column=1, columnspan=4)

btnsubmit = Button(Left, padx=10, pady=10, bd=6, fg="black", font=('arial', 25, 'bold'), text="SUBMIT",
                   command=submit, bg="powder blue").grid(row=8, column=1)

# =====================================RIGHT============================================

s = StringVar()
search_name = str()
search_rname = StringVar()
searchrname = StringVar()
smm = StringVar()
syyyy = StringVar()
searchdate = StringVar()
srchitem = StringVar()
radiosearch = StringVar()
sitem = StringVar()


def searchname():
    TF = os.path.exists(search_name + '.csv')

    if not TF:
        with open(search_name + '.csv', 'w') as csvnew:
            csv.writer(csvnew)

            fieldname = ['name', 'Rname', 'date', 'G/S', 'item', 'weight', 'price', 'interest']
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writeheader()


    with open('data.csv', 'r') as csvf:
        sname = csv.reader(csvf)
        with open(search_name + '.csv', 'a') as csvnew:
            wname = csv.writer(csvnew,delimeter=',')
            for n in sname:
                if n[0] == search_name:
                    wname.writerow(n)


lblsname = Label(Right, font=('arial', 25, 'bold'), text="Name", fg="black", bd=10, anchor='w')
lblsname.grid(row=0, column=0)
entrysname = Entry(Right, font=('arial', 20, 'bold'), textvariable=search_name, fg="black", bd=6)
entrysname.grid(row=0, column=1, columnspan=3)
btnsname = Button(Right, padx=10, pady=7, bd=6, fg="black", font=('arial', 12, 'bold'), text="SEARCH",
                  command=searchname, bg="powder blue").grid(row=0, column=4)

lblsrname = Label(Right, font=('arial', 25, 'bold'), text="Reference", fg="black", bd=10, anchor='w')
lblsrname.grid(row=1, column=0)
entrysrname = Entry(Right, font=('arial', 20, 'bold'), textvariable=search_rname, fg="black", bd=6)
entrysrname.grid(row=1, column=1, columnspan=3)
btnsrname = Button(Right, padx=10, pady=7, bd=6, fg="black", font=('arial', 12, 'bold'), text="SEARCH",
                   command=searchrname, bg="powder blue").grid(row=1, column=4)

lblsdate = Label(Right, font=('arial', 25, 'bold'), text="date", fg="black", bd=10, anchor='w')
lblsdate.grid(row=2, column=0)
entrysmm = Entry(Right, font=('arial', 20, 'bold'), textvariable=smm, fg="black", width=8, bd=6)
entrysmm.grid(row=2, column=1)
entrsyyyy = Entry(Right, font=('arial', 20, 'bold'), textvariable=syyyy, fg="black", width=8, bd=6)
entrsyyyy.grid(row=2, column=2)
btnsdate = Button(Right, padx=10, pady=7, bd=6, fg="black", font=('arial', 12, 'bold'), text="SEARCH",
                  command=searchdate, bg="powder blue").grid(row=2, column=4)

lblitem = Label(Right, font=('arial', 25, 'bold'), text="Item", fg="black", bd=10, anchor='w')
lblitem.grid(row=3, column=0)
entryitem = Entry(Right, font=('arial', 20, 'bold'), textvariable=sitem, width=6, fg="black", bd=6)
entryitem.grid(row=3, column=1)
goldsbutton = Radiobutton(Right, variable=s, font=('arial', 20, 'bold'), value='GOLD', text='Gold', width=5,
                          command=radiosearch).grid(row=3, column=2)
silversbutton = Radiobutton(Right, variable=s, font=('arial', 20, 'bold'), value='SILVER', text='Silver', width=5,
                            command=radiofunc).grid(row=3, column=3)
btnsname = Button(Right, padx=10, pady=7, bd=6, fg="black", font=('arial', 12, 'bold'), text="SEARCH",
                  command=srchitem, bg="powder blue").grid(row=3, column=4)

# ======================================CLOSE============================================
root.mainloop()
