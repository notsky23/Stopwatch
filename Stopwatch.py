# template for "Stopwatch: The Game"
from tkinter import *
import time

# define global variables
Width = 300
Height = 200
interval = 100
t = 0
times = 0
timeIsRunning = False
color = "White"

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timeIsRunning, times
    timeIsRunning = True

    times = (int(min.get()) * 600) + (int(sec.get()) * 10) + (int(ms.get()))
    while timeIsRunning:
        seconds, milliseconds = (times // 10, times % 10)

        minutes = 0
        if seconds >= 60:
            minutes, seconds = (seconds // 60, seconds % 60)

        min.set("{0:02d}".format(minutes))
        sec.set("{0:02d}".format(seconds))
        ms.set("{0:1d}".format(milliseconds))

        # update time
        window.update()

        time.sleep(0.1)

        times += 1


def stop_handler():
    global timeIsRunning, color

    timeIsRunning = False

    pts = int(points.get())
    trs = int(tries.get())

    if (times % 10 == 0):
        pts += 1
        trs += 1
        points.set("{0:1d}".format(pts))
        tries.set("{0:1d}".format(trs))
    else:
        trs += 1
        tries.set("{0:1d}".format(trs))


def reset_handler():
    global times

    times = 0

    min.set("{0:02d}".format(0))
    sec.set("{0:02d}".format(0))
    ms.set("{0:1d}".format(0))
    points.set("{0:1d}".format(0))
    tries.set("{0:1d}".format(0))

    
# create frame
window = Tk()
window.title("Stopwatch Game")
window.geometry('600x300')
window.resizable(False, False)
window.config(bg='black')

# create buttons
startButton = Button(window, text="Start", bd='3', width=15, height=1, command=start_handler)
startButton.place(x=20, y=80)

stopButton = Button(window, text="Stop", bd='3', width=15, height=1, command=stop_handler)
stopButton.place(x=20, y=120)

resetButton = Button(window, text="Reset", bd='3', width=15, height=1, command=reset_handler)
resetButton.place(x=20, y=160)

# create label
lbl = Label(window, text="Stopwatch Game", bg='black', fg='white', width=15, height=1, font='Helvetica 30').place(x=150, y=10)
pointsLabel = Label(window, text="Points: ", bg='black', fg='white', width=15, height=1, font='Helvetica 12').place(x=30, y=230)
triesLabel = Label(window, text="Tries: ", bg='black', fg='white', width=15, height=1, font='Helvetica 12').place(x=350, y=230)

# create entry for HH MM SS
min = StringVar()
Entry(window, textvariable=min, width=2, font='Helvetica 70').place(x=180, y=80)
min.set('00')

sec = StringVar()
Entry(window, textvariable=sec, width=2, font='Helvetica 70').place(x=310, y=80)
sec.set('00')

ms = StringVar()
Entry(window, textvariable=ms, width=2, font='Helvetica 70', justify=CENTER).place(x=440, y=80)
ms.set('0')

# create entry for points and tries
points = StringVar()
pointEntry = Entry(window, textvariable=points, width=2, bg=color, font='Helvetica 12', justify=CENTER).place(x=150, y=230)
points.set('0')

tries = StringVar()
triesEntry = Entry(window, textvariable=tries, width=2, bg=color, font='Helvetica 12', justify=CENTER).place(x=480, y=230)
tries.set('0')

# start frame
window.mainloop()

# Please remember to review the grading rubric