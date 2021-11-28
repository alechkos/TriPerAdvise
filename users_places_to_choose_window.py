from tkinter import *

users_places_win = Tk()
users_places_win.title('TriPerAdvise')
users_places_win.geometry('800x600+600+200')
users_places_win.resizable(False, False)
photo = PhotoImage(file='logo.png')
users_places_win.iconphoto(False, photo)
users_places_win.config(bg='grey')
users_places_win.mainloop()
