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
