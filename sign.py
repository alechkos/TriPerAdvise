# import the library of tkinter
from tkinter import *
from tkinter import messagebox
import firebase as fb
import menu
import cities


class Sign_up:
    root = None
    list_p = []
    uname = None

    def __init__(self, root):

        self.root = root
        # A Label widget to show in toplevel
        Label(root, text="Registration", font=("Times New Roman", 17, "bold"),
              borderwidth=5, bg='grey').place(x=170, y=50, width=120, height=50)
        # a label for entering email
        Label(root, text="Enter email:", font=('Ariel', 10, 'italic'),
              bg='grey').place(x=-20, y=150, width=120, height=50)
        # a label for entering password
        Label(root, text="Enter password:", font=('Ariel', 10, 'italic'),
              bg='grey').place(x=-10, y=200, width=120, height=50)
        Label(root, text="Repeat password:", font=('Ariel', 10, 'italic'),
              bg='grey').place(x=-8, y=240, width=120, height=50)
        Label(root, text="Enter your name:", font=('Ariel', 10, 'italic'),
              bg='grey').place(x=-10, y=280, width=120, height=50)

        # creating field for entering email
        mail = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        mail.place(x=100, y=160, width=300, height=40)
        # creating field for entering password
        password = Entry(root, show='*', width=50, fg="blue", justify=CENTER, bd=3)
        password.place(x=100, y=200, width=300, height=40)
        password2 = Entry(root, show='*', width=50, fg="blue", justify=CENTER, bd=3)
        password2.place(x=100, y=240, width=300, height=40)
        # creating a name
        name = Entry(root, width=50, fg='blue', justify=CENTER, bd=3)
        name.place(x=100, y=280, width=300, height=40)
        # creating button for confirmation of data

        ok = Button(root, text="Ok", font=("Times New Roman", 15), borderwidth=5,
                    command=lambda: self.registration(mail, password, password2, name))
        ok.place(x=350, y=330, width=50, height=40)

        # creating button for back to previous page
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

    def registration(self, m, p, p2, name):
        flag = False
        if p.get() != p2.get():
            messagebox.showwarning("Wrong password!", "The passwords aren't the same!")
            return
        if len(name.get()) == 0:
            messagebox.showwarning("Wrong name!", "Enter a name please!")
            return
        try:
            fb.auth.create_user_with_email_and_password(m.get(), p.get())
            flag = True
        except Exception:
            Label(self.root, text="The password should to be more than\n 6 characters or mail is incorrect\n"
                                  "or this mail has been registred",
                  font=("Times New Roman", 12, "bold"),
                  fg="red").place(x=115, y=95)
        if flag:
            fb.db.child("Users").child(name.get()).update({"Mail": m.get(), "Name": name.get()})
            temp_m = Tk()
            temp_m.geometry("800x640")
            # sets the title of the
            temp_m.title("Cities")
            temp_m.config(bg='grey')
            temp_m.attributes('-fullscreen', True)
            temp_list = fb.db.child("Users").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")
            cities.Cities(temp_m, self.list_p, '', self.uname,  m.get(), '', '', 'Cities', '')
            self.root.destroy()
