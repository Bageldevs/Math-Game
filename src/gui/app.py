import tkinter as tk

class App: 
    def __init__(self, width, height, title, resize):
        self.width = width
        self.height = height
        self.title = title
        self.resize = resize
        self.tk_Window = tk.Tk()

    def create_app(self):
        self.tk_Window.geometry(f"{self.width}x{self.height}")
        self.tk_Window.title = self.title
        self.tk_Window.resizable = self.resize
    
    def get_win(self):
        return self.tk_Window
    
    def run(self):
        self.create_app()
        self.tk_Window.mainloop()
