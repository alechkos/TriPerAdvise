from tkinter import *
from login import Login
from tkinter import messagebox
import admin_menu

class Administrator(Login):

    def __init__(self, root):
        super().__init__(root)
        lab = Label(root, text='Administrator Login', font=("Times New Roman", 16, 'bold'), bg='grey')
        lab.place(x=140, y=50)

    def enter(self, m, p):
        import firebase as fb
        import menu
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
            temp_list = fb.db.child("Administrators").get()
            for n in temp_list:
                if n.val().get("Mail") == m.get():
                    self.uname = n.val().get("Name")

            if self.uname == None:
                flag1 = False

            if flag1:
                temp_m = Tk()
                # sets the title of the
                temp_m.title("Cities")
                temp_m.config(bg='#116562')
                temp_m.geometry("640x400")
                # temp_m.attributes('-fullscreen', True)
                admin_menu.Admin_Menu(temp_m, self.list_p, '', self.uname, m.get(), '', '', 'Cities', '')
                self.root.destroy()

            else:
                messagebox.showerror("Wrong Login!",
                                     "You a trying to enter like an Administrator.\n Try to enter from user's/moderator's Login!")
                self.go_to_menu()

    def forgotPass(self):
        import password
        temp_m = Tk()
        temp_m.geometry("400x400")
        # sets the title of the
        temp_m.title("Password")
        temp_m.config(bg='grey')
        password.Forgot_Pass(temp_m, 'admin_login')
        self.root.destroy()