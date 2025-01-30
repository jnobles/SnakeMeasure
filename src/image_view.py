import tkinter as tk
from tkinter import ttk


class TkGridHelper:
    @staticmethod
    def create_label(parent, text, row, col, rowspan=1, colspan=1, anchor=tk.CENTER):
        label = ttk.Label(master=parent, text=text, anchor=anchor)
        label.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        return label

    @staticmethod
    def create_button(parent, text, row, col, rowspan=1, colspan=1):
        button = ttk.Button(master=parent, text=text)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        return button

    @staticmethod
    def create_entry(parent, row, col, rowspan=1, colspan=1):
        string_var = tk.StringVar()
        entry = ttk.Entry(master=parent, textvariable=string_var)
        entry.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
        return entry, string_var


class ImageView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.create_view()

    def create_dot(self, event):
        dot_size = 5
        self.canvas.create_oval(event.x-(dot_size/2), event.y-(dot_size/2), event.x+(dot_size/2), event.y+(dot_size/2), fill="red")

    def create_view(self):
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.bind("<Button-1>", self.create_dot)
