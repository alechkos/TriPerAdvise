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