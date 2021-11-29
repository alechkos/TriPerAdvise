# import the library of tkinter
from tkinter import *
import sign
import login


class Menu:
    def start_window(self, root):
        def signup_press():
            master = Tk()
            master.geometry("440x440")
            # sets the title of the
            master.title("Sign up")
            reg = sign.Sign_up()
            reg.signup_press(master)
            root.destroy()

        def login_press():
            master = Tk()
            master.geometry("440x440")
            # sets the title of the
            master.title("Log in")
            ent = login.Login()
            ent.login_press(master)
            root.destroy()
        sign_up = Button(root, text="Sign up", command=signup_press, font=("Times New Roman", 15),
                         borderwidth=5)
        # sign_up.pack()
        sign_up.place(x=100, y=60, width=120, height=50)
        log_in = Button(root, text="Log in", command=login_press, font=("Times New Roman", 15), borderwidth=5)
        # log_in.pack()
        log_in.place(x=200, y=60, width=120, height=50)
        label1 = Label(root, text="Welcome to TriPerAdvise", bg="#FFF", font=("Times New Roman", 21, "bold"))
        label1.pack()

