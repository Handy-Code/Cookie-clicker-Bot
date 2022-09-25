import pyautogui
import win32gui
import string
import time



class window:
    name = 0
    hwnd = 0
    x = 0
    y = 0
    w = 0
    h = 0


    '''
    Constructor for windows class
    '''
    def __init__(self, name):
        self.name = name
        self.WindowFinder(name)
        self.WindowCoords(self.hwnd)


    '''
    Window finder: This is supposed to check where the fuck the game is running and get it's coordinates. It checks every single window running on the pc
    then it checks if in it's name there is "Cookie Clicker" and then gets it's hwnd (this has to be done this way since cookie clicker's window
    decides to change every second or so(it's horrible, but works for now))
    '''
    def WindowFinder(self, windowName):
        timeout = time.time() + 5
        while self.hwnd == 0 and time.time() < timeout:
            windows = pyautogui.getAllWindows()
            for window in windows:
                if windowName in window.title:
                    self.hwnd = win32gui.FindWindow(None, window.title)
        # Timeout just in case the game is closed
        if time.time() > timeout:
            print ("Can't find the window")
        

        


    '''
    Coords getter: This fuctions get the window coordinates by having the
    '''
    def WindowCoords(self, hwnd):
        if hwnd != 0:
            rect = win32gui.GetWindowRect(hwnd)
            self.x = rect[0]
            self.y = rect[1]
            self.w = rect[2] - self.x
            self.h = rect[3] - self.y
