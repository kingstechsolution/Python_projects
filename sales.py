from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import os

class Sales:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x630+220+150")
        self.root.title("SMK Inventory Management System  |  Developed By Dreams-Tech Solutions")
        self.root.config(bg="white")
        self.root.focus_force()

        self.txn_list = []
        self.var_invoice = StringVar()

        # ==========Title=============
        lab_title = Label(self.root, text="View Sales Invoice", font=("times new roman", 25, "bold"), bd=3,relief=RIDGE, bg="#184a45", fg="#ffffff")
        lab_title.pack(side=TOP, fill=X, padx=10, pady=20)

        lab_invoice = Label(self.root, text="Invoice No.", font=("times new roman",15), bg="white")
        lab_invoice.place(x=50, y=100)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 13), bg="lightyellow")
        txt_invoice.place(x=160, y=100, width=200, height=28)

        # =======_Search Button Image_==========
        icon = Image.open(r"images/search2.png")
        icon = icon.resize((23, 19), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(icon)
        search_btn = Button(self.root, text="Search", command= self.search, font=("times new roman", 13, "bold"),image=self.photo, padx=8, cursor="hand2", compound=LEFT, anchor="e", bg="#2196f3",fg="white")
        search_btn.place(x=375, y=100, width=98)

        icon1 = Image.open(r"images/clear.png")
        icon1 = icon1.resize((23, 19), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(icon1)
        search_btn = Button(self.root, text="Clear", command= self.clear, font=("times new roman", 13, "bold"), image=self.photo1, padx=8,cursor="hand2", compound=LEFT, anchor="e", bg="lightgray")
        search_btn.place(x=490, y=100, width=98)

        # =========== Sales List =============
        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=400)

        scrolly=Scrollbar(sales_frame, orient=VERTICAL)
        self.Sales_list = Listbox(sales_frame, font=("times new roman", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH, expand=1)
        self.Sales_list.bind("<ButtonRelease-1>", self.get_data)

        # =========== Transaction Area =============
        txn_frame = Frame(self.root, bd=3, relief=RIDGE)
        txn_frame.place(x=280, y=140, width=420, height=400)

        lab_title2 = Label(txn_frame, text="Customer Transaction Window", font=("times new roman", 15, "bold"), bg="orange")
        lab_title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(txn_frame, orient=VERTICAL)
        self.txn_area = Text(txn_frame, bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.txn_area.yview)
        self.txn_area.pack(fill=BOTH, expand=1)

        # ==========_Left_Floating_Image_===========
        self.txn_photo = Image.open(r"images/sup3.jpg")
        self.txn_photo = self.txn_photo.resize((600, 400), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(self.txn_photo)

        lab_image = Label(self.root, text="Employee", image=self.photoimg2, bd=0)
        lab_image.place(x=700, y=110)

        self.show()
# ===============================================================
    def show(self):
        del self.txn_list[:]
        self.Sales_list.delete(0, END)
    #   print(os.listdir('../Inventory Management System')) Transaction1.txt, Category.py
        for i in os.listdir('Sales Transactions'):
            if i.split('.') [-1] == "txt":
                self.Sales_list.insert(END, i)
                self.txn_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.Sales_list.curselection()
        file_name = self.Sales_list.get(index_)
        print(file_name)
        self.txn_area.delete('1.0', END)
        fp = open(f'Sales Transactions/{file_name}', 'r')
        for i in fp:
            self.txn_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice ID is required", parent = self.root)
        else:
            if self.var_invoice.get() in self.txn_list:
                fp = open(f'Sales Transactions/{self.var_invoice.get()}.txt','r')
                self.txn_area.delete('1.0', END)
                for i in fp:
                    self.txn_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invoice ID not found", parent = self.root)

    def clear(self):
        self.show()
        self.txn_area.delete('1.0', END)


if __name__ == "__main__":
    root = Tk()
    obj = Sales(root)
    root.mainloop()