from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class Product:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x630+220+150")
        self.root.title("SMK Inventory Management System  |  Developed By Dreams-Tech Solutions")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==============_Variables_===============
        # ========_Form Entries_=========
        self.var_pid = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_category_sup()

        self.var_product = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_status = StringVar()

        # ======_Search Bar_==========
        self.var_searchBy = StringVar()
        self.var_searchTxt = StringVar()

        product_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=10, width=500, height=600)

        # ========_Title_=========
        title = Label(product_frame, text="Manage Product Details", font=("times new roman", 20, "bold"), bd=3,relief=RIDGE, bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        # ========_Column 1_=========
        lab_category = Label(product_frame, text="Category:", font=("times new roman", 18, "bold"), bg="white")
        lab_category.place(x=30, y=60)

        lab_supplier = Label(product_frame, text="Supplier:", font=("times new roman", 18, "bold"), bg="white")
        lab_supplier.place(x=30, y=110)

        lab_product = Label(product_frame, text="Product:", font=("times new roman", 18, "bold"), bg="white")
        lab_product.place(x=30, y=160)

        lab_price = Label(product_frame, text="Price:", font=("times new roman", 18, "bold"), bg="white")
        lab_price.place(x=30, y=210)

        lab_quantity = Label(product_frame, text="Quantity:", font=("times new roman", 18, "bold"), bg="white")
        lab_quantity.place(x=30, y=260)

        lab_status = Label(product_frame, text="Status:", font=("times new roman", 18, "bold"), bg="white")
        lab_status.place(x=30, y=310)

        # =========_Column 2_===========
        combo_category = ttk.Combobox(product_frame, textvariable=self.var_category, values=self.cat_list, state="readonly",justify=CENTER, font=("times new roman", 15))
        combo_category.place(x=180, y=64, width=240)
        combo_category.current(0)

        combo_supplier = ttk.Combobox(product_frame, textvariable=self.var_supplier, values=self.sup_list, state="readonly", justify=CENTER, font=("times new roman", 15))
        combo_supplier.place(x=180, y=114, width=240)
        combo_supplier.current(0)

        txt_product = Entry(self.root, textvariable=self.var_product, font=("times new roman", 17), bg="lightyellow")
        txt_product.place(x=190, y=177, width=245)

        txt_price = Entry(self.root, textvariable=self.var_price, font=("times new roman", 17), bg="lightyellow")
        txt_price.place(x=190, y=227, width=245)

        txt_quantity = Entry(self.root, textvariable=self.var_quantity, font=("times new roman", 17), bg="lightyellow")
        txt_quantity.place(x=190, y=277, width=245)

        combo_status = ttk.Combobox(product_frame, textvariable=self.var_status, values=("Active", "Out of Stock"), state="readonly", justify=CENTER, font=("times new roman", 15))
        combo_status.place(x=180, y=315, width=240)
        combo_status.current(0)

        # ===========_CRUD Functions Buttons_============
        save = Image.open(r"images/save.png")
        save = save.resize((23, 19), Image.LANCZOS)
        self.save = ImageTk.PhotoImage(save)
        save_btn = Button(product_frame, text="Save", command=self.save_data, font=("times new roman", 13, "bold"), image=self.save, padx=8, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        save_btn.place(x=20, y=380)

        update = Image.open(r"images/update.png")
        update = update.resize((23, 19), Image.LANCZOS)
        self.update = ImageTk.PhotoImage(update)
        update_btn = Button(product_frame, text="Update", command=self.update_data, font=("times new roman", 13, "bold"),image=self.update, padx=4, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        update_btn.place(x=120, y=380, width=95)

        delete = Image.open(r"images/delete.png")
        delete = delete.resize((23, 19), Image.LANCZOS)
        self.delete = ImageTk.PhotoImage(delete)
        delete_btn = Button(product_frame, text="Delete", command=self.delete_data, font=("times new roman", 13, "bold"),image=self.delete, padx=4, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        delete_btn.place(x=230, y=380, width=95)

        clear = Image.open(r"images/clear.png")
        clear = clear.resize((23, 19), Image.LANCZOS)
        self.clear = ImageTk.PhotoImage(clear)
        clear_btn = Button(product_frame, text="Clear", command=self.clear_data, font=("times new roman", 13, "bold"),image=self.clear, padx=6, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        clear_btn.place(x=340, y=380, width=85)

        # ==========_Search Frame_==========
        searchframe = LabelFrame(self.root, text="Search Products", bg="white", font=("times new roman", 15, "bold"),bd=2, relief=RIDGE)
        searchframe.place(x=525, y=10, width=550, height=73)

        # ========_Options_=========
        combo_search = ttk.Combobox(searchframe, textvariable=self.var_searchBy,values=("Select", "Category", "Supplier", "Product"), state="readonly", justify=CENTER, font=("times new roman", 15))
        combo_search.place(x=10, y=5, width=180)
        combo_search.current(0)

        text_search = Entry(searchframe, textvariable=self.var_searchTxt, font=("yu gothic ui", 15), bg="lightyellow")
        text_search.place(x=200, y=4)

        # =======_Search Button Image_==========
        icon = Image.open(r"images/search2.png")
        icon = icon.resize((23, 19), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(icon)
        search_btn = Button(searchframe, text="Search", command=self.search, font=("times new roman", 13, "bold"),image=self.photo, padx=8, cursor="hand2", compound=LEFT, anchor="e", bg="#40b5ad",fg="white")
        search_btn.place(x=440, y=4, width=100)

        # =============Product Details View Table_==============
        prod_frame = Frame(self.root, bd=3, relief=RIDGE)
        prod_frame.place(x=520, y=100, width=555, height=510)

        scroll_y = Scrollbar(prod_frame, orient=VERTICAL)
        scroll_x = Scrollbar(prod_frame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(prod_frame, columns=("pid", "category", "supplier", "product", "price", "quantity", "status"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.ProductTable.xview)
        scroll_y.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid", text="Product ID")
        self.ProductTable.heading("category", text="Category")
        self.ProductTable.heading("supplier", text="Supplier")
        self.ProductTable.heading("product", text="Product")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("quantity", text="Quantity")
        self.ProductTable.heading("status", text="Status")

        self.ProductTable["show"] = "headings"
        self.ProductTable.column("pid", width=100)
        self.ProductTable.column("category", width=180)
        self.ProductTable.column("supplier", width=180)
        self.ProductTable.column("product", width=180)
        self.ProductTable.column("price", width=150)
        self.ProductTable.column("quantity", width=120)
        self.ProductTable.column("status", width=150)
        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)
        self.show_data()

        # ========== Right Side Images =================
        img4 = Image.open(r"images/right.png")
        img4 = img4.resize((200, 150), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        labimg2 = Label(self.root, image=self.photoimg4, bd=2, relief=RIDGE)
        labimg2.place(x=1080, y=20, width=200, height=150)

        img5 = Image.open(r"images/right.png")
        img5 = img5.resize((200, 150), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        labimg2 = Label(self.root, image=self.photoimg5, bd=2, relief=RIDGE)
        labimg2.place(x=1080, y=240, width=200, height=150)

        img6 = Image.open(r"images/right.png")
        img6 = img6.resize((200, 150), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        labimg2 = Label(self.root, image=self.photoimg6, bd=2, relief=RIDGE)
        labimg2.place(x=1080, y=460, width=200, height=150)

# ===========================================================
    def fetch_category_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()
            if len(cat) >0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            if len(sup) >0:
                del self.sup_list[:]
                self.sup_list.append("Select")
            for i in sup:
                self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


 # ===============_This saves the employee details gotten from the front-end user interface_===============
    def save_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_category.get() == "Select" or self.var_category.get() == "Empty" or self.var_supplier.get() == "Select" or self.var_product.get() == "":
                messagebox.showerror("Saving Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from product where product=?", (self.var_product.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Product already exists in record, Enter new product", parent=self.root)
                else:
                    cur.execute("Insert into product (category, supplier, product, price, quantity, status) values(?,?,?,?,?,?)",(
                                            self.var_category.get(),
                                            self.var_supplier.get(),
                                            self.var_product.get(),
                                            self.var_price.get(),
                                            self.var_quantity.get(),
                                            self.var_status.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Product Details Added Successfully", parent=self.root)
                    self.show_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

# ==============_This displays the database data in the columns in the user interface_========================
    def show_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.ProductTable.delete(* self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

# ==============_This gets the user data stored in the database_========================
    def get_data(self, event):
        cur = self.ProductTable.focus()
        content = self.ProductTable.item(cur)
        row = content["values"]
        self.var_pid.set(row[0]),
        self.var_category.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_product.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6])

# ==============_This updates the employee details in the database_========================
    def update_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_pid.get() == "Select":
                messagebox.showerror("Update Error", "Kindly select product from list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product Name", parent=self.root)
                else:
                    cur.execute("Update product set category=?, supplier=?, product=?, price=?, quantity=?, status=? where pid=? ", (
                                            self.var_category.get(),
                                            self.var_supplier.get(),
                                            self.var_product.get(),
                                            self.var_price.get(),
                                            self.var_quantity.get(),
                                            self.var_status.get(),
                                            self.var_pid.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Product Details Updated Successfully", parent=self.root)
                    self.show_data()
                    conn.close()
        except Exception as ex:
            messagebox.showerror("Update Error", f"Error due to : {str(ex)}")

    # ==============_This deletes the employee details in the database_========================

    def delete_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_pid.get() == "Select":
                messagebox.showerror("Delete Error", "Kindly select product from list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product Name", parent=self.root)
                else:
                    if messagebox.askyesno("Confirm", "Do you want to delete Product?", parent=self.root) == YES:
                        cur.execute("delete from product where product=?", (self.var_product.get(),))
                        conn.commit()
                        self.show_data()
                        messagebox.showinfo("Delete Status", "Product Details Deleted Successfully", parent=self.root)
                    else:
                        return
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    # ==============_This clears the employee details in the text fields_========================

    def clear_data(self):
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_product.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_searchTxt.set(""),
        self.var_searchBy.set("Select")
        self.show_data()

    # ==============_SEARCH SYSTEM FUNCTIONS_========================
    def search(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_searchBy.get() == "Select":
                messagebox.showerror("Search Error", "Select Search Option", parent=self.root)
            elif self.var_searchTxt.get() == "":
                messagebox.showerror("Search Error", "Search Input Text Required", parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchTxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Search Error", "No Record Found!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Search Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Product(root)
    root.mainloop()