import pyautogui
import win32gui
import string
import time



class Window:
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
        while self.hwnd == 0 and time.time() < timeout: # This loop and the timeout are here because if there is a title chagin app it will try for 5 seconds to get the name of the tab
            allWindows = pyautogui.getAllWindows()
            for window in allWindows:
                if windowName in window.title:
                    self.hwnd = win32gui.FindWindow(None, window.title)
        # Timeout just in case the game is closed
        if time.time() > timeout:
            print ("Can't find the window")
        

    '''
    Coords getter: This fuctions get the window coordinates with the hwnd
    '''
    def WindowCoords(self, hwnd):
        if hwnd != 0:
            rect = win32gui.GetWindowRect(hwnd)
            self.x = rect[0]
            self.y = rect[1]
            self.w = rect[2] - self.x
            self.h = rect[3] - self.y

            
    '''
    Window resizer: this fuction resizes the window just by having it's hwnd. It also refreshes the self coords
    '''
    def WindowResizer(self, x, y ,w ,h):
        if self.hwnd != 0:
            win32gui.MoveWindow(self.hwnd, x, y, w, h, True)    #this is the sentence that makes the resize possible
            self.WindowCoords(self.hwnd)