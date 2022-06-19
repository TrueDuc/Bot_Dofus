import pyautogui
import time
import locate


def farm():
    time.sleep(3)
    print("Lets go") 
    # we find where are the wheat
    L_pos = locate.locate('picture/wheat_map2.png')
    # we repeat the process as many time as we find wheat
    while L_pos:
        for pos in locate.locate('picture/wheat_map2.png'):
            pyautogui.click(pos[0],pos[1])
            time.sleep(3)
        L_pos = locate.locate('picture/wheat_map2.png')

    print("No more wheat.")





