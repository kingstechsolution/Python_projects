from tkcalendar import *
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x630+220+150")
        self.root.title("SMK Inventory Management System")
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
        self.var_role = StringVar()

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

        searchframe = LabelFrame(self.root, text="Search Employee", bg="white", font=("yu gothic ui", 15, "bold"), bd=2,
                                 relief=RIDGE)
        searchframe.place(x=290, y=20, width=550, height=73)

        # ========_Options_=========
        combo_search = ttk.Combobox(searchframe, textvariable=self.var_searchBy,values=("Select", "Employee ID", "Name", "Contact"), state="readonly",
                                    justify=CENTER, font=("goudy old style", 15))
        combo_search.place(x=10, y=3, width=180)
        combo_search.current(0)

        text_search = Entry(searchframe, textvariable=self.var_searchTxt, font=("yu gothic ui", 15), bg="lightyellow")
        text_search.place(x=200, y=2)

        # =======_Search Button Image_==========
        icon = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/search2.png")
        icon = icon.resize((23, 19), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(icon)
        search_btn = Button(searchframe, text="Search", font=("yu gothic ui", 13, "bold"), image=self.photo, padx=8,
                            cursor="hand2", compound=LEFT, anchor="e", bg="red", fg="white")
        search_btn.place(x=444, y=-3, width=100)

        # ========_Title_=========
        title = Label(self.root, text="Employee Details", font=("yu gothic ui", 15, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=100, y=100, width=1100)

        # ========_Content Layout_=========
        # ===========_Row 1_============
        employee_id = Label(self.root, text="Emp ID :", font=("yu gothic ui", 15), bg="white")
        employee_id.place(x=100, y=150)
        txt_employee_id = Entry(self.root, textvariable=self.var_employee_id, font=("yu gothic ui", 12),
                                bg="light yellow")
        txt_employee_id.place(x=200, y=155, width=200)

        gender = Label(self.root, text="Gender :", font=("yu gothic ui", 15), bg="white")
        gender.place(x=450, y=150)
        combo_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                    values=("Select", "Male", "Female", "Other"), state="readonly", justify=CENTER,
                                    font=("yu gothic ui", 12))
        combo_gender.place(x=550, y=155, width=200)
        combo_gender.current(0)

        contact = Label(self.root, text="Contact :", font=("yu gothic ui", 15), bg="white")
        contact.place(x=800, y=150)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("yu gothic ui", 12), bg="light yellow")
        txt_contact.place(x=900, y=155, width=200)

        # ===========_Row 2_=============
        name = Label(self.root, text="Name :", font=("yu gothic ui", 15), bg="white")
        name.place(x=100, y=195)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("yu gothic ui", 12, "bold"), bg="light yellow")
        txt_name.place(x=200, y=200, width=200)

        dob = Label(self.root, text="D.O.B :", font=("yu gothic ui", 15), bg="white")
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
        email = Label(self.root, text="Email :", font=("yu gothic ui", 15), bg="white")
        email.place(x=100, y=240)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("yu gothic ui", 12), bg="light yellow")
        txt_email.place(x=200, y=245, width=200)

        password = Label(self.root, text="Password :", font=("yu gothic ui", 15), bg="white")
        password.place(x=450, y=240)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("yu gothic ui", 12), bg="light yellow")
        txt_pass.place(x=550, y=245, width=200)

        user_type = Label(self.root, text="User Type :", font=("yu gothic ui", 15), bg="white")
        user_type.place(x=800, y=240)
        combo_user_type = ttk.Combobox(self.root, textvariable=self.var_uType, values=("Admin", "Employee"),
                                       state="readonly", justify=CENTER, font=("yu gothic ui", 12))
        combo_user_type.place(x=900, y=245, width=200)
        combo_user_type.current(0)

        # ===========_Row 4_============
        address = Label(self.root, text="Address :", font=("yu gothic ui", 15), bg="white")
        address.place(x=100, y=285)
        txt_address = Text(self.root, font=("yu gothic ui", 12), bg="light yellow")
        txt_address.place(x=200, y=290, width=330, height=75)

        salary = Label(self.root, text="Salary :", font=("yu gothic ui", 15), bg="white")
        salary.place(x=545, y=285)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("yu gothic ui", 12), bg="light yellow")
        txt_salary.place(x=620, y=293, width=200)

        role = Label(self.root, text="Role :", font=("yu gothic ui", 15), bg="white")
        role.place(x=840, y=285)
        txt_role = Entry(self.root, textvariable=self.var_role, font=("yu gothic ui", 12), bg="light yellow")
        txt_role.place(x=900, y=290, width=200)
        """
        combo_user_type = ttk.Combobox(self.root, textvariable=self.var_role, values=("Sales Rep", "Marketer"),state="readonly", justify=CENTER, font=("yu gothic ui", 15))
        combo_user_type.place(x=900, y=292, width=200)
        combo_user_type.current(0)
        """

        # ===========_CRUD Functions Buttons_============
        save = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/save.png")
        save = save.resize((23, 19), Image.LANCZOS)
        self.save = ImageTk.PhotoImage(save)
        save_btn = Button(self.root, text="Save", font=("yu gothic ui", 13, "bold"), image=self.save, padx=8,
                          cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        save_btn.place(x=570, y=330)

        update = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/update.png")
        update = update.resize((23, 19), Image.LANCZOS)
        self.update = ImageTk.PhotoImage(update)
        update_btn = Button(self.root, text="Update", font=("yu gothic ui", 13, "bold"), image=self.update, padx=4,
                            cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        update_btn.place(x=670, y=330, width=95)

        delete = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/delete.png")
        delete = delete.resize((23, 19), Image.LANCZOS)
        self.delete = ImageTk.PhotoImage(delete)
        delete_btn = Button(self.root, text="Delete", font=("yu gothic ui", 13, "bold"), image=self.delete, padx=4,
                            cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        delete_btn.place(x=775, y=330, width=95)

        clear = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/clear.png")
        clear = clear.resize((23, 19), Image.LANCZOS)
        self.clear = ImageTk.PhotoImage(clear)
        clear_btn = Button(self.root, text="Clear", font=("yu gothic ui", 13, "bold"), image=self.clear, padx=6,
                           cursor="hand2", compound=LEFT, anchor="e", bd=1, fg="black")
        clear_btn.place(x=880, y=330, width=85)

        # =============_Employee Data View Table_==============
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=380, relwidth=1, height=240)

        scroll_y = Scrollbar(emp_frame, orient=VERTICAL)
        scroll_x = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployyeTable = ttk.Treeview(emp_frame, columns=("id", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "role", "address", "salary"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.EmployyeTable.xview)
        scroll_y.config(command=self.EmployyeTable.yview)

        self.EmployyeTable.heading("id", text="Employee ID")
        self.EmployyeTable.heading("name", text="Full Name")
        self.EmployyeTable.heading("email", text="Email")
        self.EmployyeTable.heading("gender", text="Gender")
        self.EmployyeTable.heading("contact", text="Contact")
        self.EmployyeTable.heading("dob", text="Date Of Birth")
        self.EmployyeTable.heading("doj", text="Employment Date")
        self.EmployyeTable.heading("pass", text="Password")
        self.EmployyeTable.heading("utype", text="User Type")
        self.EmployyeTable.heading("role", text="Job Role")
        self.EmployyeTable.heading("address", text="Address")
        self.EmployyeTable.heading("salary", text="Salary")

        self.EmployyeTable["show"] = "headings"

        self.EmployyeTable.column("id", width=90)
        self.EmployyeTable.column("name", width=180)
        self.EmployyeTable.column("email", width=180)
        self.EmployyeTable.column("gender", width=120)
        self.EmployyeTable.column("contact", width=150)
        self.EmployyeTable.column("dob", width=150)
        self.EmployyeTable.column("doj", width=150)
        self.EmployyeTable.column("pass", width=150)
        self.EmployyeTable.column("utype", width=150)
        self.EmployyeTable.column("role", width=180)
        self.EmployyeTable.column("address", width=180)
        self.EmployyeTable.column("salary", width=150)

        self.EmployyeTable.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
