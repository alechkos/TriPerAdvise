from tkinter import *
import firebase as fb
import menu

class Login:


    def login_press(self, root):
        def go_to_menu():
            temp_m = Tk()
            temp_m.geometry("440x440")
            # sets the title of the
            temp_m.title("Sign up")
            m = menu.Menu()
            m.start_window(temp_m)
            root.destroy()

        # A Label widget to show in toplevel
        Label(root, text="Enter data to log in", font=("Times New Roman", 18), justify=CENTER).place(x=140, y=100,
                                                                                                       width=220, height=50)

        # a label for entering email
        Label(root, text="Enter email:").place(x=-20, y=150, width=120, height=50)
        # a label for entering password
        Label(root, text="Enter password:").place(x=-14, y=200, width=120, height=50)

        # creating field for entering email
        Entry(root, width=50, fg="blue", justify=CENTER, bd=3).place(x=100, y=160, width=300, height=40)

        # creating field for entering password
        Entry(root, width=50, fg="blue", justify=CENTER, bd=3).place(x=100, y=200, width=300, height=40)

        # creating button for confirmation of data
        ok = Button(root, text="Ok", font=("Times New Roman", 15), borderwidth=5).place(x=350, y=240, width=50, height=40)
        #creating button for come back
        back = Button(root, text="<-", command=go_to_menu, font=("Times New Roman", 15), borderwidth=5).place(x=10,
                                                                                                               y=10,
                                                                                                               width=50,
                                                                                                               height=40)


