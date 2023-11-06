from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack()
        self.isRunning = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()
    
    def close(self):
        self.isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()