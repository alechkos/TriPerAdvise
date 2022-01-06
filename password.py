from tkinter import *
from tkinter import messagebox
import login
import fa
import smtplib
from email.message import EmailMessage

class Forgot_Pass:

    def __init__(self, root, ind):
        self.root = root
        self.ind = ind

        Label(self.root, text="Password Recovery", font=("Times New Roman", 14, "bold"), bg="grey").place(x=130, y=50)
        Label(root, text="Enter email:", bg="grey").place(x=-20, y=150, width=120, height=50)

        mail = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        mail.place(x=100, y=160, width=250, height=40)

        if self.ind == 'login':
            back = Button(root, text="<<", command=self.go_to_login, font=("Times New Roman", 15), borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)
        elif self.ind == 'mod_login':
            back = Button(root, text="<<", command=self.go_to_mod_login, font=("Times New Roman", 15), borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)
        else:
            back = Button(root, text="<<", command=self.go_to_admin_login, font=("Times New Roman", 15), borderwidth=5)
            back.place(x=1, y=1, width=80, height=40)

        ok = Button(root, text="Ok", font=("Times New Roman", 15), borderwidth=5,
                    command=lambda: self.enter(mail))
        ok.place(x=320, y=220, width=50, height=30)



    def go_to_login(self):
        master = Tk()
        master.geometry("440x440")
        # sets the title of the
        master.title("Log in")
        master.config(bg='grey')
        login.Login(master)
        self.root.destroy()

    def go_to_mod_login(self):
        import mod_enter
        master = Tk()
        master.geometry("440x440")
        # sets the title of the
        master.title("Log in")
        master.config(bg='grey')
        mod_enter.Moderator(master)
        self.root.destroy()

    def go_to_admin_login(self):
        import admin_enter
        master = Tk()
        master.geometry("440x440")
        # sets the title of the
        master.title("Log in")
        master.config(bg='grey')
        admin_enter.Administrator(master)
        self.root.destroy()

    def enter(self, mail):
        flag = True
        try:
            user = fa.auth.get_user_by_email(mail.get())
        except Exception:
            messagebox.showerror("Wrong Email", "Enter correct e-mail!")
            flag = False

        if flag:
            link = fa.auth.generate_password_reset_link(mail.get())

            file = open("confirm_email.txt", "w+")
            file.write('Hello,\n'
                       'We received your request for reset the password in our application.\n'
                       'If it was you, please go to this link --> ' + link + '\n'
                       'If it was bot you, just ignore this e-mail.\n'
                        'We are glad that you are with us.')
            file.close()

            file = open("confirm_email.txt", "r+")
            msg = EmailMessage()
            msg.set_content(file.read())

            msg['Subject'] = f'Reset password in TriPerAdvise'
            msg['From'] = 'TriPerAdvise@gmail.com'
            msg['To'] = mail.get()


            # Send the message via our own SMTP server.
            s = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
            s.login('pavelni@ac.sce.ac.il', '3bw1NpMtdAsTf0Jn')
            s.send_message(msg)
            s.quit()
            messagebox.showinfo("Reset password", "The mail with link has sent!")
