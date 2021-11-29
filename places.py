from tkinter import *
import firebase as fb
import cities


class Places:

    def all_places(self, root, name):
        """
        Import list of places from city's name
        :param root: ->Tk()
        :param name: city's name
        :return: list of the places in 'name'
        """


        label_places = Label(root, text='Places:', font=('New Times Roman', 21, 'bold')).grid(row=1, column=2)
        places = fb.db.child('Cities').child(name).child('Places').get()


        list_of_places = []
        for i in places:
            list_of_places.append(Button(root, text=i.key() + ': ' + str(i.val()), borderwidth=5))
        count = 0
        for i in list_of_places:
            i.grid(row=2 + count, column=2, stick='we')
            count += 1

        def exit_program():
            raise SystemExit
            sys.exit()

        Button(root, text="Exit the program",borderwidth=5, command=exit_program).grid(row=0, column=3)