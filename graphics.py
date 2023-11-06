from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg='white', width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
        print("closing window")
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__isRunning = False


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
 
class Line:
    def __init__(self, point1, point2) -> None:
        self.x1, self.y1 = point1.x, point1.y
        self.x2, self.y2 = point2.x, point2.y

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
        