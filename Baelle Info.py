from math import *
from tkinter import *


WIDTH = 400
HEIGHT = 400

class gui(object):
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Baelle")
        self.fenster.geometry("400x400")
        
    
        self.canvas = Canvas(master=fenster)
        self.canvas.place(x=0, y=0, width=WIDTH, height=HEIGHT)


gui.fenster.mainloop