import tkinter as tk
from .game.menu import *

class App: 
    def __init__(self, width: int, height: int, title: str, resize: bool):
        self.width = width
        self.height = height
        self.title = title
        self.resize = resize
        self.tk_Window = tk.Tk()

        self.create_app()

    def create_app(self):
        ## window configuration ##
        self.tk_Window.geometry(f"{self.width}x{self.height}")
        self.tk_Window.title(self.title)
        self.tk_Window.resizable(self.resize, self.resize)

        self.canvas = tk.Canvas(self.tk_Window)
        self.canvas.pack()

        self.menu = Menu(self.canvas)

    def get_win(self):
        ## get window ##
        return self.tk_Window
    
    def get_canvas(self):
        ## get canvas ##
        return self.canvas

    def run(self):
        self.tk_Window.update()
        ## MENU ##
        self.menu.draw(0, 200, 700, 0)
        self.menu.update()

        ## GAME ##
        
        
        