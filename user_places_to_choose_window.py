from tkinter import *

user_places_win = Tk()
user_places_win.title('TriPerAdvise')
user_places_win.geometry('800x600+600+200')
user_places_win.resizable(False, False)
photo = PhotoImage(file='logo.png')
user_places_win.iconphoto(False, photo)
user_places_win.config(bg='grey')
user_places_win.mainloop()
