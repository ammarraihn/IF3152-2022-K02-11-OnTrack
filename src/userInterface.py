from tkinter import *
from tkinter import ttk
from manageActivity import manageActivity
import tkinter as tk

HEADING1 = ('Poppins', 20, 'bold')
HEADING2 = ('Poppins', 14)
FONT = ('Poppins', 12)

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

class Completed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    