from tkinter import *
# package for Pictures
from PIL import ImageTk, Image
# import database
import firebase as fb
import hotels

root = Tk()
root.geometry("860x640")

class Cities:

    def all_cities(self, root):
        """
        import List of cities from firebase
        :param root: ->Tk()
        :return: list of the cities
        """
        label_cities = Label(root, text="Cities:", font=("Times New Roman", 21, "bold"))
        label_cities.grid(row=0, column=0)

        cities = fb.db.child("Cities").get()

        def go_to_hotels(name):
            """
            Create a new window with list of hotels of the city
            :param name: name of the city
            :return: list of the hotels
            """
            master = Tk()
            master.geometry("860x640")
            temp = hotels.Hotels()
            temp.all_hotels(master, name)
            root.destroy()

        listOfCities = []
        for i in cities:
            c = i.key()
            listOfCities.append(Button(root, text=c, borderwidth=5, command=lambda m=c: go_to_hotels(m)))

        count = 0
        for i in listOfCities:
            i.grid(row=1 + count, column=0, stick='we')
            count += 1


hotel = Cities()
hotel.all_cities(root)
root.mainloop()
