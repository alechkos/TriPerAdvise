from tkinter import *
import sys


class General:
    cname = None
    pname = None
    pprice = None
    ind = None
    title_name = None

    def __init__(self, root, list_p, cname='', uname='', mail='', pname='', pprice='', title_name='', ind=''):
        self.root = root
        self.list_p = list_p
        self.uname = uname
        self.mail = mail
        self.title_name = title_name

        log_out = Button(root, text="Log Out", borderwidth=5, command=self.log_out)
        log_out.place(rely=0.0, relx=0.8, x=0, y=0, anchor=NE)

        exit = Button(root, text="Exit the program", borderwidth=5, command=self.exit_program)
        exit.place(rely=0.0, relx=1.0, x=0, y=0, anchor=NE)

    def go_to_cities(self):
        import cities
        General.title_name = "Cities"
        master = Tk()
        master.geometry("800x640")
        master.title("Cities")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        cities.Cities(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                      self.ind)
        self.root.destroy()

    def go_to_parts(self):
        import parts
        General.title_name = 'Parts'
        master = Tk()
        master.geometry("800x640")
        master.title("Our menu")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        parts.Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                     self.ind)
        self.root.destroy()

    def go_to_parts1(self, name):
        import parts
        General.title_name = 'Parts'
        General.cname = name
        master = Tk()
        master.title("Our menu")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        parts.Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice, self.title_name,
                     self.ind)
        self.root.destroy()

    def chosed_hotel(self, name, price):
        import parts_after_button
        General.title_name = 'Else'
        General.pname = name
        General.pprice = price
        master = Tk()
        master.title(name)
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        parts_after_button.Button_Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname,
                                         self.pprice, self.title_name, self.ind)
        self.root.destroy()

    def goto_charge(self, ind, name):
        import parts_after_button
        General.title_name = 'Else'
        General.ind = ind
        General.pname = name
        master = Tk()
        master.title(name)
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        parts_after_button.Button_Hotels(master, self.list_p, self.cname, self.uname, self.mail, self.pname,
                                         self.pprice, self.title_name, self.ind)
        self.root.destroy()

    def deletePart(self, name):
        import delete_part
        import add_description
        master = Tk()
        master.title("Delete Part")
        master.config(bg='grey')
        master.attributes('-fullscreen', True)
        if name == "Description" or name == "Del_Description" or name == 'Pictures' or name == 'Del_Pictures':
            add_description.Description(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                                        self.title_name, self.ind, name)
        else:
            General.ind = 'delete_part'
            delete_part.deletePart(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                                   self.title_name, self.ind, name)
        self.root.destroy()

    def go_to_admin_menu(self):
        import admin_menu
        master = Tk()
        master.title("Users")
        master.config(bg='#116562')
        master.geometry('640x400')
        admin_menu.Admin_Menu(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                    self.title_name, self.ind)
        self.root.destroy()

    def users(self):
        import users
        master = Tk()
        if self.title_name != "Moderators":
            master.title("Users")
        else:
            master.title("Moderators")
        master.config(bg='#116562')
        master.geometry('640x400')
        users.Users(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                                   self.title_name, self.ind)
        self.root.destroy()


    def goto_stat(self, name):
        import stat_of_user
        self.uname = name
        master = Tk()
        master.title("Users")
        master.config(bg='#116562')
        master.geometry('640x400')
        stat_of_user.Statistics(master, self.list_p, self.cname, self.uname, self.mail, self.pname, self.pprice,
                              self.title_name, self.ind)
        self.root.destroy()

    def log_out(self):
        import menu
        master = Tk()
        master.title('TriPerAdvise')
        master.geometry("440x440")
        master.resizable(False, False)
        # photo = PhotoImage(file='logo.png')
        # root.iconphoto(False, photo)
        master.config(bg='grey')
        menu.Menu(master)
        self.root.destroy()

    def exit_program(self):
        raise SystemExit
        sys.exit()
