from tkinter import *
window = Tk()
window.title(string="Doodlejump")   # Name

window = Canvas(window, width=480, height=720, bg="black")  # Create_field
window.pack()

dx = 0          # Horizontal_speed_doodler
dy = -11        # Vertical_speed_doodler
rec_x = 100     # Doodler_x_coordinates
rec_y = 550     # Doodler_y_coordinates
pad_x = 100     # Pad(1)_x_coordinates
pad_y = 600     # Pad(1)_y_coordinates


def platform():

    pad = window.create_rectangle(pad_x, pad_y, pad_x + 80, pad_y + 15, fill="white")   # Create_the_lowest_platform(1)

def b1(event): #Left Mouse Button   # Move_Left
    global dx
    dx = 12
    dx = -dx
window.bind('<Button-1>', b1)

def b2(event): #Left Mouse Button   # Move_Rifht
    global dx
    dx = 0
window.bind('<Button-2>', b2)

def b3(event): #Right Mouse Button  # Dont_Move
    global dx
    dx = -12
    dx = -dx
window.bind('<Button-3>', b3)



doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill = "white")   # Create_Doodler

def move():
    global dx
    global dy
    global rec_x
    global rec_y

    rec_x = rec_x + dx
    rec_y = rec_y + dy

    if rec_x >= 400:            # Horizontal_teleport
        rec_x = rec_x-450

    if rec_x <= -50:            # Horizontal_teleport
        rec_x = rec_x+450

    if rec_y > 800:             # Game_Over
        but = Button(window, font = "none, 30", text = "   Game Over !!! \n Click to Restart", width=25, height=10, bg='black', fg='red',)
        but.pack()
        dx = 0
        dy = 0
        rec_x = 0
        rec_y = 0

    if rec_y < 400:             # High_of_jump_Limit
        dy = -dy

    if rec_x == pad_x and pad_y > rec_y > pad_y-45 and dy > 0:                         # Platform_Reflection
        dy = -dy

    if pad_x < rec_x < pad_x + 80 and pad_y > rec_y > pad_y-45 and dy > 0:             # Platform_Reflection
        dy = -dy

    if pad_x > rec_x > pad_x - 50 and pad_y > rec_y > pad_y-45 and dy > 0:             # Platform_Reflection
        dy = -dy

    window.coords(doodler, rec_x, rec_y, rec_x + 50, rec_y + 50)    # I_do_not_remember
    window.after(40, move)  # Re-paint_window

window.after(0, platform)   # Re-paint_window_platform
window.after(0, move)       # Re-paint_window_move
window.mainloop()