from general import General
from tkinter import*
from tkinter import messagebox
import firebase as fb


class Change(General):

    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)

        label = Label(self.root, text="Change Name", font=('Times New Roman', 16, 'bold'))
        label.place(x=130, y=50)
        Label(root, text="Enter a\n new name:", bg='grey').place(x=-20, y=150, width=120, height=50)

        name = Entry(root, width=50, fg="blue", justify=CENTER, bd=3)
        name.place(x=100, y=160, width=250, height=40)

        change = Button(self.root, text="Change", font=("Times New Roman", 15), borderwidth=5,
                        command=lambda: self.do_change(name))
        change.place(x=320, y=220, width=50, height=30)

        back = Button(root, text="<<", borderwidth=5, command=self.go_to_cart, width=20)
        back.grid(row=0, column=0)

        exit = Button(root, text="Exit the program", borderwidth=5, command=self.exit_program)
        exit.place(rely=0.0, relx=1.0, x=0, y=0, anchor=NE)


    def do_change(self, name):
        try:
            temp_list = fb.db.child("Users").get()
            temp_data = fb.db.child("Users").child(self.uname).get()
            temp_mail = temp_data.val()["Mail"]
            temp_name = temp_data.val()["Name"]
            fb.db.child("Users").child(self.uname).remove()
            fb.db.child('Users').child(name.get()).update({"Mail": temp_mail, "Name": name.get()})
            self.uname = name.get()
            messagebox.showinfo("Successful", "You have changed your name!")
        except Exception:
            messagebox.showerror("Error!", "Something went wrong!")

    def go_to_cart(self):
        import cart
        master = Tk()
        master.geometry("800x640")
        master.title("Shopping Cart")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                  self.ind)
        self.root.destroy()
