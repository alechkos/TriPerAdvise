from tkinter import *
import firebase as fb
from general import General

class Admin_Menu(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        Label(self.root, text="Menu", font=('Times New Roman', 21, 'bold')).grid(row=0, column=0, stick='we')

        parts = fb.db.get()
        list_of_parts = ['Moderators', 'Users', 'Statistics']
        buttons = []
        for n in parts:
            if n.key() in list_of_parts:
                buttons.append(Button(self.root, text=n.key(), command=lambda m=n.key(): self.go_to_choice(m),
                                      borderwidth=5, width=10, height=5))

        count = 1
        for b in buttons:
            b.grid(row=count, column=0, pady=5)
            count += 1

    def go_to_choice(self, name):
        if name == 'Users':
            self.title_name = name
            self.users()
        
        elif name == 'Moderators':
            self.title_name = name
            self.users()
