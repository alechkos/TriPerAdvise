from tkinter import *
import firebase as fb
from general import General


class Hotels(General):
    def __init__(self, root, list_p, cname, uname, mail, pname, pprice, title_name, ind):
        super().__init__(root, list_p, cname, uname, mail, pname, pprice, title_name, ind)
        Label(self.root, text=self.cname, font=('Cambria', 20, 'italic')).grid(row=1, column=3, pady=20)

        flag = False
        moders = fb.db.child('Moderators').get()
        if moders.val():
            for n in moders:
                if n.val().get("Mail") == self.mail:
                    flag = True

        parts = fb.db.child('Cities').child(self.cname).get()
        column_count = 0
        for i in parts:
            part_list = []
            part_list_del = []
            if not flag:
                Label(root, text=i.key(), font=("Times New Roman", 18, "bold")).grid(row=2, column=column_count)
                temp_plist = fb.db.child('Cities').child(self.cname).child(i.key()).get()
                for p in temp_plist:
                    c = p.key()
                    t = p.val()
                    part_list.append(Button(self.root, text=c + ':' + t, borderwidth=5,
                                            command=lambda m=c, y=t: self.chosed_hotel(m, y)))

            else:
                part_list.append(Button(self.root, text='Add ' + i.key(), borderwidth=5, width=15, height=5,
                                        command=lambda m=i.key(): self.addPart(m)))
                part_list_del.append(Button(self.root, text='Delete ' + i.key(), borderwidth=5, width=15, height=5,
                                            command=lambda m=i.key(): self.deletePart(m)))
            grid_count = 0
            for g in part_list:
                g.grid(row=3 + grid_count, column=column_count, stick='we', padx=20)
                grid_count += 1

            for g in part_list_del:
                g.grid(row=4 + grid_count, column=column_count, stick='we', padx=20, pady=20)
                grid_count += 1
            column_count += 1

        if flag:
            add_description = Button(self.root, text="Add Description", borderwidth=5, width=15, height=5,
                                     command=lambda: self.deletePart('Description'))
            add_description.grid(row=3, column=column_count, stick='we', padx=20)

            del_description = Button(self.root, text="Delete Description", borderwidth=5, width=15, height=5,
                                     command=lambda: self.deletePart('Del_Description'))
            del_description.grid(row=5, column=column_count, stick='we', padx=20)
            column_count += 1

            add_pictures = Button(self.root, text="Add Pictures", borderwidth=5, width=15, height=5,
                                     command=lambda: self.deletePart('Pictures'))
            add_pictures.grid(row=3, column=column_count, stick='we', padx=20)

            del_pictures = Button(self.root, text="Delete Pictures", borderwidth=5, width=15, height=5,
                                     command=lambda: self.deletePart('Del_Pictures'))
            del_pictures.grid(row=5, column=column_count, stick='we', padx=20)

        back = Button(root, text="<<", borderwidth=5, command=self.go_to_cities)
        back.grid(row=0, column=0, stick='we')


        if not flag:
            shop_cart = Button(root, text="Shopping Cart", borderwidth=5, command=self.go_to_cart)
            shop_cart.place(rely=0.0, relx=0.92, x=0, y=0, anchor=NE)

    def go_to_cart(self):
        import cart
        master = Tk()
        master.geometry("800x640")
        master.title("Shopping Cart")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        cart.User(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, "Parts",
                  self.ind)
        self.root.destroy()

    def addPart(self, name):
        import add_parts
        master = Tk()
        master.title("Shopping Cart")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        add_parts.addPart(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                          self.title_name, self.ind, name)
        self.root.destroy()



