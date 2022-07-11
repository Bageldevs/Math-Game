import tkinter as tk
from turtle import width
from .game.menu import *
from .game.game_screen import *

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
        

        self.menu_canvas = tk.Canvas(self.tk_Window, width=700, height=175, bg="#AFAFAF", bd=1, highlightbackground="#AFAFAF")
        
        self.menu_canvas.pack(side = tk.BOTTOM)
        
        #self.game_canvas = tk.Canvas(self.tk_Window, self.width, self.height)
        #self.game_canvas.pack()
    
        self.menu = Menu(self.menu_canvas)
        #self.gameWindow = game_win(self.game_canvas)

    def get_win(self):
        ## get window ##
        return self.tk_Window
    
    def get_canvas(self):
        ## get canvas ##
        return self.canvas

    def run(self):
        ## MENU ##
        #self.menu.draw(0, 0, 700, 175)
        self.menu.update()

        ## GAME ##
        #self.gameWindow.draw()
        #self.gameWindow.update()

        ## TKINTER WINDOW ##
        self.tk_Window.update()     