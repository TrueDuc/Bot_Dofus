import pyautogui

def move(dir):
    if (dir == "left"):
        pyautogui.click(330,500)
    elif (dir == "right"):
        pyautogui.click(1580,500)
    elif (dir == "up"):
        pyautogui.click(980,30)
    elif (dir == "down"):
        pyautogui.click(980,910)
    else:
        print("Erreur de direction")
    return

#############################################################

def move_pos(x,y):
    pyautogui.moveTo(x, y)
    return

def moveLeft():
    pyautogui.click(330,500)
    return

def moveRight():
    pyautogui.click(1580,500)
    return

def moveUp():
    pyautogui.click(980,30)
    return

def moveDown():
    pyautogui.click(980,910)
    return