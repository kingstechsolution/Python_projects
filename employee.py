from tkcalendar import *
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class Employee:
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
        self.var_employee_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()

        self.var_dob = StringVar()
        self.var_doj = StringVar()

        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_uType = StringVar()
        self.var_salary = StringVar()

        # ====_Gets the selected date in date of birth when the user closes the calendar_======
        def pick_date(event):
            global cal, date_window
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title("Choose Date")
            date_window.geometry("250x220+770+380")
            cal = Calendar(date_window, selectmode="day", date_pattern="dd/mm/y")
            cal.place(x=0, y=0)

            submit_btn = Button(date_window, text="Submit", command=grab_date, bg="light yellow")
            submit_btn.place(x=100, y=190)

        def grab_date():
            dob_entry.delete(0, END)
            dob_entry.insert(0, cal.get_date())
            date_window.destroy()

        # ====_Gets the selected date in date of employment when the user closes the calendar_======
        def pick_date1(event):
            global cal1, date_window1
            date_window1 = Toplevel()
            date_window1.grab_set()
            date_window1.title("Choose Date")
            date_window1.geometry("250x220+1100+380")
            cal1 = Calendar(date_window1, selectmode="day", date_pattern="dd/mm/y")
            cal1.place(x=0, y=0)

            submit_btn1 = Button(date_window1, text="Submit", command=grab_date1, bg="light yellow")
            submit_btn1.place(x=100, y=190)

        def grab_date1():
            txt_doj.delete(0, END)
            txt_doj.insert(0, cal1.get_date())
            date_window1.destroy()

            # ==========_Search Frame_==========
        searchframe = LabelFrame(self.root, text="Search Employee", bg="white", font=("times new roman", 15, "bold"), bd=2,relief=RIDGE)
        searchframe.place(x=290, y=20, width=550, height=73)

        # ========_Options_=========
        combo_search = ttk.Combobox(searchframe, textvariable=self.var_searchBy,values=("Select", "Email", "Name", "Contact"), state="readonly",justify=CENTER, font=("times new roman", 15))
        combo_search.place(x=10, y=3, width=180)
        combo_search.current(0)

        text_search = Entry(searchframe, textvariable=self.var_searchTxt, font=("yu gothic ui", 15), bg="lightyellow")
        text_search.place(x=200, y=2)

        # =======_Search Button Image_==========
        icon = Image.open(r"images/search2.png")
        icon = icon.resize((23, 19), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(icon)
        search_btn = Button(searchframe, text="Search", command=self.search, font=("times new roman", 13, "bold"), image=self.photo, padx=8,cursor="hand2", compound=LEFT, anchor="e", bg="#40b5ad", fg="white")
        search_btn.place(x=440, y=3, width=100)

        # ============Top Right Image===============
        img3 = Image.open(r"images/employee.png")
        img3 = img3.resize((140, 90), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        labimg = Label(self.root, image=self.photoimg3, bd=2, relief=RIDGE)
        labimg.place(x=145, y=10, width=140, height=90)

        # ========_Title_=========
        title = Label(self.root, text="Manage Employee Details", font=("times new roman", 20, "bold"), bd=3, relief=RIDGE, bg="#0f4d7d", fg="white")
        title.place(x=0, y=100, width=1300)

        # ========_Content Layout_=========
        # ===========_Row 1_============
        employee_id = Label(self.root, text="Emp ID :", font=("times new roman", 15), bg="white")
        employee_id.place(x=100, y=150)
        self.txt_employee_id = Entry(self.root, textvariable=self.var_employee_id, font=("yu gothic ui", 12),bg="light yellow")
        self.txt_employee_id.place(x=200, y=155, width=200)

        gender = Label(self.root, text="Gender :", font=("times new roman", 15), bg="white")
        gender.place(x=450, y=150)
        combo_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select", "Male", "Female"), state="readonly", justify=CENTER,font=("yu gothic ui", 12))
        combo_gender.place(x=550, y=155, width=200)
        combo_gender.current(0)

        contact = Label(self.root, text="Contact :", font=("times new roman", 15), bg="white")
        contact.place(x=800, y=150)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("yu gothic ui", 12), bg="light yellow")
        self.txt_contact.place(x=900, y=155, width=200)

        # ===========_Row 2_=============
        name = Label(self.root, text="Name :", font=("times new roman", 15), bg="white")
        name.place(x=100, y=195)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("yu gothic ui", 12), bg="light yellow")
        self.txt_name.place(x=200, y=200, width=200)

        dob = Label(self.root, text="D.O.B :", font=("times new roman", 15), bg="white")
        dob.place(x=450, y=195)
        dob_entry = Entry(self.root, textvariable=self.var_dob, bg="light yellow", font=("yu gothic ui", 12))
        dob_entry.place(x=550, y=200, width=200)
        dob_entry.insert(0, "dd/mm/yyyy")
        dob_entry.bind("<1>", pick_date)

        doj = Label(self.root, text="D.O.E :", font=("yu gothic ui", 15), bg="white")
        doj.place(x=800, y=195)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("yu gothic ui", 12), bg="light yellow")
        txt_doj.place(x=900, y=200, width=200)
        txt_doj.insert(0, "dd/mm/yyyy")
        txt_doj.bind("<1>", pick_date1)

        # ===========_Row 3_============
        email = Label(self.root, text="Email :", font=("times new roman", 15), bg="white")
        email.place(x=100, y=240)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("yu gothic ui", 12), bg="light yellow")
        txt_email.place(x=200, y=245, width=200)

        password = Label(self.root, text="Password :", font=("times new roman", 15), bg="white")
        password.place(x=450, y=240)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("yu gothic ui", 12), bg="light yellow")
        txt_pass.place(x=550, y=245, width=200)

        user_type = Label(self.root, text="User Type :", font=("times new roman", 15), bg="white")
        user_type.place(x=800, y=240)
        combo_user_type = ttk.Combobox(self.root, textvariable=self.var_uType, values=("Admin", "Employee"),state="readonly", justify=CENTER, font=("yu gothic ui", 12))
        combo_user_type.place(x=900, y=245, width=200)
        combo_user_type.current(0)

        # ===========_Row 4_============
        address = Label(self.root, text="Address :", font=("times new roman", 15), bg="white")
        address.place(x=100, y=285)
        self.txt_address = Text(self.root, font=("yu gothic ui", 12), bg="light yellow")
        self.txt_address.place(x=200, y=290, width=330, height=75)

        salary = Label(self.root, text="Salary :", font=("times new roman", 15), bg="white")
        salary.place(x=545, y=285)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("yu gothic ui", 12), bg="light yellow")
        txt_salary.place(x=620, y=288, width=200)

        # ===========_CRUD Functions Buttons_============
        save = Image.open(r"images/save.png")
        save = save.resize((23, 19), Image.LANCZOS)
        self.save = ImageTk.PhotoImage(save)
        save_btn = Button(self.root, text="Save", command=self.save_data, font=("times new roman", 13, "bold"), image=self.save, padx=8, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        save_btn.place(x=570, y=330)

        update = Image.open(r"images/update.png")
        update = update.resize((23, 19), Image.LANCZOS)
        self.update = ImageTk.PhotoImage(update)
        update_btn = Button(self.root, text="Update", command=self.update_data, font=("times new roman", 13, "bold"), image=self.update, padx=4 ,cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        update_btn.place(x=670, y=330, width=95)

        delete = Image.open(r"images/delete.png")
        delete = delete.resize((23, 19), Image.LANCZOS)
        self.delete = ImageTk.PhotoImage(delete)
        delete_btn = Button(self.root, text="Delete", command=self.delete_data, font=("times new roman", 13, "bold"), image=self.delete, padx=4, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        delete_btn.place(x=775, y=330, width=95)

        clear = Image.open(r"images/clear.png")
        clear = clear.resize((23, 19), Image.LANCZOS)
        self.clear = ImageTk.PhotoImage(clear)
        clear_btn = Button(self.root, text="Clear", command=self.clear_data, font=("times new roman", 13, "bold"), image=self.clear, padx=6, cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        clear_btn.place(x=880, y=330, width=85)

        # =============_Employee Data View Table_==============
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=380, relwidth=1, height=240)

        scroll_y = Scrollbar(emp_frame, orient=VERTICAL)
        scroll_x = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("id", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.EmployeeTable.xview)
        scroll_y.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("id", text="Employee ID")
        self.EmployeeTable.heading("name", text="Employee Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="Date Of Birth")
        self.EmployeeTable.heading("doj", text="Employment Date")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.column("id", width=180)
        self.EmployeeTable.column("name", width=180)
        self.EmployeeTable.column("email", width=180)
        self.EmployeeTable.column("gender", width=120)
        self.EmployeeTable.column("contact", width=150)
        self.EmployeeTable.column("dob", width=150)
        self.EmployeeTable.column("doj", width=150)
        self.EmployeeTable.column("pass", width=150)
        self.EmployeeTable.column("utype", width=150)
        self.EmployeeTable.column("address", width=180)
        self.EmployeeTable.column("salary", width=150)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show_data()

    # ===============_This saves the employee details gotten from the front-end user interface_===============
    def save_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_employee_id.get() == "":
                messagebox.showerror("Saving Error", "Employee ID is required", parent=self.root)
            elif self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from employee where id=?", (self.var_employee_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID has already been assigned, try a different ID", parent=self.root)
                else:
                    cur.execute("Insert into employee (id, name, email, gender, contact, dob, doj, pass, utype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                            self.var_employee_id.get(),
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_gender.get(),
                                            self.var_contact.get(),

                                            self.var_dob.get(),
                                            self.var_doj.get(),

                                            self.var_pass.get(),
                                            self.var_uType.get(),
                                            self.txt_address.get('1.0', END),
                                            self.var_salary.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee Details Saved Successfully", parent=self.root)
                    self.show_data()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

# ==============_This displays the database data in the columns in the user interface_========================
    def show_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(* self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

# ==============_This gets the user data stored in the database_========================
    def get_data(self, event):
        cur = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(cur)
        row = content["values"]

        self.var_employee_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_uType.set(row[8]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[9]),
        self.var_salary.set(row[10])

# ==============_This updates the employee details in the database_========================
    def update_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_employee_id.get() == "":
                messagebox.showerror("Update Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("Select * from employee where id=?", (self.var_employee_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("Update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, "
                                "utype=?, address=?, salary=? where id=?", (
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_gender.get(),
                                            self.var_contact.get(),
                                            self.var_dob.get(),
                                            self.var_doj.get(),
                                            self.var_pass.get(),
                                            self.var_uType.get(),
                                            self.txt_address.get('1.0', END),
                                            self.var_salary.get(),
                                            self.var_employee_id.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Update Data", "Employee Details Updated Successfully", parent=self.root)
                    self.show_data()
                    conn.close()
        except Exception as ex:
            messagebox.showerror("Update Error", f"Error due to : {str(ex)}")

    # ==============_This deletes the employee details in the database_========================

    def delete_data(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.var_employee_id.get() == "":
                messagebox.showerror("Delete Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("Select * from employee where id=?", (self.var_employee_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Delete Error", "Invalid Employee ID", parent=self.root)
                else:
                    if messagebox.askyesno("Confirmation Message", "Do you want to delete Employee Data?", parent=self.root) == YES:
                        cur.execute("delete from employee where id=?", (self.var_employee_id.get(),))
                        conn.commit()
                        self.show_data()
                        messagebox.showinfo("Delete Status", "Employee Details Deleted Successfully", parent=self.root)
                    else:
                        return
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    # ==============_This clears the employee details in the text fields_========================

    def clear_data(self):
        self.var_employee_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_uType.set("Admin")
        self.txt_address.delete('1.0', END),
        self.var_salary.set(""),
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
                cur.execute("select * from employee where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchTxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Search Error", "No Record Found!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Search Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()