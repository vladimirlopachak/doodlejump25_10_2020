from tkinter import *
from random import *
window = Tk()
window.title(string="Doodlejump")   # Name

window = Canvas(window, width=480, height=720, bg="black")  # Create_field
window.pack()

dx = 0          # Horizontal_speed_doodler
dy = -6        # Vertical_speed_doodler

rec_x = 100     # Doodler_x_coordinates
rec_y = 550     # Doodler_y_coordinates

pad_x1 = 100    # Pad(1)_x_coordinates
pad_y1 = 600    # Pad(1)_y_coordinates

pad_x2 = (randint(30, 400))     # Pad(2)_x_coordinates
pad_y2 = 480                    # Pad(2)_y_coordinates

pad_x3 = (randint(30, 400))     # Pad(3)_x_coordinates
pad_y3 = 360                    # Pad(3)_y_coordinates

pad_x4 = (randint(30, 400))     # Pad(4)_x_coordinates
pad_y4 = 240                    # Pad(4)_y_coordinates

pad_x5 = (randint(30, 400))     # Pad(5)_x_coordinates
pad_y5 = 120                    # Pad(5)_y_coordinates


def platform1():
    pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 80, pad_y1 + 15, fill="white")  # Create_the_platform(1)


def platform2():
    pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")   # Create_the_platform(2)


def platform3():
    pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")   # Create_the_platform(3)


def platform4():
    pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")   # Create_the_platform(4)


def platform5():
    pad2 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")   # Create_the_platform(5)


def b1(event):      # Left Mouse Button_Move_Left
    global dx
    dx = 12
    dx = -dx


window.bind('<Button-1>', b1)


def b2(event):  # Left Mouse Button_Don_not_Move
    global dx
    dx = 0


window.bind('<Button-2>', b2)


def b3(event):  # Right Mouse Button_Move_Right
    global dx
    dx = -12
    dx = -dx


window.bind('<Button-3>', b3)

doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")   # Create_Doodler


def move():
    global dx
    global dy
    global rec_x
    global rec_y

    rec_x = rec_x + dx
    rec_y = rec_y + dy

    if rec_x >= 480:            # Horizontal_teleport
        rec_x = rec_x-480

    if rec_x <= -50:            # Horizontal_teleport
        rec_x = rec_x+480

    if rec_y > 800:             # Game_Over
        but = Button(window, font="none, 30", text="   Game Over !!! \n Click to Restart", width=25, height=10, fg="red", bg="black")
        but.pack()
        dx = 0
        dy = 0
        rec_x = 0
        rec_y = 0

    if rec_y < 0:             # High_of_jump_Limit
        dy = -dy

######################################################################################################################
    if rec_x == pad_x1 and pad_y1 > rec_y > pad_y1-45 and dy > 0:                         # Platform_Reflection
        dy = -dy

    if pad_x1 < rec_x < pad_x1 + 80 and pad_y1 > rec_y > pad_y1-50 and dy > 0:             # Platform_Reflection
        dy = -dy

    if pad_x1 > rec_x > pad_x1 - 50 and pad_y1 > rec_y > pad_y1-50 and dy > 0:             # Platform_Reflection
        dy = -dy
######################################################################################################################

    if rec_x == pad_x2 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x2 < rec_x < pad_x2 + 70 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x2 > rec_x > pad_x2 - 50 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy
######################################################################################################################
    if rec_x == pad_x3 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x3 < rec_x < pad_x3 + 70 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x3 > rec_x > pad_x3 - 50 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy
######################################################################################################################
    if rec_x == pad_x4 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x4 < rec_x < pad_x4 + 70 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x4 > rec_x > pad_x4 - 50 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy
############################################################################################
    if rec_x == pad_x5 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x5 < rec_x < pad_x5 + 70 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy

    if pad_x5 > rec_x > pad_x5 - 50 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0:  # Platform_Reflection
        dy = -dy
############################################################################################
    window.coords(doodler, rec_x, rec_y, rec_x + 50, rec_y + 50)    # I_do_not_remember
    window.after(40, move)  # Re-paint_window


window.after(0, platform1)      # Re-paint_window_platform(1)
window.after(0, platform2)      # Re-paint_window_platform(2)
window.after(0, platform3)      # Re-paint_window_platform(3)
window.after(0, platform4)      # Re-paint_window_platform(4)
window.after(0, platform5)      # Re-paint_window_platform(5)
window.after(0, move)           # Re-paint_window_move
window.mainloop()