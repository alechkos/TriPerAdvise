# import the library of tkinter
from tkinter import *
import sign
import login
import mod_enter
import admin_enter


class Menu:

    def __init__(self, root):
        self.root = root

        sign_up = Button(root, text="Sign up", command=self.signup_press, font=("Times New Roman", 15),
                         borderwidth=5)
        sign_up.place(x=100, y=60, width=120, height=50)

        log_in = Button(root, text="Log in", command=self.login_press, font=("Times New Roman", 15), borderwidth=5)
        log_in.place(x=200, y=60, width=120, height=50)

        log_in_mod = Button(root, text="Moderator Login", command=self.login_mod_press, font=("Times New Roman", 15), borderwidth=5)
        log_in_mod.place(x=220, y=130, width=150, height=50)

        log_in_admin = Button(root, text="Administrator Login", command=self.login_admin_press, font=("Times New Roman", 15), borderwidth=5)
        log_in_admin.place(x=40, y=130, width=180, height=50)

        label1 = Label(root, text="Welcome to TriPerAdvise", bg="#FFF", font=("Times New Roman", 21, "bold"))
        label1.pack()

    def signup_press(self):
        master = Tk()
        master.geometry("450x480")
        # sets the title of the
        master.title("Sign up")
        master.config(bg='grey')
        sign.Sign_up(master)
        self.root.destroy()

    def login_press(self):
        master = Tk()
        master.geometry("440x440")
        # sets the title of the
        master.title("Log in")
        master.config(bg='grey')
        login.Login(master)
        self.root.destroy()

    def login_mod_press(self):
        master = Tk()
        master.geometry("440x440")
        # sets the title of the
        master.title("Log in")
        master.config(bg='grey')
        mod_enter.Moderator(master)
        self.root.destroy()

    def login_admin_press(self):
        master = Tk()
        master.geometry("440x440")
        # sets the title of the
        master.title("Log in")
        master.config(bg='grey')
        admin_enter.Administrator(master)
        self.root.destroy()