from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("My first viewer!")

my_img = ImageTk.PhotoImage(Image.open("C:/Users/Павел/Desktop/Images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/Павел/Desktop/Images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/Павел/Desktop/Images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/Павел/Desktop/Images/4.png"))

image_list = [my_img, my_img2, my_img3, my_img4]

status = Label(root, text="Image 1 of " + str(len(image_list)))

my_Label = Label(image=my_img)
my_Label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global button_forward
    global button_back
    global my_Label

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_Label.grid(row=0, column=0, columnspan=3)


def back(image_number):
    global button_forward
    global button_back
    global my_Label

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_Label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="EXIT THE PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3)

root.mainloop()
