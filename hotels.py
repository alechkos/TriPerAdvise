from tkinter import *
# package for Pictures
from PIL import ImageTk, Image
# import database
import firebase as fb


class Hotels:

    def all_hotels(self, root, name):
        """
        import List of hotels of city's name from firebase
        :param root: ->Tk()
        :param name: city's name
        :return: list of the hotels of city's name
        """
        label_hotels = Label(root, text="Hotels:", font=("Times New Roman", 21, "bold"))
        label_hotels.grid(row=0, column=0)
        hotels = fb.db.child("Cities").child(name).child("Hotels").get()

        listOfHotels = []
        for i in hotels:
            listOfHotels.append(Button(root, text=i.key() + ": " + str(i.val()), borderwidth=5))

        count = 0
        for i in listOfHotels:
            i.grid(row=1 + count, column=0, stick='we')
            count += 1
