import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)


# Create Label in Tkinter
my_label = tkinter.Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.pack()         # Puts the label on the screen and automatically centers it on the screen
# my_label.pack(side='left')
# my_label.pack(expand="true")



# To keep the window open
window.mainloop()
