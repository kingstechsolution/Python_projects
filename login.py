from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("SMK Inventory Management Login System  |  Developed By Dreams-Tech Solutions")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")

        self.otp = ""
        # ========Images===========
        imgp = Image.open(r"images/phone.png")
        imgp = imgp.resize((900, 600), Image.LANCZOS)
        self.phone_image1 = ImageTk.PhotoImage(imgp)
        self.lab_phone_image1 = Label(self.root, image=self.phone_image1, bd=0)
        self.lab_phone_image1.place(x=100, y=90)

        # ==========Login Frame===========
        self.user_id = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=790, y=135, width=350, height=450)

        title = Label(login_frame, text="Inventory Login System", font=("Anton", 17, "bold"), bg="white", fg="steelblue")
        title.place(x=0, y=25, relwidth=1)

        # ========User Icon===========
        img1 = Image.open(r"images/user (1).png")
        img1 = img1.resize((25, 25), Image.LANCZOS)
        self.username_img = ImageTk.PhotoImage(img1)
        self.lab_user = Label(login_frame, image=self.username_img, bg="white", bd=0)
        self.lab_user.place(x=47, y=100)
        lab_user = Label(login_frame, text="User ID", font=("Andalus", 15), bg="white", fg="#767171")
        lab_user.place(x=75, y=100)
        txt_user = Entry(login_frame, textvariable=self.user_id, font=("times new roman", 15), bg="#ECECEC")
        txt_user.place(x=50, y=135, width=250)

        # ========Paasword Icon===========
        img2 = Image.open(r"images/user (2).png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.password_img = ImageTk.PhotoImage(img2)
        self.lab_pass = Label(login_frame, image=self.password_img, bg="white", bd=0)
        self.lab_pass.place(x=47, y=200)
        lab_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
        lab_pass.place(x=75, y=200)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="#ECECEC")
        txt_pass.place(x=50, y=235, width=250)

        img3 = Image.open(r"images/login.png")
        img3 = img3.resize((200, 43), Image.LANCZOS)
        self.login_button = ImageTk.PhotoImage(img3)
        self.btn_login = Button(login_frame, command=self.login, image=self.login_button, bg="white", activebackground="white", bd=0, cursor="hand2")
        self.btn_login.place(x=75, y=290)

        hr = Label(login_frame, bg="lightgrey")
        hr.place(x=50, y=360, width=250, height=2)
        Or = Label(login_frame, text="OR", font=("times new roman", 15, "bold"), bg="white", fg="lightgrey")
        Or.place(x=150, y=345)

        btn_forgot = Button(login_frame, text="Forgot Password?", command=self.forgot_window, font=("times new roman", 13, "bold"), cursor="hand2", bg="white", activebackground="white", activeforeground="steelblue", fg="steelblue", bd=0)
        btn_forgot.place(x=100, y=390)

        # ==========Register Frame===========
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=790, y=595, width=350, height=55)

        lab_register = Label(register_frame, text="Don't have an account?", font=("times new roman", 13), bg="white")
        lab_register.place(x=60, y=15)
        btn_signup = Button(register_frame, text="Sign Up", font=("times new roman", 13, "bold"), cursor="hand2", bg="white", activebackground="white", activeforeground="steelblue", fg="steelblue", bd=0)
        btn_signup.place(x=220, y=14)

        # ==========Animation Images==========
        img01 = Image.open(r"images/otp1.jpeg")
        img01 = img01.resize((400, 400), Image.LANCZOS)
        self.im1 = ImageTk.PhotoImage(img01)

        img02 = Image.open(r"images/otp4.png")
        img02 = img02.resize((550, 350), Image.LANCZOS)
        self.im2 = ImageTk.PhotoImage(img02)

        img03 = Image.open(r"images/otp3.jpeg")
        img03 = img03.resize((400, 400), Image.LANCZOS)
        self.im3 = ImageTk.PhotoImage(img03)

        img05 = Image.open(r"images/1.webp")
        img05 = img05.resize((400, 400), Image.LANCZOS)
        self.im4 = ImageTk.PhotoImage(img05)

        self.lab_change_image = Label(self.root, bg="white")
        self.lab_change_image.place(x=381, y=152, width=333, height=473)

        self.animate()

    # ==============All Functions==================

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im4
        self.im4 = self.im
        self.lab_change_image.config(image=self.im)
        self.lab_change_image.after(2000, self.animate)


    def login(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.user_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            cur.execute("Select utype from employee where id=? AND pass=?", (self.user_id.get(), self.password.get()))
            user = cur.fetchone()
            if user == None:
                messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
            else:
                if user [0] == "Admin":
                    self.root.destroy()
                    os.system("python dashboard.py")
                else:
                    self.root.destroy()
                    os.system("python billclass.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def forgot_window(self):
        conn = sqlite3.connect(database=r'AppDatabase.db')
        cur = conn.cursor()
        try:
            if self.user_id.get() == "":
                messagebox.showerror("Error", "User ID is required", parent=self.root)
            else:
                cur.execute("Select email from employee where id=?", (self.user_id.get(),))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror("Error", "Invalid User ID", parent=self.root)
                else:
                    # ======Forgot Password Window==========
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_confirm_pass = StringVar()

                    chk = self.send_email(email[0])
                    if chk == 'f':
                        messagebox.showerror("Error", "Connection Error, Try again", parent=self.root)
                    else:
                        self.forgot_win = Toplevel(self.root)
                        self.forgot_win.title("Forgot Password")
                        self.forgot_win.geometry("400x350+650+200")
                        self.forgot_win.focus_force()

                        title = Label(self.forgot_win, text="Reset Password", font=("goudy old style", 15, "bold"), bg="#40b5ad", fg="white")
                        title.pack(side=TOP, fill=X)

                        lab_reset = Label(self.forgot_win, text="Enter OTP Sent to Registered Email", font=("times new roman", 15))
                        lab_reset.place(x=20, y=60)
                        txt_reset = Entry(self.forgot_win, textvariable=self.var_otp, font=("times new roman", 15), bg="light yellow")
                        txt_reset.place(x=20, y=100, width=250, height=30)

                        img11 = Image.open(r"images/save.png")
                        img11 = img11.resize((20, 20), Image.LANCZOS)
                        self.reset_img = ImageTk.PhotoImage(img11)
                        self.reset_btn = Button(self.forgot_win, text="Submit", command=self.validate_otp, image=self.reset_img, font=("times new roman", 15),bg="lightblue", compound=RIGHT, anchor="e", padx=5, cursor="hand2")
                        self.reset_btn.place(x=280, y=95)

                        new_pass = Label(self.forgot_win, text="New Password", font=("times new roman", 15))
                        new_pass.place(x=20, y=160)
                        txt_new_pass = Entry(self.forgot_win, textvariable=self.var_new_pass, font=("times new roman", 15),bg="light yellow")
                        txt_new_pass.place(x=20, y=190, width=250, height=30)

                        confirm_pass = Label(self.forgot_win, text="Confirm Password", font=("times new roman", 15))
                        confirm_pass.place(x=20, y=225)
                        txt_confirm_pass = Entry(self.forgot_win, textvariable=self.var_confirm_pass, font=("times new roman", 15),bg="light yellow")
                        txt_confirm_pass.place(x=20, y=250, width=250, height=30)

                        img10 = Image.open(r"images/update.png")
                        img10 = img10.resize((20, 20), Image.LANCZOS)
                        self.update_img = ImageTk.PhotoImage(img10)
                        self.btn_update = Button(self.forgot_win, image=self.update_img, command=self.update_password, text="Update", state=DISABLED, bg="lightblue", compound=RIGHT, anchor="e", font=("times new roman", 15), padx=5, cursor="hand2")
                        self.btn_update.place(x=150, y=300)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def update_password(self):
        if self.var_new_pass.get() == "" or self.var_confirm_pass.get() == "":
            messagebox.showerror("Error", "Enter New Password & Confirm Password", parent=self.forgot_win)
        elif self.var_new_pass.get() != self.var_confirm_pass.get():
            messagebox.showerror("Error", "Passwords do not match, Try again", parent=self.forgot_win)
        else:
            conn = sqlite3.connect(database=r'AppDatabase.db')
            cur = conn.cursor()
            try:
                cur.execute("Update employee SET pass=? where id=?", (self.var_new_pass.get(), self.user_id.get()))
                conn.commit()
                messagebox.showinfo("Success", "Password has been changed successfully", parent=self.forgot_win)
                self.forgot_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def validate_otp(self):
        if int(self.otp) == int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.reset_btn.config(state=DISABLED)
        else:
            messagebox.showerror("Authentication Error", "Invalid OTP", parent=self.forgot_win)

    def send_email(self, to_):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_,pass_)

        self.otp = int(time.strftime("%M%S%H")) + int(time.strftime("%S"))
        print(self.otp)

        subj = 'SMK Inventory Management System - Reset Password OTP'
        msg = f'Dear Sir/Madam,\n\nYour Reset Password OTP is {str(self.otp)}.\n\nWith Reagrds,\nSMK Management Team.'
        msg = "Subject:{}\n\n{}".format(subj, msg)
        s.sendmail(email_, to_, msg)
        chk = s.ehlo()
        if chk[0] == 250:
            return 's'
        else:
            return 'f'


root = Tk()
obj = Login(root)
root.mainloop()