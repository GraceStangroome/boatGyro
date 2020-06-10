# This code is the GUI for the system for steadying the roll of the boat. It was written by Grace Stangroome.

# Importing and setting up tkinter
import tkinter
import main_file2 as main
import DataLog as log
import CustomWindows as Custom
import ast
from tkinter import messagebox as m
import threading
from threading import Thread 
top = tkinter.Tk()
a = tkinter.Button
my_threads = []
b = 0

def threaded_run(mode):
    t = Thread(target=main.run)
    s = Thread(target=main.quit)
    if mode == "start":
        my_threads.append(1)
        t.start()
    elif mode == "stop":
        s.run()
        my_threads.remove(1)
        my_threads.append(0)
        log.current_destroy()
        log.records("current process data log deleted")
    elif mode == "check":
        if 1 in my_threads:
            return False  # If the "Start" thread is running, it is not safe to close.
        else:
            return True


def ensure():
    check = threaded_run("check")
    if check is True:
        log.records("program quit")
        top.destroy()
    elif check is False:
        m.showwarning("Warning", "You are trying to quit while the program is still running. Please cancel the program and try again.")


def help():
    # as the help text was rather extended, placing it in a txt file seemed more adequate.
    content = ast.literal_eval(open("/home/pi/Desktop/NEA/Final Code/help.txt").read())
    box = m.showinfo("Help", content)
    return box
    

# To show the content in the data logs.
def load(file):
    if file == "Records":
        title = "Records"
        content = log.open_file("records")
    elif file == "Current":
        title = "Current Process"
        content = log.open_file("current")
    else:
        title = "Error"
        content = "Cannot locate file."
    return Custom.DisplayWindow(title, content)

        
# declaring colours and styles
green = '#%02x%02x%02x' % (0, 255, 0)
red = '#%02x%02x%02x' % (255, 63, 51)
blue = '#%02x%02x%02x' % (51, 181, 255,)

# buttons
S = a(top, bg=(green), text= "Start Program", font=("Segoe UI Black", 40), height="2", width="15", command=lambda: threaded_run(mode="start"))
C = a(top, bg=(red), text="Stop Program", font=("Segoe UI Black", 40), height="2", width="15", command=lambda: threaded_run(mode="stop"))
R = a(top, text="View Reports", font=("Segoe UI",20), height="2", width="30", command=lambda: load(file="Records"))
P = a(top, text="View Current Process", font=("Segoe UI",20), height="2", width="30", command=lambda: load(file="Current"))
H = a(top, text="Help", font=("Segoe UI",20), height="2", width="30", command=lambda: help())
Q = a(top, bg=(blue), text="Quit", font=("Segoe UI Black", 35), height="2", width="17", command=lambda: ensure())

# order of buttons
S.pack()
C.pack()
R.pack()
P.pack()
H.pack()
Q.pack()

# finishing
top.mainloop()
