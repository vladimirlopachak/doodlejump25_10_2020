from tkinter import *
from random import *
window = Tk()
window.title(string="Cosmic Jump")   # Name

window = Canvas(window, width=480, height=720, bg="black")  # Create_field
window.pack()

score = 0

defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
window.pack()

dx = 0          # Horizontal_speed_doodler
dy = -6        # Vertical_speed_doodler

pad_reflection1 = 1
pad_reflection2 = 0
pad_reflection3 = 0
pad_reflection4 = 0
pad_reflection5 = 0

rec_x = 100     # Doodler_x_coordinates
rec_y = 550     # Doodler_y_coordinates

pad_x1 = 100    # Pad(1)_x_coordinates
pad_y1 = 600    # Pad(1)_y_coordinates

pad_x2 = (randint(0, 410))     # Pad(2)_x_coordinates
pad_y2 = 480                    # Pad(2)_y_coordinates

pad_x3 = (randint(0, 410))     # Pad(3)_x_coordinates
pad_y3 = 360                    # Pad(3)_y_coordinates

pad_x4 = (randint(0, 410))     # Pad(4)_x_coordinates
pad_y4 = 240                    # Pad(4)_y_coordinates

pad_x5 = (randint(0, 410))     # Pad(5)_x_coordinates
pad_y5 = 120                    # Pad(5)_y_coordinates

doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")   # Create_Doodler

def b1(event):      # Left_Mouse_Button_move_left
    global dx
    dx = 10
    dx = -dx
window.bind('<Button-1>', b1)

def b2(event):  # Left_Mouse_Button_do_not_move
    global dx
    dx = 0
window.bind('<Button-2>', b2)

def b3(event):  # Right_Mouse_Button_move_right
    global dx
    dx = -10
    dx = -dx
window.bind('<Button-3>', b3)

def platforms():
    global score
    global dx
    global dy
    global rec_x
    global rec_y
    global pad_x1
    global pad_y1
    global pad_x2
    global pad_y2
    global pad_x3
    global pad_y3
    global pad_x4
    global pad_y4
    global pad_x5
    global pad_y5
    global doodler
    global pad1
    global pad2
    global pad3
    global pad4
    global pad5

    pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
    pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
    pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
    pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
    pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)

def move():
    global defscore
    global score
    global pad_reflection1
    global pad_reflection2
    global pad_reflection3
    global pad_reflection4
    global pad_reflection5
    global dx
    global dy
    global rec_x
    global rec_y
    global pad_x1
    global pad_y1
    global pad_x2
    global pad_y2
    global pad_x3
    global pad_y3
    global pad_x4
    global pad_y4
    global pad_x5
    global pad_y5
    global doodler
    global pad1
    global pad2
    global pad3
    global pad4
    global pad5


    rec_x = rec_x + dx
    rec_y = rec_y + dy

    if rec_x >= 480:            # Horizontal_teleport
        rec_x = rec_x-480

    if rec_x <= -50:            # Horizontal_teleport
        rec_x = rec_x+480

    if rec_y > 800:             # Game_Over
        rec_y = - 100
        window.delete(defscore)
        game_over_text1 = window.create_text(240, 300, anchor=N, text="  Game Over", font="None 20", fill="red")
        window.pack()

        game_over_text = window.create_text(235, 332, anchor=N, text="Total score:", font="None 20", fill="white")
        window.pack()

        game_over_score = window.create_text(327, 333, anchor=N, text=score, font="None 20", fill="white")
        window.pack()

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

    if rec_y < 400:             # High_of_jump_limit
        dy = -dy

######################################################################################################################
    #if rec_x == pad_x1 and pad_y1 > rec_y > pad_y1-50 and dy > 0 and rec_y < pad_y1 - 43:                                                       # Platform_Reflection
    #    dy = -dy
    if pad_x1 < rec_x < pad_x1 + 70 and pad_y1 > rec_y > pad_y1-50 and dy > 0  and rec_y < pad_y1 - 43 and pad_reflection1 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 += 1
        pad_reflection2 = 0
        pad_reflection3 = 0
        pad_reflection4 = 0
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = (randint(0, 410))
        pad_y5 = pad_y5 - 480

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)
    if pad_x1 < rec_x < pad_x1 + 70 and pad_y1 > rec_y > pad_y1-50 and dy > 0  and rec_y < pad_y1 - 43:
        dy = -dy

    if pad_x1+1 > rec_x > pad_x1 - 50 and pad_y1 > rec_y > pad_y1-50 and dy > 0 and rec_y < pad_y1 - 43 and pad_reflection1 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 += 1
        pad_reflection2 = 0
        pad_reflection3 = 0
        pad_reflection4 = 0
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = (randint(0, 410))
        pad_y5 = pad_y5 - 480

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)
    if pad_x1+1 > rec_x > pad_x1 - 50 and pad_y1 > rec_y > pad_y1-50 and dy > 0 and rec_y < pad_y1 - 43:
        dy = -dy
######################################################################################################################

    if pad_x2 < rec_x < pad_x2 + 70 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0 and rec_y < pad_y2 - 43 and pad_reflection2 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 += 1
        pad_reflection3 = 0
        pad_reflection4 = 0
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = (randint(0, 410))
        pad_y1 = pad_y1 - 480

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)

    if pad_x2 < rec_x < pad_x2 + 70 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0 and rec_y < pad_y2 - 43:
        dy = -dy

    if pad_x2+1 > rec_x > pad_x2 - 50 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0 and rec_y < pad_y2 - 43 and pad_reflection2 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 += 1
        pad_reflection3 = 0
        pad_reflection4 = 0
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = (randint(0, 410))
        pad_y1 = pad_y1 - 480

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)

    if pad_x2+1 > rec_x > pad_x2 - 50 and pad_y2 > rec_y > pad_y2 - 50 and dy > 0 and rec_y < pad_y2 - 43:
        dy = -dy
######################################################################################################################

    if pad_x3 < rec_x < pad_x3 + 70 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0 and rec_y < pad_y3 - 43 and pad_reflection3 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 = 0
        pad_reflection3 += 1
        pad_reflection4 = 0
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = (randint(0, 410))
        pad_y2 = pad_y2 - 480

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)

    if pad_x3 < rec_x < pad_x3 + 70 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0 and rec_y < pad_y3 - 43:                                                     # Platform_Reflection
        dy = -dy

    if pad_x3+1 > rec_x > pad_x3 - 50 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0 and rec_y < pad_y3 - 43 and pad_reflection3 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 = 0
        pad_reflection3 += 1
        pad_reflection4 = 0
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = (randint(0, 410))
        pad_y2 = pad_y2 - 480

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)

    if pad_x3+1 > rec_x > pad_x3 - 50 and pad_y3 > rec_y > pad_y3 - 50 and dy > 0 and rec_y < pad_y3 - 43:                                                     # Platform_Reflection
        dy = -dy
######################################################################################################################

    if pad_x4 < rec_x < pad_x4 + 70 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0 and rec_y < pad_y4 - 43 and pad_reflection4 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 = 0
        pad_reflection3 = 0
        pad_reflection4 += 1
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = (randint(0, 410))
        pad_y3 = pad_y3 - 480

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)
    if pad_x4 < rec_x < pad_x4 + 70 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0 and rec_y < pad_y4 - 43:  # Platform_Reflection
        dy = -dy

    if pad_x4+1 > rec_x > pad_x4 - 50 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0 and rec_y < pad_y4 - 43 and pad_reflection4 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 = 0
        pad_reflection3 = 0
        pad_reflection4 += 1
        pad_reflection5 = 0

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = (randint(0, 410))
        pad_y3 = pad_y3 - 480

        pad_x4 = pad_x4
        pad_y4 = pad_y4 + 120

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)
    if pad_x4+1 > rec_x > pad_x4 - 50 and pad_y4 > rec_y > pad_y4 - 50 and dy > 0 and rec_y < pad_y4 - 43:  # Platform_Reflection
        dy = -dy
######################################################################################################################

    if pad_x5 < rec_x < pad_x5 + 70 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0 and rec_y < pad_y5 - 43 and pad_reflection5 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 = 0
        pad_reflection3 = 0
        pad_reflection4 = 0
        pad_reflection5 += 1

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = (randint(0, 410))
        pad_y4 = pad_y4 - 480

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)
    if pad_x5 < rec_x < pad_x5 + 70 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0 and rec_y < pad_y5 - 43:
        dy = -dy

    if pad_x5+1 > rec_x > pad_x5 - 50 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0 and rec_y < pad_y5 - 43 and pad_reflection5 == 0:
        dy = -dy
        score += 1
        window.delete(defscore)
        defscore = window.create_text(240, 20, anchor=N, text=score, font="None 20", fill="white")
        window.pack()
        pad_reflection1 = 0
        pad_reflection2 = 0
        pad_reflection3 = 0
        pad_reflection4 = 0
        pad_reflection5 += 1

        rec_x = rec_x
        rec_y = rec_y + 120

        pad_x1 = pad_x1
        pad_y1 = pad_y1 + 120

        pad_x2 = pad_x2
        pad_y2 = pad_y2 + 120

        pad_x3 = pad_x3
        pad_y3 = pad_y3 + 120

        pad_x4 = (randint(0, 410))
        pad_y4 = pad_y4 - 480

        pad_x5 = pad_x5
        pad_y5 = pad_y5 + 120

        window.delete(doodler)
        window.delete(pad1)
        window.delete(pad2)
        window.delete(pad3)
        window.delete(pad4)
        window.delete(pad5)

        doodler = window.create_rectangle(rec_x, rec_y, 0, 0, fill="white")  # Create_Doodler
        pad1 = window.create_rectangle(pad_x1, pad_y1, pad_x1 + 70, pad_y1 + 15, fill="white")  # Create_the_platform(1)
        pad2 = window.create_rectangle(pad_x2, pad_y2, pad_x2 + 70, pad_y2 + 15, fill="white")  # Create_the_platform(2)
        pad3 = window.create_rectangle(pad_x3, pad_y3, pad_x3 + 70, pad_y3 + 15, fill="white")  # Create_the_platform(3)
        pad4 = window.create_rectangle(pad_x4, pad_y4, pad_x4 + 70, pad_y4 + 15, fill="white")  # Create_the_platform(4)
        pad5 = window.create_rectangle(pad_x5, pad_y5, pad_x5 + 70, pad_y5 + 15, fill="white")  # Create_the_platform(5)
    if pad_x5+1 > rec_x > pad_x5 - 50 and pad_y5 > rec_y > pad_y5 - 50 and dy > 0 and rec_y < pad_y5 - 43:
        dy = -dy
######################################################################################################################
    window.coords(doodler, rec_x, rec_y, rec_x + 50, rec_y + 50)    # I_do_not_remember
    window.after(40, move)  # Re-paint_window


window.after(40, platforms)      # Re-paint_platforms
window.after(40, move)           # Re-paint_function_move
window.mainloop()