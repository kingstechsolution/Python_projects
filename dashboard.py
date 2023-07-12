from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from employee import Employee
from tkinter import messagebox

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("SMK Inventory Management System")
        self.root.config(bg="ghostwhite")

        #=======_Title_=========
        img1 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/logo5.png")
        img1 = img1.resize((80, 55), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        title = Label(self.root, text="Inventory Management System", image=self.photoimg1, compound=LEFT, font=("times new roman",35,"bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0,y=0, relwidth=1, height=70)

        #========_Logout Button_==========
        imgLB = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/logout.png")
        imgLB = imgLB.resize((18, 18), Image.LANCZOS)
        self.photoimgLB = ImageTk.PhotoImage(imgLB)
        logout_btn = Button(self.root, text="Logout", image=self.photoimgLB, compound=RIGHT, anchor="e", font=("times new roman",15,"bold"),bg="yellow", cursor="hand2", width=80)
        logout_btn.place(x=1350, y=15)

        #========_Date & Time Bar_==========
        self.clock_label = Label(self.root, text="Super Marche Kado Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("anton",15),bg="#4d636d", fg="white")
        self.clock_label.place(x=0,y=70, relwidth=1, height=40)

        #========_Side Navigation Bar_=========
        self.menu_logo = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/shop.jpeg")
        self.menu_logo = self.menu_logo.resize((200,150),Image.LANCZOS)
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        Left_menu = Frame(self.root, bd=2, relief=RIDGE, bg="slategrey")
        Left_menu.place(x=0, y=112, width=210, height=700)

        label_menu_logo = Label(Left_menu, image=self.menu_logo)
        label_menu_logo.pack(side=TOP, fill=X)

        #==========_Menu Label_============
        img0 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/rg.png")
        img0 = img0.resize((50, 40), Image.LANCZOS)
        self.photoimg0 = ImageTk.PhotoImage(img0)
        menu_label = Label(Left_menu, text="Menu",image=self.photoimg0, compound=LEFT, anchor="w", font=("times new roman", 20,"bold"),bg="teal", fg="white", padx=15)
        menu_label.pack(side=TOP, fill=X)

        #==========_Side Nav_Bar Images_===========
        img2 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/emp.png")
        img2 = img2.resize((50, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/sup.png")
        img3 = img3.resize((50, 40), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        img4 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/cat.png")
        img4 = img4.resize((50, 40), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        img5 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/prod.png")
        img5 = img5.resize((50, 40), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        img6 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/sales.png")
        img6 = img6.resize((50, 40), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        img7 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/serv1.png")
        img7 = img7.resize((50, 40), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        img8 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/exit.png")
        img8 = img8.resize((50, 40), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        # ==========_Side Nav_Bar Buttons_===========
        employee_label = Button(Left_menu, text="Employee", command=self.employee, image=self.photoimg2, compound=LEFT, anchor="w",font=("anton", 16,"bold"), bd=3, cursor="hand2", bg="white", fg="black", padx=15)
        employee_label.pack(side=TOP, fill=X, pady=1)

        supplier_label = Button(Left_menu, text="Supplier", image=self.photoimg3, compound=LEFT, anchor="w", font=("anton", 16,"bold"), bd=3, cursor="hand2", bg="white", fg="black", padx=15)
        supplier_label.pack(side=TOP, fill=X, pady=1)

        category_label = Button(Left_menu, text="Category", image=self.photoimg4, compound=LEFT, anchor="w", font=("anton", 16,"bold"), bd=3, cursor="hand2", bg="white", fg="black", padx=15)
        category_label.pack(side=TOP, fill=X, pady=1)

        product_label = Button(Left_menu, text="Products", image=self.photoimg5, compound=LEFT, anchor="w", font=("anton", 16,"bold"), bd=3,  cursor="hand2", bg="white", fg="black", padx=15)
        product_label.pack(side=TOP, fill=X, pady=1)

        sales_label = Button(Left_menu, text="Sales", image=self.photoimg6, compound=LEFT, anchor="w", font=("anton", 16,"bold"), bd=3, cursor="hand2", bg="white", fg="black", padx=15)
        sales_label.pack(side=TOP, fill=X, pady=1)

        service_label = Button(Left_menu, text="Services", image=self.photoimg7, compound=LEFT, anchor="w",font=("anton", 16, "bold"), bd=3, cursor="hand2", bg="white", fg="black", padx=15)
        service_label.pack(side=TOP, fill=X, pady=1)

        exit_label = Button(Left_menu, text="Exit", command=self.exit, image=self.photoimg8, compound=LEFT, anchor="w", font=("anton", 16,"bold"), bd=3, cursor="hand2", bg="white", fg="black", padx=15)
        exit_label.pack(side=TOP, fill=X, pady=1)


        #=======_Navigation Bar Down Image_========
        self.menu_logo2 = Image.open(r"C:\Users\XPS\PycharmProjects\Inventory Management System\images/meet.jpg")
        self.menu_logo2 = self.menu_logo2.resize((200, 105), Image.LANCZOS)
        self.menu_logo2 = ImageTk.PhotoImage(self.menu_logo2)

        label_menu_logo2 = Label(Left_menu, image=self.menu_logo2)
        label_menu_logo2.pack(side=TOP, fill=X)

        #==========_Div Content_============
        div = Frame(self.root, bd=2, relief=RIDGE)
        div.place(x=278, y=135, width=1150, height=380)
        self.label_employee = Label(self.root, text="Total Employees\n [ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.label_employee.place(x=300, y=150, height=150, width=300)

        self.label_supplier = Label(self.root, text="Total Suppliers\n [ 0 ]", bd=5, relief=RIDGE,bg="orange", fg="white",font=("goudy old style", 20, "bold"))
        self.label_supplier.place(x=700, y=150, height=150, width=300)

        self.label_category = Label(self.root, text="Total Categories\n [ 0 ]", bd=5, relief=RIDGE, bg="teal", fg="white",font=("goudy old style", 20, "bold"))
        self.label_category.place(x=1100, y=150, height=150, width=300)

        self.label_product = Label(self.root, text="Total Products\n [ 0 ]", bd=5, relief=RIDGE, bg="slategrey", fg="white",font=("goudy old style", 20, "bold"))
        self.label_product.place(x=300, y=350, height=150, width=300)

        self.label_sales = Label(self.root, text="Total Sales\n [ 0 ]", bd=5, relief=RIDGE, bg="steelblue", fg="white",font=("goudy old style", 20, "bold"))
        self.label_sales.place(x=700, y=350, height=150, width=300)

        self.label_services = Label(self.root, text="Total Services\n [ 0 ]", bd=5, relief=RIDGE, bg="dark blue",fg="white", font=("goudy old style", 20, "bold"))
        self.label_services.place(x=1100, y=350, height=150, width=300)

        # ========_Footer_==========
        footer = Label(self.root, text="Super Marche Kado - Inventory Management System |      Developed by Kings-Tech Solutions\n Technical Issue Contact: 680-922-674", font=("anton", 10,"bold"), bg="#4d636d", fg="white")
        footer.place(x=0, y=790, relwidth=1, height=40)
#==========================================================================================================================
    def employee(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Employee(self.new_window)

    def exit(self):
        self.root.destroy()




if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
