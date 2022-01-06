from tkinter import *
from tkinter import messagebox
import firebase as fb
import menu
import cities
import password


class Login:
    list_p = []
    uname = None

    def __init__(self, root):
        self.root = root
        # A Label widget to show in toplevel
        Label(root, text="Enter data to log in", font=("Times New Roman", 18),
              justify=CENTER, bg='grey').place(x=140, y=100, width=220, height=50)

        # a label for entering email
        Label(root, text="Enter email:", bg='grey').place(x=-20, y=150, width=120, height=50)
        # a label for entering password
        Label(root, text="Enter password:", bg='grey').place(x=-14, y=200, width=120, height=50)

        # creating field for entering email
        mail = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        mail.place(x=100, y=160, width=300, height=40)
        # creating field for entering password
        password = Entry(root, show='*', width=50, fg="blue", justify=CENTER, bd=3)
        password.place(x=100, y=200, width=300, height=40)

        # creating button for confirmation of data
        ok = Button(root, text="Ok", font=("Times New Roman", 15), borderwidth=5,
                    command=lambda: self.enter(mail, password))
        ok.place(x=350, y=241, width=50, height=40)
        # creating button for come back

        forgot_pass = Button(root, text="Forgot my password", font=("Times New Roman", 12), borderwidth=5,
                             command=self.forgotPass)
        forgot_pass.place(x=100, y=241)

        back = Button(root, text="<<", command=self.go_to_menu, font=("Times New Roman", 15), borderwidth=5)
        back.place(x=1, y=1, width=80, height=40)

    def go_to_menu(self):
        temp_m = Tk()
        temp_m.geometry("440x440")
        # sets the title of the
        temp_m.title("Sign up")
        temp_m.config(bg='grey')
        menu.Menu(temp_m)
        self.root.destroy()

    def enter(self, m, p):
        flag = False
        try:
            fb.auth.sign_in_with_email_and_password(m.get(), p.get())
            flag = True
        except Exception:
            temp_m = Tk()
            temp_m.geometry("440x440")
            # sets the title of the
            temp_m.title("Sign up")
            temp_m.config(bg='grey')
            Label(temp_m, text="The mail or password is incorrect!", font=("Times New Roman", 12, "bold"),
                  fg="red").place(x=60, y=100, width=300, height=40)
            menu.Menu(temp_m)
            self.root.destroy()
        if flag:
            flag1 = True
            temp_list = fb.db.child("Users").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")

            if self.uname == None:
                flag1 = False

            if flag1:
                temp_m = Tk()
                # sets the title of the
                temp_m.title("Cities")
                temp_m.config(bg='grey')
                temp_m.attributes('-fullscreen', True)
                cities.Cities(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
                self.root.destroy()

            else:
                messagebox.showerror("Wrong Login!",
                                     "You a trying to enter like a user.\n "
                                     "Try to enter from moderator's or admin's Login!")
                self.go_to_menu()

    def forgotPass(self):
        temp_m = Tk()
        temp_m.geometry("400x400")
        # sets the title of the
        temp_m.title("Password")
        temp_m.config(bg='grey')
        password.Forgot_Pass(temp_m, 'login')
        self.root.destroy()
