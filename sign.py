# import the library of tkinter
from tkinter import *
import firebase as fb
import menu
import cities


class Sign_up:

    def signup_press(self, root):
        def go_to_menu():
            temp_m = Tk()
            temp_m.geometry("440x440")
            # sets the title of the
            temp_m.title("Sign up")
            m = menu.Menu()
            m.start_window(temp_m)
            root.destroy()

        def registration(m, p):
            flag = False
            try:
                fb.auth.create_user_with_email_and_password(m.get(), p.get())
                flag = True
            except Exception:
                temp_m = Tk()
                temp_m.geometry("440x440")
                # sets the title of the
                temp_m.title("Menu")
                Label(temp_m, text="The password should to be more than\n 6 characters or mail is incorrect",
                      font=("Times New Roman", 12, "bold"),
                      fg="red").place(x=70, y=110, width=300, height=40)
                m = menu.Menu()
                m.start_window(temp_m)
                root.destroy()

            if flag:
                temp_m = Tk()
                temp_m.geometry("800x640")
                # sets the title of the
                temp_m.title("Cities")
                temp = cities.Cities()
                temp.all_cities(temp_m)
                root.destroy()

        # A Label widget to show in toplevel
        Label(root, text="Registration", font=("Times New Roman", 17, "bold"), borderwidth=5).place(x=170, y=50,
                                                                                                    width=120,
                                                                                                    height=50)

        # a label for entering email
        Label(root, text="Enter email:").place(x=-20, y=150, width=120, height=50)
        # a label for entering password
        Label(root, text="Enter password:").place(x=-14, y=200, width=120, height=50)

        # creating field for entering email
        mail = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        mail.place(x=100, y=160, width=300, height=40)
        # creating field for entering password
        password = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        password.place(x=100, y=200, width=300, height=40)
        # creating button for confirmation of data
        ok = Button(root, text="Ok", font=("Times New Roman", 15), borderwidth=5,
                    command=lambda: registration(mail, password))
        ok.place(x=350, y=240, width=50, height=40)

        # creating button for back to previous page
        back = Button(root, text="<<", command=go_to_menu, font=("Times New Roman", 15), borderwidth=5)
        back.place(x=10, y=10, width=50, height=40)
