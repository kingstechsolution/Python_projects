from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import random

class Supplier:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x630+220+150")
        self.root.title("SMK Inventory Management System  |  Developed By Dreams-Tech Solutions")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==============_Variables_===============
        # ======_Search Bar_==========
        self.var_searchBy = StringVar()
        self.var_searchTxt = StringVar()
        # ========_Form Entries_=========
        self.var_sup_invoice = StringVar()
        x = random.randint(100000, 999999)
        self.var_sup_invoice.set(str(x))

        self.var_name = StringVar()
        self.var_contact = StringVar()

            # ==========_Search Frame_==========
        lab_search = Label(self.root, text="Invoice No.", font=("times new roman", 13, "bold"), bg="white")
        lab_search.place(x=730, y=75)

        text_search = Entry(self.root, textvariable=self.var_searchTxt, font=("yu gothic ui", 15), bg="lightyellow")
        text_search.place(x=830, y=70)

        # =======_Search Button Image_==========
        icon = Image.open(r"images/search2.png")
        icon = icon.resize((23, 19), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(icon)
        search_btn = Button(self.root, text="Search", command=self.search, font=("times new roman", 13, "bold"), image=self.photo, bd=1, padx=8,cursor="hand2", compound=LEFT, anchor="e", bg="#40b5ad", fg="white")
        search_btn.place(x=1070, y=70, width=100)

        # ========_Title_=========
        title = Label(self.root, text="Manage Supplier Details", font=("times new roman", 20, "bold"), bd=3, relief=RIDGE, bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X, padx=10, pady=20)

        # ========_Content Layout_=========
        # ===========_Row 1_============
        lab_supplier_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white")
        lab_supplier_invoice.place(x=100, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, state="readonly", font=("yu gothic  ui", 12), bg="light yellow")
        txt_supplier_invoice.place(x=250, y=85, width=200)

        # ===========_Row 2_=============
        lab_name = Label(self.root, text="Supplier Name", font=("times new roman", 15), bg="white")
        lab_name.place(x=100, y=125)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("yu gothic ui", 12), bg="light yellow")
        txt_name.place(x=250, y=130, width=200)

        # ===========_Row 3_============
        lab_contact = Label(self.root, text="Contact", font=("times new roman", 15), bg="white")
        lab_contact.place(x=100, y=165)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("yu gothic ui", 12), bg="light yellow")
        txt_contact.place(x=250, y=170, width=200)

        # ===========_Row 4_============
        lab_desc = Label(self.root, text="Description", font=("times new roman", 15), bg="white")
        lab_desc.place(x=100, y=210)
        self.txt_desc = Text(self.root, font=("yu gothic ui", 12), bg="light yellow")
        self.txt_desc.place(x=250, y=215, width=390, height=100)

        # ===========_CRUD Functions Buttons_============
        save = Image.open(r"images/save.png")
        save = save.resize((23, 19), Image.LANCZOS)
        self.save = ImageTk.PhotoImage(save)
        save_btn = Button(self.root, text="Save", command=self.save_data, font=("times new roman", 13), image=self.save, padx=8, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        save_btn.place(x=250, y=350)

        update = Image.open(r"images/update.png")
        update = update.resize((23, 19), Image.LANCZOS)
        self.update = ImageTk.PhotoImage(update)
        update_btn = Button(self.root, text="Update", command=self.update_data, font=("times new roman", 13), image=self.update, padx=4 ,cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        update_btn.place(x=350, y=350, width=95)

        delete = Image.open(r"images/delete.png")
        delete = delete.resize((23, 19), Image.LANCZOS)
        self.delete = ImageTk.PhotoImage(delete)
        delete_btn = Button(self.root, text="Delete", command=self.delete_data, font=("times new roman", 13), image=self.delete, padx=4, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        delete_btn.place(x=455, y=350, width=95)

        clear = Image.open(r"images/clear.png")
        clear = clear.resize((23, 19), Image.LANCZOS)
        self.clear = ImageTk.PhotoImage(clear)
        clear_btn = Button(self.root, text="Clear", command=self.clear_data, font=("times new roman", 13), image=self.clear, padx=6, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        clear_btn.place(x=560, y=350, width=85)

        # ============Bottom Image===============
        img3 = Image.open(r"images/sup_01.jpg")
        img3 = img3.resize((635, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        labimg = Label(self.root, image=self.photoimg3, bd=3, relief=RIDGE)
        labimg.place(x=10, y=390, width=635, height=220)

        img4 = Image.open(r"images/sup3.jpg")
        img4 = img4.resize((150, 110), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        labimg1 = Label(self.root, image=self.photoimg4, bd=1, relief=RIDGE)
        labimg1.place(x=480, y=85, width=150, height=110)

        # =============Supplier Data View Table_==============
        sup_frame = Frame(self.root, bd=3, relief=RIDGE)
        sup_frame.place(x=650, y=110, width=630, height=500)

        scroll_y = Scrollbar(sup_frame, orient=VERTICAL)
        scroll_x = Scrollbar(sup_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(sup_frame, columns=("InvoiceNo", "name", "contact", "description"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.SupplierTable.xview)
        scroll_y.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("InvoiceNo", text="Invoice No")
        self.SupplierTable.heading("name", text="Supplier Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("description", text="Description")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("InvoiceNo", width=80)
        self.SupplierTable.column("name", width=180)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("description", width=180)
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show_data()

    # ===============_This saves the supplier details gotten from the front-end user interface_===============
    def save_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Saving Error", "Invoice No is required", parent=self.root)
            elif self.var_name.get() == "":
                messagebox.showerror("Details Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from supplier where InvoiceNo=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Details Error", "This Invoice No Already Exists in Record", parent=self.root)
                else:
                    cur.execute("Insert into supplier (InvoiceNo, name, contact, description) values(?,?,?,?)", (
                                            self.var_sup_invoice.get(),
                                            self.var_name.get(),
                                            self.var_contact.get(),
                                            self.txt_desc.get('1.0', END),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Supplier Details Saved Successfully", parent=self.root)
                    self.show_data()
        except Exception as ex:
            messagebox.showerror("Saving Error", f"Error due to : {str(ex)}")

# ==============_This displays the database data in the columns in the user interface_========================
    def show_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(* self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Data Error", f"Error due to : {str(ex)}", parent=self.root)

# ==============_This gets the user data stored in the database_========================
    def get_data(self, event):
        cur = self.SupplierTable.focus()
        content = self.SupplierTable.item(cur)
        row = content["values"]

        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0', END),
        self.txt_desc.insert(END, row[3])

# ==============_This updates the employee details in the database_========================
    def update_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Update Error", "Invoice No is required", parent=self.root)
            else:
                cur.execute("Select * from supplier where InvoiceNo=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Details Error", "Invalid Invoice No", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?, contact=?, description=? where InvoiceNo=?", (
                                            self.var_name.get(),
                                            self.var_contact.get(),
                                            self.txt_desc.get('1.0', END),
                                            self.var_sup_invoice.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Update Data", "Supplier Details Updated Successfully", parent=self.root)
                    self.show_data()
                    conn.close()
        except Exception as ex:
            messagebox.showerror("Update Error", f"Error due to : {str(ex)}")

    # ==============_This deletes the employee details in the database_========================

    def delete_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Delete Error", "Invoice No is required", parent=self.root)
            else:
                cur.execute("Select * from supplier where InvoiceNo=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Delete Error", "Invalid Invoice No", parent=self.root)
                else:
                    if messagebox.askyesno("Confirmation Message", "Do you want to delete Employee Data?", parent=self.root) == YES:
                        cur.execute("delete from supplier where InvoiceNo=?", (self.var_sup_invoice.get(),))
                        conn.commit()
                        self.show_data()
                        messagebox.showinfo("Delete Status", "Employee Details Deleted Successfully", parent=self.root)
                    else:
                        return Supplier
        except Exception as ex:
            messagebox.showerror("Delete Error", f"Error due to : {str(ex)}")

    # ==============_This clears the employee details in the text fields_========================
    def clear_data(self):
        x = random.randint(100000, 999999)
        self.var_sup_invoice.set(str(x))
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END),
        self.var_searchTxt.set(""),
        self.show_data()

    # ==============_SEARCH SYSTEM FUNCTIONS_========================
    def search(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_searchTxt.get() == "":
                messagebox.showerror("Search Error", "Invoice No. is Required", parent=self.root)
            else:
                cur.execute("select * from supplier where InvoiceNo=?",(self.var_searchTxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Search Error", "No Record Found!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Search Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Supplier(root)
    root.mainloop()
