from tkinter import *
import firebase as fb
from general import General


class Cities(General):
    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        label_cities = Label(self.root, text="Cities:", font=("Times New Roman", 21, "bold"))
        label_cities.grid(row=0, column=0, stick='we')

        flag = False
        moders = fb.db.child('Moderators').get()
        if moders.val():
            for n in moders:
                if n.val().get("Mail") == self.mail:
                    flag = True

        cities = fb.db.child("Cities").get()
        listOfCities = []
        for i in cities:
            c = i.key()
            listOfCities.append(
                Button(self.root, text=c, font=('Arial', 10, 'bold'), borderwidth=5, width=20, height=2,
                       command=lambda m=c: self.go_to_parts1(m)))

        count = 0
        for i in listOfCities:
            i.grid(row=1 + count, column=0, stick='we', pady=5)
            count += 1

        if not flag:
            shop_cart = Button(self.root, text="Shopping Cart", borderwidth=5, command=self.go_to_cart)
            shop_cart.place(rely=0.0, relx=0.92, x=0, y=0, anchor=NE)

    def go_to_cart(self):
        import cart
        master = Tk()
        master.title("Shopping Cart")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, "Cities",
                  self.ind)
        self.root.destroy()
