import turtle

# Function to get coordinates of turtle screen using mouse clicks
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()       # keeps the turtle window open