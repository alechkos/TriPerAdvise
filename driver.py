<<<<<<< HEAD
from tkinter import *
import menu
import sign

# creating graphic interface for application
login_window = Tk()
# creating the size of window
login_window.geometry("440x170")

m = menu.Menu()
m.start_window(login_window)

login_window.mainloop()
=======
import menu
from tkinter import *

root = Tk()
root.title('TriPerAdvise')
root.geometry("440x440")
root.resizable(False, False)
# photo = PhotoImage(file='logo.png')
# root.iconphoto(False, photo)
root.config(bg='grey')

m = menu.Menu()
m.start_window(root)

root.mainloop()
>>>>>>> Pavel
