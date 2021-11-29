from tkinter import *
# package for Pictures
# import database
import firebase as fb
import hotels
import places
import sys


class Cities:

    def all_cities(self, root):
        """
        import List of cities from firebase
        :param root: ->Tk()
        :return: list of the cities
        """
        label_cities = Label(root, text="Cities:", font=("Times New Roman", 21, "bold"))
        label_cities.grid(row=0, column=0, stick='we')

        cities = fb.db.child("Cities").get()


        def go_to_hotels(name):
            """
            Create a new window with list of hotels of the city
            :param name: name of the city
            :return: list of the hotels
            """
            master = Tk()
            master.geometry("800x640")
            l_hotels = hotels.Hotels()
            l_hotels.all_hotels(master, name)
            l_places = places.Places()
            l_places.all_places(master, name)
            root.destroy()

        listOfCities = []
        for i in cities:
            c = i.key()
            listOfCities.append(Button(root, text=c, borderwidth=5, command=lambda m=c: go_to_hotels(m)))

        count = 0
        for i in listOfCities:
            i.grid(row=1 + count, column=0, stick='we')
            count += 1

        def exit_program():
            raise SystemExit
            sys.exit()

        Button(root, text="Exit the program",borderwidth=5, command=exit_program).grid(row=count+2, column=0)