from tkinter import *


def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=f"{input.get()}")


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Create Label in Tkinter
my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.config(text="New Text")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)


# Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)



# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

# To keep the window open
window.mainloop()
