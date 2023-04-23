from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.60934
    # km = round(miles * 1.60934)
    km_value_label.config(text=str(km))
    # km_value_label.config(text=f"{km}")



window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=60, pady=40)

# Entry
input = Entry(width=9)
input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_lable = Label(text="is equal to")
is_equal_to_lable.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# To keep the window open
window.mainloop()
