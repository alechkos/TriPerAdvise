from tkinter import *

win = Tk()
win.title('TriPerAdvise')
win.geometry('800x600+600+200')
win.resizable(False, False)
photo = PhotoImage(file='logo.png')
win.iconphoto(False, photo)
win.config(bg='grey')
win.mainloop()
