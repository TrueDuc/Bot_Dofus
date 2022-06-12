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

# find the pos of img.png on the screen
def locate(img):
    L_pos = []
    for loc in pyautogui.locateAllOnScreen(img, grayscale=False, confidence = 0.25):
        center = pyautogui.center(loc)
        # we verify that the location is on the main screen and not already visited
        if inScreen(center):
            if not(near(center, L_pos)):
                L_pos.append(center)   
    return L_pos


time.sleep(3)
print("Lets go")    

L_pos = []

for wheat_loc in pyautogui.locateAllOnScreen('image/wheat_map2.png', grayscale=False, confidence = 0.25):

    wheat_point = pyautogui.center(wheat_loc)
    # we verify that the location of the wheat is on the main screen (note on the sides)
    print("test", wheat_point[0], wheat_point[1])
    if inScreen(wheat_point): 
        if not(near(wheat_point, L_pos)):
            print("GO TO", wheat_point[0], wheat_point[1])
            pyautogui.click(wheat_point[0], wheat_point[1])
            L_pos.append(wheat_point)
            time.sleep(5)


print("No more wheat.")


