import tkinter as tk

class Menu:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        
    def draw(self, x0: int, y0: int, x1: int, y1: int):
        #positioning
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        #create rect
        self.rect = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='red')

        #a = canvas.create_rectangle(50, 0, 50, 0, fill='red')
        #print(f'{self.x0, self.y0, self.x1, self.y1}'

    def update(self):
        pass