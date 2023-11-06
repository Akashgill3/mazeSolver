from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack()
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
        print("closing window")
    
    def close(self):
        self.__isRunning = False

