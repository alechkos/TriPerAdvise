from tkinter import *
import firebase as fb


class Window:
    def create_window(self):
        root = Tk()
        root.title('TriPerAdvise')
        root.geometry('1024x768+450+100')
        root.resizable(False, False)
        photo = PhotoImage(file='logo.png')
        root.iconphoto(False, photo)
        root.config(bg='grey')
        root.mainloop()

win=Window()
win.create_window()