from tkinter import *
import firebase as fb
from general import General

class Users(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        flag = True
        if self.title_name == "Moderators":
            flag = False

        if flag:
            Label(self.root, text="Users", font=("Times New Roman", 21, 'italic')).place(x=300, y=10)
        else:
            Label(self.root, text="Moderators", font=("Times New Roman", 21, 'italic')).place(x=300, y=10)


        try:
            if flag:
                parts = fb.db.child("Users").get()
            else:
                parts = fb.db.child("Moderators").get()
            users_name = []
            for n in parts:
                users_name.append(Button(self.root, text=n.key(), borderwidth=5, command=lambda m=n.key(): self.goto_stat(m),
                                         width=10, height=3))
            temp = 50
            for b in users_name:
                b.place(x=5, y=temp)
                temp += 70
            back = Button(root, text="<<", borderwidth=5, command=self.go_to_admin_menu, width=20)
            back.grid(row=0, column=0, stick='we')

        except Exception:
            self.go_to_admin_menu()





