from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class Category:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x630+220+150")
        self.root.title("SMK Inventory Management System  |  Developed By Dreams-Tech Solutions")
        self.root.config(bg="white")
        self.root.focus_force()
        # ===========Variables============
        self.var_category_id = StringVar()
        self.var_name = StringVar()


        # ==========Title=============
        lab_title = Label(self.root, text="Manage Product Category", font=("times new roman", 25, "bold"), bd=3, relief=RIDGE, bg="#184a45", fg="#ffffff")
        lab_title.pack(side=TOP, fill=X, padx=10, pady=20)

        # =========Labels and Entries=============
        lab_name = Label(self.root, text="Enter Category Name :", font=("times new roman", 17, "bold"), bg="white", fg="#000000")
        lab_name.place(x=20, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("yu gothic ui", 17), bg="lightyellow", fg="#000000")
        txt_name.place(x=250, y=100, width=300)

        # ===========Buttons=========
        save = Image.open(r"images/save.png")
        save = save.resize((23, 19), Image.LANCZOS)
        self.save = ImageTk.PhotoImage(save)
        save_btn = Button(self.root, text="Add", command=self.add_data, font=("times new roman", 13), image=self.save, bg="#40b5ad", padx=8,cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="#000000")
        save_btn.place(x=570, y=102)

        delete = Image.open(r"images/delete.png")
        delete = delete.resize((23, 19), Image.LANCZOS)
        self.delete = ImageTk.PhotoImage(delete)
        delete_btn = Button(self.root, text="Delete", command=self.delete_data, font=("times new roman", 13), image=self.delete, bg="#F89880", padx=8,cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="#000000")
        delete_btn.place(x=670, y=103)

        # ============Bottom Image===============
        img3 = Image.open(r"images/cat_3.png")
        img3 = img3.resize((755, 430), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        labimg = Label(self.root, image=self.photoimg3, bd=3, relief=RIDGE)
        labimg.place(x=15, y=160, width=755, height=430)

        img4 = Image.open(r"images/cat_4.png")
        img4 = img4.resize((480, 300), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        labimg2 = Label(self.root, image=self.photoimg4, bd=3, relief=RIDGE)
        labimg2.place(x=790, y=290, width=480, height=300)

        # =============Products Category Data View Table_==============
        category_frame = Frame(self.root, bd=3, relief=RIDGE)
        category_frame.place(x=790, y=80, width=480, height=200)

        scroll_y = Scrollbar(category_frame, orient=VERTICAL)
        scroll_x = Scrollbar(category_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(category_frame, columns=("cid", "name"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.CategoryTable.xview)
        scroll_y.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid", text="Category ID")
        self.CategoryTable.heading("name", text="Category Name")
        self.CategoryTable["show"] = "headings"
        self.CategoryTable.column("cid", width=50)
        self.CategoryTable.column("name", width=200)
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

        # ===============_Functions_===============
    def add_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Name is required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Category Error", "Category Name Already Exists, Enter a New Category Name", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)", (self.var_name.get(),))
                    conn.commit()
                    messagebox.showinfo("Category Status", "Product Category Added Successfully", parent=self.root)
                    self.show_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def show_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Data Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, event):
        cur = self.CategoryTable.focus()
        content = self.CategoryTable.item(cur)
        row = content["values"]
        self.var_category_id.set(row[0]),
        self.var_name.set(row[1])

    def delete_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_category_id.get() == "":
                messagebox.showerror("Delete Error", "No Category Name Selected From List", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?", (self.var_category_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Delete Error", "Category Does Not Exist", parent=self.root)
                else:
                    if messagebox.askyesno("Confirmation Message", "Do you want to delete Category?", parent=self.root) == YES:
                        cur.execute("delete from category where cid=?", (self.var_category_id.get(),))
                        conn.commit()
                        self.show_data()
                        self.var_category_id.set(""),
                        self.var_name.set("")
                        messagebox.showinfo("Delete Status", "Product Category Deleted Successfully", parent=self.root)
                    else:
                        return
        except Exception as ex:
            messagebox.showerror("Delete Error", f"Error due to : {str(ex)}")



if __name__ == "__main__":
    root = Tk()
    obj = Category(root)
    root.mainloop()
