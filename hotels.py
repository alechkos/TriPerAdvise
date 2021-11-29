from tkinter import *
# import database
import firebase as fb
import cities


class Hotels:

    def all_hotels(self, root, name):
        """
        import List of hotels of city's name from firebase
        :param root: ->Tk()
        :param name: city's name
        :return: list of the hotels of city's name
        """

        def go_to_cities():
            master = Tk()
            master.geometry("440x440")
            # sets the title of the
            master.title("Cities")
            temp = cities.Cities()
            temp.all_cities(master)
            root.destroy()

        back = Button(root, text="<<", borderwidth=5, command=go_to_cities).grid(row=0, column=0, stick='we')
        label_hotels = Label(root, text="Hotels:", font=("Times New Roman", 21, "bold"))
        label_hotels.grid(row=1, column=0)
        hotels = fb.db.child("Cities").child(name).child("Hotels").get()

        listOfHotels = []
        for i in hotels:
            listOfHotels.append(Button(root, text=i.key() + ": " + str(i.val()), borderwidth=5))

        count = 0
        for i in listOfHotels:
            i.grid(row=2 + count, column=0, stick='we')
            count += 1
