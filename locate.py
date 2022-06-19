from hashlib import new
import pyautogui
import time


# funtion to know if a pos is in the screen (return 1) or in the sides (return 0)
def inScreen(pos):
    if pos[0] >= 355 and pos[0] <= 1565 and pos[1] >= 50 and pos[1] <= 900:
        return 1
    return 0

# function to know if a pos is nearby an other pos we have already visit (return 1) or if it is a "new" pos (return 0)
def near(new_pos, L_pos):
    for pos in L_pos:
        if new_pos[0]-pos[0] < 10 and new_pos[1]-pos[1] < 10:
            return 1
    return 0

# find the pos of pic.png on the screen
def locate(pic):
    L_pos = []

    for loc in pyautogui.locateAllOnScreen(pic, grayscale=False, confidence = 0.25):
        center = pyautogui.center(loc)
        # we verify that the location is on the main screen and not already visited
        if inScreen(center):
            if not(near(center, L_pos)):
                L_pos.append(center)   
    return L_pos





