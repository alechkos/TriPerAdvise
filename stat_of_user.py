from tkinter import *
import firebase as fb
from general import General
import fa
from tkinter import messagebox

class Statistics(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        flag = True
        if self.title_name == "Moderators":
            flag = False
        Label(self.root, text="Statistics of " + self.uname, font=('Times New Roman', 21, 'italic')).place(x=300, y=10)

        if flag:
            parts = fb.db.child("Users").child(self.uname).get()
        else:
            parts = fb.db.child("Moderators").child(self.uname).get()
        list_of_stat = []
        name_mail = []
        for p in parts:
            if type(p.val()) is not dict:
                name_mail.append(Label(self.root, text=p.key() + ': ' + p.val(), font=('Kotlin', 16, 'bold')))
                if p.key() == 'Mail':
                    email = p.val()
            else:
                if flag:
                    items = fb.db.child("Users").child(self.uname).child("Buys").get()
                    for i in items:
                        list_of_stat.append(Label(self.root, text=i.key() + ': ' + i.val(), font=('Kotlin', 12, 'bold')))
                else:
                    items = fb.db.child("Moderators").child(self.uname).child("Work").get()
                    for i in items:
                        for j in i.val():
                            list_of_stat.append(
                                Label(self.root, text=j + ': ' + i.val()[j], font=('Kotlin', 12, 'bold')))

        temp = 50
        for lab in name_mail:
            lab.place(x=5, y=temp)
            temp += 30

        if flag:
            Label(self.root, text="Buys of " + self.uname + ':', font=('Kotlin', 16, 'bold')).place(x=5, y=temp)
            temp += 30
        else:
            Label(self.root, text="Work of " + self.uname + ':', font=('Kotlin', 16, 'bold')).place(x=5, y=temp)
            temp += 30

        for lab in list_of_stat:
            lab.place(x=20, y=temp)
            temp += 30

        delete = Button(self.root, text="Delete " + self.uname, borderwidth=5, command=lambda: self.delete_user(email, flag))
        delete.place(x=550, y=340)


        change = Button(self.root, text="Change to Moderator", borderwidth=5, command=lambda: self.change(flag))
        change.place(x=400, y=340)

        back = Button(root, text="<<", borderwidth=5, command=self.users, width=20)
        back.grid(row=0, column=0, stick='we')

    def delete_user(self, mail, ind):
        flag = True
        try:
            user = fa.auth.get_user_by_email(mail)
            uid = user.uid
            fa.auth.delete_user(uid)
            if ind:
                fb.db.child("Users").child(self.uname).remove()
            else:
                fb.db.child("Moderators").child(self.uname).remove()
        except Exception:
            flag = False
            messagebox.showerror("Error!", "Something went wrong!")

        if flag:
            messagebox.showinfo("Successful", "You have deleted " + self.uname)

    def change(self, ind):
        if ind:
            fb.db.child("Users").child(self.uname).child("Buys").remove()
            flag = True
            try:
                name = fb.db.child("Users").child(self.uname).get()
                fb.db.child("Moderators").child(self.uname).update(name.val())
                fb.db.child("Users").child(self.uname).remove()
            except Exception:
                flag = False
                messagebox.showerror("Error", "Something went wrong!")

            if flag:
                messagebox.showinfo("Successful", "You have added " + self.uname + " as Moderator")
        else:
            fb.db.child("Moderators").child(self.uname).child("Work").remove()
            flag = True
            try:
                name = fb.db.child("Moderators").child(self.uname).get()
                fb.db.child("Users").child(self.uname).update(name.val())
                fb.db.child("Moderators").child(self.uname).remove()
            except Exception:
                flag = False
                messagebox.showerror("Error", "Something went wrong!")

            if flag:
                messagebox.showinfo("Successful", "You have added " + self.uname + " as Moderator")