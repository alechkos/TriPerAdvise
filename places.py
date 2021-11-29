from tkinter import *
import firebase as fb


class Places:

    def all_places(self, root, name):
        """
        Import list of places from city's name
        :param root: ->Tk()
        :param name: city's name
        :return: list of the places in 'name'
        """
        label_places = Label(root, text='Places', font=('New Times Roman', 21, 'bold')).grid(row=0, column=1)
        places = fb.db.child('Cities').child(name).child('Places').get()

        list_of_places = []
        for i in places:
            list_of_places.append(Button(root, text=i.key() + ': ' + str(i.val()), borderwidth=5))
        count = 0
        for i in list_of_places:
            i.grid(row=1 + count, column=0, stick='we')
            count += 1
