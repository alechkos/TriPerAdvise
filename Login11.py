# import the library of tkinter
from tkinter import *
from window_signup import Sign_Up

#def create_window():
    #Sign_Up(signup_window)


# creating graphic interface for application
login_window = Tk()

# creating the size of window
login_window.geometry("440x170")

# creating title of window
login_window.title("TriPerAdvise")
# prohibition of change of window size
login_window.resizable(False, False)
#photo = PhotoImage(file='logo.png')
#login_window.iconphoto(False, photo)
# creating background of window to be white
login_window["bg"] = "#FFF"


#added function for opening new window
def signup_press():
	master = Tk() #defined master in this case because using login_window will kill the whole application
	#opens as new window you define what and how just like on top
	master.geometry("440x440")
    # sets the title of the
	master.title("New Window")
 
    # A Label widget to show in toplevel
	Label(master,text ="This is a new window").pack()
	login_window.destroy() #destroys the first window so it wont run anymore
 
def login_press(): print("You choose log in")


sign_up = Button(login_window, text="Sign up", command=signup_press, font=("Times New Roman", 15), borderwidth=5)
# sign_up.pack()
sign_up.place(x=100, y=60, width=120, height=50)

log_in = Button(login_window, text="Log in", command=login_press, font=("Times New Roman", 15), borderwidth=5)
# log_in.pack()
log_in.place(x=200, y=60, width=120, height=50)

label1 = Label(login_window, text="Welcome to TriPerAdvise", bg="#FFF", font=("Times New Roman", 21, "bold"))
label1.pack()

login_window.mainloop()
