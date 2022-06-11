import pyautogui

# we try to locate the template on the screen
try:
    wheat_loc = pyautogui.locateOnScreen('wheat_map.png', confidence = 0.9)

# in case of failure we print the error message and we exit
except pyautogui.ImageNotFoundException:
    print("No wheat here.")
    exit()

wheat_point = pyautogui.center(wheat_loc)
# we verify that the location of the wheat is on the main screen (note on the sides)
if wheat_point[0] >= 355 and wheat_point[0] <= 1565 and wheat_point[1] >= 50 and wheat_point[1] <= 900:
    pyautogui.click(wheat_point[0], wheat_point[1])  

