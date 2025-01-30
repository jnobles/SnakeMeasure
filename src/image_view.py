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
        self.snake_dots = []
        self.snake_line = None
        self.snake_spline = None
        self.canvas = tk.Canvas(self)
        self.create_view()

    def create_dot(self, event):
        dot_size = 5
        dot = self.canvas.create_oval(event.x-(dot_size/2), event.y-(dot_size/2), event.x+(dot_size/2), event.y+(dot_size/2), fill="red")
        self.snake_dots.append([dot, [event.x, event.y]])
        self.update_line()

    def remove_dot(self, event):
        try:
            dot = self.snake_dots[-1][0]
        except IndexError:
            pass
        else:
            self.canvas.delete(dot)
            self.snake_dots.pop()
            self.update_line()

    def update_line(self):
        try:
            coords = [coord for point in self.snake_dots for coord in point[1]]
            self.canvas.delete(self.snake_line)
            self.canvas.delete(self.snake_spline)
            self.snake_line = self.canvas.create_line(coords, fill="blue", width=2)
            self.snake_spline = self.canvas.create_line(coords, fill="red", width=2, smooth=True)
        except (tk.TclError, IndexError):
            pass

    def create_view(self):
        self.rowconfigure(0,  weight=1)
        self.columnconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.bind("<Button-1>", self.create_dot)
        self.canvas.bind("<Button-3>", self.remove_dot)
