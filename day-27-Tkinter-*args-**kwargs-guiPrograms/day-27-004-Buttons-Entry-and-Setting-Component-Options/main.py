from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Create Label in Tkinter
my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.pack()

my_label["text"] = "Label Text Method 2"
my_label.config(text="Label Text Method 3")


# Button
def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=f"{input.get()}")


button = Button(text="Click Me!", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.pack()

# To keep the window open
window.mainloop()
