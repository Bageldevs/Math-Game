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

        self.canvas = tk.Canvas(self.tk_Window, width=700, height=600)
        self.canvas.pack()

        self.menu = Menu(self.canvas)

    def get_win(self):
        ## get window ##
        return self.tk_Window
    
    def get_canvas(self):
        ## get canvas ##
        return self.canvas

    def run(self):
        ## MENU ##
        self.menu.draw(0, 425, 700, 600)
        
        ## Coordinates that worked (0, 200, 700, 0)
        '''
        x0 = 0
        y0 = 0
        x1 = 700
        y1 = 250
        '''

        """For example, the rectangle specified by top left corner (100,100) and 
        bottom right corner (102,102) is a square two pixels by two pixels, including 
        pixel (101,101) but not including (102,102)."""

        self.menu.update()

        ## GAME ##

        ## TKINTER WINDOW ##
        self.tk_Window.update()
        
        
        