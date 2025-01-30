import tkinter as tk

from image_view import ImageView


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def run(self):
        self.image_view = ImageView(self.root)
        self.image_view.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
