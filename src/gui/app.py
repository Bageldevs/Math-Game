import tkinter as tk
from draw_gui import *

class App: 
    def __init__(self, width: int, height: int, title: str, resize: bool):
        self.width = width
        self.height = height
        self.title = title
        self.resize = resize
        self.tk_Window = tk.Tk()

    def create_app(self):
        self.tk_Window.geometry(f"{self.width}x{self.height}")
        self.tk_Window.title(self.title)
        self.tk_Window.resizable(self.resize, self.resize)

        self.canvas = tk.Canvas(self.tk_Window, self.width, self.height)
        self.canvas.pack()

        self.draw_gui = DrawGUI(self.canvas)

    def get_win(self):
        return self.tk_Window
    
    def get_canvas(self):
        return self.canvas

    def run(self):
        self.create_app()

        self.draw_gui.draw()
        self.tk_Window.mainloop()