from Tkinter import *
import Tkinter as tk
import sys
import re

def center(toplevel):
    print "center func"
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def popupmsg(msg):
    print "popup func"
    popup = tk.Toplevel()
    popup.title("Information Dialog")
    label = Label(popup, text = msg)
    label.pack(side="top", pady=10)
    button = Button(popup, text = "OK", command = popup.destroy)
    button.pack()
    popup.grab_set()
    center(popup)
    popup.mainloop()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
    
def only_number(i_string):
    return all(number.isdigit() for number in i_string)
               
def only_letter(i_string):
    if re.match("^[a-zA-Z]*$", i_string):
        return True
