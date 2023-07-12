import sqlite3
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox, ttk
import time
import os
import tempfile


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("SMK Inventory Management System  |  Developed By Dreams-Tech Solutions")
        self.root.config(bg="ghostwhite")
        self.cart_list = []
        self.check_print = 0


        # =======_Title_=========
        img1 = Image.open(r"images/logo1.png")
        img1 = img1.resize((80, 55), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        title = Label(self.root, text="Inventory Management System", image=self.photoimg1, compound=LEFT,
                      font=("times new roman", 35, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # ========_Logout Button_==========
        imgLB = Image.open(r"images/logout.png")
        imgLB = imgLB.resize((18, 18), Image.LANCZOS)
        self.photoimgLB = ImageTk.PhotoImage(imgLB)
        logout_btn = Button(self.root, command=self.logout, text="Logout", image=self.photoimgLB, compound=RIGHT, anchor="e",
                            font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2", width=80)
        logout_btn.place(x=1350, y=15)

        # ========_Date & Time Bar_==========
        self.clock_label = Label(self.root,
                                 text="Super Marche Kado Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: "
                                      "HH:MM:SS",
                                 font=("Anton", 15), bg="#4d636d", fg="white")
        self.clock_label.place(x=0, y=70, relwidth=1, height=40)

        # =========== Product Frame ==============
        product_frame1 = Frame(self.root, relief=RIDGE, bd=4, bg="white")
        product_frame1.place(x=10, y=120, width=460, height=620)

        pTitle = Label(product_frame1, text="All Products", font=("times new roman", 20, "bold"), bg="#262626", fg="white")
        pTitle.pack(side=TOP, fill=X)

        # ============_Product Search Frame_================
        self.var_search = StringVar()
        product_frame2 = Frame(product_frame1, relief=RIDGE, bd=2, bg="white")
        product_frame2.place(x=4, y=40, width=445, height=90)

        lab_search = Label(product_frame2, text="Search Product | By Name", font=("times new roman", 15, "bold"), bg="white", fg="green")
        lab_search.place(x=2, y=5)

        txt_search = Entry(product_frame2, textvariable=self.var_search, font=("times new roman", 15), bg="lightyellow")
        txt_search.place(x=133, y=50, width=200, height=22)

        # =======_Search Button Image_==========
        icon = Image.open(r"images/search2.png")
        icon = icon.resize((23, 19), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(icon)
        search_btn = Button(product_frame2, text="Search", command=self.search, font=("times new roman", 13, "bold"),
                            image=self.photo, padx=8, cursor="hand2", compound=LEFT, anchor="e", bg="#2196f3", fg="white")
        search_btn.place(x=340, y=45, width=95)

        # =======_Show Button Image_==========
        icon1 = Image.open(r"images/search.png")
        icon1 = icon1.resize((23, 19), Image.LANCZOS)
        self.photo12 = ImageTk.PhotoImage(icon1)
        show_btn = Button(product_frame2, text="Show All", command=self.show_data, font=("times new roman", 13, "bold"),
                            image=self.photo12, padx=8, cursor="hand2", compound=LEFT, anchor="e", bg="#083531",fg="white")
        show_btn.place(x=315, y=10, width=120)

        lab_name = Label(product_frame2, text="Product Name", font=("times new roman", 15, "bold"), bg="white")
        lab_name.place(x=5, y=45)

        # ============_Product Details Frame_================
        product_frame3 = Frame(product_frame1, bd=3, relief=RIDGE)
        product_frame3.place(x=2, y=145, width=450, height=440)

        scroll_y = Scrollbar(product_frame3, orient=VERTICAL)
        scroll_x = Scrollbar(product_frame3, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(product_frame3, columns=("pid", "name", "price", "qty", "status"),
                                       yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="PID")
        self.product_table.heading("name", text="Product Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=50)
        self.product_table.column("name", width=180)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=80)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        lab_note = Label(product_frame1, text="Note: 'Enter 0 Quantity to Remove Product From Cart'",
                         font=("times new roman", 12), anchor='w', bg="white", fg="red")
        lab_note.pack(side=BOTTOM, fill=X)

        # =========== Client Frame ==============
        self.var_cname = StringVar()
        self.var_contact = StringVar()

        client_frame = Frame(self.root, relief=RIDGE, bd=4, bg="white")
        client_frame.place(x=475, y=120, width=580, height=70)

        cTitle = Label(client_frame, text="Customer Details", font=("times new roman", 15), bg="goldenrod", fg="black")
        cTitle.pack(side=TOP, fill=X)

        lab_name = Label(client_frame, text="Name:", font=("times new roman", 15), bg="white")
        lab_name.place(x=5, y=35)

        txt_name = Entry(client_frame, textvariable=self.var_cname, font=("times new roman", 13), bg="lightyellow")
        txt_name.place(x=70, y=35, width=180)

        lab_contact = Label(client_frame, text="Contact:", font=("times new roman", 15), bg="white")
        lab_contact.place(x=280, y=35)

        txt_contact = Entry(client_frame, textvariable=self.var_contact, font=("times new roman", 15), bg="lightyellow")
        txt_contact.place(x=360, y=33, width=150)

        # =========== Cal Cart Frame ==============
        cart_calc_frame = Frame(self.root, relief=RIDGE, bd=2, bg="white")
        cart_calc_frame.place(x=475, y=200, width=580, height=400)

        # =========== Calculator Frame ==============
        self.var_cal_input = StringVar()
        cal_frame = Frame(cart_calc_frame, relief=RIDGE, bd=9, bg="grey")
        cal_frame.place(x=3, y=10, width=323, height=380)

        self.txt_cal_input = Entry(cart_calc_frame, textvariable=self.var_cal_input, font=("times new roman", 15, "bold"), width=31, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        self.txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(cart_calc_frame,text="7", command=lambda: self.get_input(7), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=4, cursor="hand2")
        btn_7.grid(row=1, column=0)

        btn_8 = Button(cart_calc_frame, text="8", command=lambda: self.get_input(8), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=8, cursor="hand2")
        btn_8.grid(row=1, column=1)

        btn_9 = Button(cart_calc_frame, text="9", command=lambda: self.get_input(9), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=8, cursor="hand2")
        btn_9.grid(row=1, column=2)

        btn_sum = Button(cart_calc_frame, text="+", command=lambda: self.get_input("+"), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=4, cursor="hand2")
        btn_sum.grid(row=1, column=3)

        btn_4 = Button(cart_calc_frame, text="4", command=lambda: self.get_input(4), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=4,
                       cursor="hand2")
        btn_4.grid(row=2, column=0)

        btn_5 = Button(cart_calc_frame, text="5", command=lambda: self.get_input(5), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=8,
                       cursor="hand2")
        btn_5.grid(row=2, column=1)

        btn_6 = Button(cart_calc_frame, text="6", command=lambda: self.get_input(6), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=8,
                       cursor="hand2")
        btn_6.grid(row=2, column=2)

        btn_minus = Button(cart_calc_frame, text="-", command=lambda: self.get_input("-"), font=("arial", 15, "bold"), bd=5, width=4, pady=18, padx=4,
                         cursor="hand2")
        btn_minus.grid(row=2, column=3)

        btn_1 = Button(cart_calc_frame, text="1", command=lambda: self.get_input(1), font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=4,
                       cursor="hand2")
        btn_1.grid(row=3, column=0)

        btn_2 = Button(cart_calc_frame, text="2", command=lambda: self.get_input(2), font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=8,
                       cursor="hand2")
        btn_2.grid(row=3, column=1)

        btn_3 = Button(cart_calc_frame, text="3", command=lambda: self.get_input(3), font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=8,
                       cursor="hand2")
        btn_3.grid(row=3, column=2)

        btn_mul = Button(cart_calc_frame, text="x", command=lambda: self.get_input("*"), font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=4,
                           cursor="hand2")
        btn_mul.grid(row=3, column=3)

        btn_0 = Button(cart_calc_frame, text="0", command=lambda: self.get_input(0), font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=4,
                       cursor="hand2")
        btn_0.grid(row=4, column=0)

        btn_c = Button(cart_calc_frame, text="C", command=self.clear, font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=8,
                       cursor="hand2")
        btn_c.grid(row=4, column=1)

        btn_eq = Button(cart_calc_frame, text="=", command=self.perform_calc, font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=8,
                       cursor="hand2")
        btn_eq.grid(row=4, column=2)

        btn_div = Button(cart_calc_frame, text="/", command=lambda: self.get_input("/"), font=("arial", 15, "bold"), bd=5, width=4, pady=20, padx=4,
                         cursor="hand2")
        btn_div.grid(row=4, column=3)

        # ============_Cart Frame_================
        cart_frame = Frame(cart_calc_frame, bd=3, relief=RIDGE)
        cart_frame.place(x=330, y=8, width=245, height=380)

        self.cart_Title = Label(cart_frame, text="Cart \t Total Products: [0]", font=("times new roman", 15), bg="goldenrod", fg="black")
        self.cart_Title.pack(side=TOP, fill=X)

        scroll_y = Scrollbar(cart_frame, orient=VERTICAL)
        scroll_x = Scrollbar(cart_frame, orient=HORIZONTAL)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"),
                                       yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cart_table.xview)
        scroll_y.config(command=self.cart_table.yview)

        self.cart_table.heading("pid", text="PID")
        self.cart_table.heading("name", text="Product")
        self.cart_table.heading("price", text="Price")
        self.cart_table.heading("qty", text="Qty")

        self.cart_table["show"] = "headings"

        self.cart_table.column("pid", width=40)
        self.cart_table.column("name", width=120)
        self.cart_table.column("price", width=100)
        self.cart_table.column("qty", width=40)
        self.cart_table.pack(fill=BOTH, expand=1)
        self.cart_table.bind("<ButtonRelease-1>", self.get_cart_data)

        # ============_Cart Widgets Frame_================
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        cart_widget_frame = Frame(self.root, relief=RIDGE, bd=2, bg="white")
        cart_widget_frame.place(x=475, y=600, width=580, height=140)

        lab_p_name = Label(cart_widget_frame, text="Product Name", font=("times new roman", 15), bg="white")
        lab_p_name.place(x=5, y=5)
        txt_p_name = Entry(cart_widget_frame, textvariable=self.var_pname, font=("times new roman", 15), bg="light yellow", state="readonly")
        txt_p_name.place(x=5, y=35, width=270, height=22)

        lab_p_price = Label(cart_widget_frame, text="Price Per Qty", font=("times new roman", 15), bg="white")
        lab_p_price.place(x=290, y=5)
        txt_p_name = Entry(cart_widget_frame, textvariable=self.var_price, font=("times new roman", 15),bg="light yellow", state="readonly")
        txt_p_name.place(x=290, y=35, width=150, height=22)

        lab_p_qty = Label(cart_widget_frame, text="Quantity", font=("times new roman", 15), bg="white")
        lab_p_qty.place(x=460, y=5)
        txt_p_qty = Entry(cart_widget_frame, textvariable=self.var_qty, font=("times new roman", 15),bg="light yellow")
        txt_p_qty.place(x=460, y=35, width=100, height=22)

        self.lab_instock = Label(cart_widget_frame, text="In Stock", font=("times new roman", 15), bg="white")
        self.lab_instock.place(x=35, y=85)

        # =======_Clear Button Image_==========
        icon5 = Image.open(r"images/clear.png")
        icon5 = icon5.resize((23, 19), Image.LANCZOS)
        self.photo5 = ImageTk.PhotoImage(icon5)
        show_btn = Button(cart_widget_frame, text="Clear", command=self.clear_cart, font=("times new roman", 13, "bold"),
                          image=self.photo5, padx=8, cursor="hand2", compound=LEFT, bg="#40b5ad", fg="black")
        show_btn.place(x=200, y=85, width=120, height=40)

        # =======_Add & Update Button Image_==========
        icon6 = Image.open(r"images/update.png")
        icon6 = icon6.resize((23, 19), Image.LANCZOS)
        self.photo6 = ImageTk.PhotoImage(icon6)
        show_btn = Button(cart_widget_frame, text="Add | Update", command=self.add_update_cart, font=("times new roman", 13, "bold"),
                          image=self.photo6, padx=8, cursor="hand2", compound=LEFT, bg="slategrey", fg="white")
        show_btn.place(x=340, y=85, width=170, height=40)

        # =============_Billing Area_===============
        billFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        billFrame.place(x=1060, y=120, width=460, height=470)

        bTitle = Label(billFrame, text="Customer Bill Area", font=("times new roman", 20, "bold"), bg="#262626", fg="white")
        bTitle.pack(side=TOP, fill=X)

        scroll_y = Scrollbar(billFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(billFrame, yscrollcommand=scroll_y.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_bill_area.yview)

        # ===============_Billing Label Frame_==================
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        billMenuFrame.place(x=1060, y=595, width=460, height=145)

        self.lbl_amt = Label(billMenuFrame, text="Bill Amount\n[0]", font=("times new roman", 14, "bold"), bg="#3f51b5", fg="white")
        self.lbl_amt.place(x=6, y=5, width=160, height=70)

        self.bill_discount = Label(billMenuFrame, text="Discount \n[5%]", font=("times new roman", 15, "bold"), bg="#8bc34a", fg="white")
        self.bill_discount.place(x=170, y=5, width=120, height=70)

        self.bill_net_pay = Label(billMenuFrame, text="Net Pay\n[0]", font=("times new roman", 14, "bold"), bg="#607d8b", fg="white")
        self.bill_net_pay.place(x=295, y=5, width=160, height=70)

        # =======_Print Bill Button & Image_==========
        iconP = Image.open(r"images/save.png")
        iconP = iconP.resize((23, 19), Image.LANCZOS)
        self.photoP = ImageTk.PhotoImage(iconP)
        print_btn = Button(billMenuFrame, text="Print", command=self.print_bill, font=("times new roman", 13, "bold"),
                          image=self.photoP, padx=8, cursor="hand2", compound=LEFT, bg="lightgrey", fg="black")
        print_btn.place(x=10, y=80, width=120, height=50)

        # =======_Clear All Button & Image_==========
        iconC = Image.open(r"images/clear.png")
        iconC = iconC.resize((23, 19), Image.LANCZOS)
        self.photoC = ImageTk.PhotoImage(iconC)
        clearAll_btn = Button(billMenuFrame, text="Clear All", command=self.clear_all, font=("times new roman", 13, "bold"),
                          image=self.photoC, padx=8, cursor="hand2", compound=LEFT, bg="lightgrey", fg="black")
        clearAll_btn.place(x=144, y=80, width=140, height=50)

        # =======_Generate Bill Button & Image_==========
        iconG = Image.open(r"images/update.png")
        iconG = iconG.resize((23, 19), Image.LANCZOS)
        self.photoG = ImageTk.PhotoImage(iconG)
        generate_btn = Button(billMenuFrame, text="Generate\nInvoice", command=self.generate_bill, font=("times new roman", 13, "bold"),
                          image=self.photoG, padx=8, cursor="hand2", compound=LEFT, bg="lightgrey", fg="black")
        generate_btn.place(x=296, y=80, width=150, height=50)

        # ========_Footer_==========
        footer = Label(self.root, text="Super Marche Kado - Inventory Management System | "
                                       "Developed by Dreams-Tech Solutions\n Technical Issue Contact: 680-305-815",
                       font=("times nw roman", 10, "bold"), bg="#4d636d", fg="white", height=3)
        footer.pack(side=BOTTOM, fill=X)
        self.show_data()
        #self.bill_top()
        self.update_date_time()





# ==============================_All Functions_================================

    def get_input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear(self):
        self.var_cal_input.set("")

    def perform_calc(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    # ==============_This displays the database data in the columns in the user interface_========================
    def show_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            cur.execute("select pid,product,price,quantity,status from product where status='Active'")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # ==============_Search System Function_========================
    def search(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Search Error", "Search Input Text Required", parent=self.root)
            else:
                cur.execute(
                    "select pid,product,price,quantity,status from product where product LIKE '%"+self.var_search.get() + "%' and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Search Error", "No Record Found!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Search Error", f"Error due to : {str(ex)}", parent=self.root)

    # ==============_Get Product Table Data_========================
    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lab_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    # ==============_Get Cart Table Data_========================
    def get_cart_data(self, ev):
        f = self.cart_table.focus()
        content = (self.cart_table.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_pname.set(row[1]),
        self.var_price.set(row[2]),
        self.var_qty.set(row[3]),
        self.lab_instock.config(text=f"In Stock [{str(row[4])}]"),
        self.var_stock.set(row[4])


    # ==============_Add/Update Button Function_========================
    def add_update_cart(self):
        if self.var_pid.get() == "":
            messagebox.showerror("Error", "Please select product from list", parent=self.root)
        elif self.var_qty.get() == "":
            messagebox.showerror("Error", "Enter Quantity", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)
        else:
            #price_cal = int(self.var_qty.get()) * float(self.var_price.get())
            #price_cal = float(price_cal)
            price_cal = self.var_price.get()
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(), self.var_stock.get()]
            # Update Cart
            present = "no"
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = "yes"
                    break
                index_ += 1
            if present == "yes":
                op = messagebox.askyesno("Confirmation", "Product already exist in cart\nDo you want to Update| Remove product from Cart List?", parent=self.root)
                if op == True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2] = price_cal # price
                        self.cart_list[index_][3] = self.var_qty.get()  # quantity
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amt = self.bill_amt + (float(row[2]) * int(row[3]))

        self.discount = (self.bill_amt * 5)/100
        self.net_pay = self.bill_amt - self.discount
        self.lbl_amt.config(text=f"Bill Amount(XAF)\n{str(self.bill_amt)}")
        self.bill_net_pay.config(text=f"Net Pay(XAF)\n{str(self.net_pay)}")
        self.cart_Title.config(text=f"Cart \t Total Products: [{str(len(self.cart_list))}]")


    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def generate_bill(self):
        if self.var_cname.get() == "" or self.var_contact.get() == "":
            messagebox.showerror("Error", f"Customer Details Required", parent=self.root)
        elif len(self.cart_list) ==0:
            messagebox.showerror("Error", f"Please add product to cart!!")
        else:
            # Bill Top
            self.bill_top()
            # Bill Middle
            self.bill_middle()
            # Bill Bottom
            self.bill_bottom()

            fp = open(f'Sales Transactions/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo("Invoice Saved", "Invoice has been generated successfully", parent=self.root)
            self.check_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\tSuper Marche Kado Bonapriso.
\tPhone No. 680-305-815, Douala, Cameroon.
{str("=" *47)}
Customer Name: {self.var_cname.get()}
Telephone No.: {self.var_contact.get()}
Invoice No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("=" *47)}
 Product Name\t\t\tQty\tPrice
{str("=" *47)} 
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_middle(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                qty = int(row[4]) - int(row[3])
                if int(row[3]) == int(row[4]):
                    status = 'Out of Stock'
                if int(row[3]) != int(row[4]):
                    status = 'Active'

                price = float(row[2]) * int(row[3])
                price = str(price)
                self.txt_bill_area.insert(END, "\n "+name+"\t\t\t"+row[3]+"\tXAF."+price)
                #===========Update qty in product table==============
                cur.execute("Update product set quantity=?, status=? where pid=?", (
                    qty,
                    status,
                    pid
                ))
                conn.commit()
            conn.close()
            self.show_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("=" *47)}
Bill Amount\t\t\t\tXAF.{self.bill_amt}
Discount\t\t\t\tXAF.{self.discount}
Net Pay\t\t\t        XAF.{self.net_pay}
{str("=" *47)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def clear_cart(self):
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.lab_instock.config(text=f"In Stock")
        self.var_stock.set("")

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete('1.0', END)
        self.cart_Title.config(text=f"Cart \t Total Products: [0]")
        self.check_print = 0
        self.var_search.set("")
        self.clear_cart()
        self.show_data()
        self.show_cart()

    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.clock_label.config(text=f"Super Marche Kado Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.clock_label.after(200, self.update_date_time)

    def print_bill(self):
        if self.check_print == 1:
            messagebox.showinfo("Invoice Printer", "Please wait while invoice is being printed...", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror("Invoice Printer", "Kindly generate invoice before printing receipt", parent=self.root)

    def logout(self):
        if messagebox.askyesno("Confirmation Message", "Do you want to Logout?") == YES:
            self.root.destroy()
            os.system("python login.py")
        else:
            return messagebox.showinfo("Welcome Message", "Welcome Back!")




if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()