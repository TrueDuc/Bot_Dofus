import pyautogui

def getSize():
    screenWidth, screenHeight = pyautogui.size()
    return(screenWidth, screenHeight)
