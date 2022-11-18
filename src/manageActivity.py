from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import date


class manageActivity(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def addData(self):
        pass

    def deleteActivity(self):
        pass

    def markAsComplete(self, ):
        vals = [(self.parent.ongoing_records.item(self.parent.ongoing_records.focus()))['values'], # nama kegiatan yang diselect di tree ongoing_records
                (self.parent.idle_records.item(self.parent.idle_records.focus()))['values']] # nama kegiatan yang diselect di tree idle_records

        if vals != vals[0] == '' and vals[1] == '':
            messagebox.showerror("Mark as Complete", "Please select an activity to mark as complete")
        else:
            self.activityModel.completeInDb(vals)

            self.parent.fetchOngoingData()
            self.parent.fetchIdleData()
            

            if not (vals[0] == '' and vals[1] == ''):
                messagebox.showinfo("Mark as Complete", "Congrats, you've completed an activity!")

            # Reset selection
            for item in self.parent.ongoing_records.selection():
                self.parent.ongoing_records.selection_remove(item)

            for item in self.parent.idle_records.selection():
                self.parent.idle_records.selection_remove(item)
            



