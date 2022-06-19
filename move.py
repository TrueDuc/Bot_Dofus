import pyautogui
import time

class Coord:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Coord(", str(self.x), ",", str(self.y), ")"])



# allows us to chose the map you want to move on
def move(way):
    if (way == "left"):
        pyautogui.click(330,500)
    elif (way == "right"):
        pyautogui.click(1580,500)
    elif (way == "up"):
        pyautogui.click(980,30)
    elif (way == "down"):
        pyautogui.click(980,910)
    else:
        print("Error direction")
    return

#############################################################
# first version 

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

# reads in "path.txt" and follows the instructions written in it to move to your destination
# def path(way):
#     time.sleep(3)
#     next_way = " "
#     my_path = open("path.txt","r")
#     while next_way != "":
#         print(next_way)
#         next_way = my_path.readline()
#         move(next_way)
#         time.sleep(5)
#     my_path.close()



# allows you to move from your current pos (x1, y1) to your destination (x2, y2) and take the ressources on the path
def path(curr_pos: Coord, destination: Coord):
    time.sleep(3)
    while curr_pos.x != destination.x:
        if curr_pos.x < destination.x:
            move("right")
            curr_pos.x += 1
        else:
            move("left")
            curr_pos.x -= 1
        time.sleep(5)

    while curr_pos.y != destination.y:
        if curr_pos.y < destination.y:
            move("down")
            curr_pos.y += 1
        else:
            move("up")
            curr_pos.y -= 1
        time.sleep(6)

        
# allows you to move from your current pos (x1, y1) to your destination (x2, y2) and take the ressources on the path
def path_farm(curr_pos: Coord, destination: Coord):
    time.sleep(3)
    while curr_pos.x != destination.x:
        if curr_pos.x < destination.x:
            move("right")
            curr_pos.x += 1
        else:
            move("left")
            curr_pos.x -= 1
        time.sleep(5)

    while curr_pos.y != destination.y:
        if curr_pos.y < destination.y:
            move("down")
            curr_pos.y += 1
        else:
            move("up")
            curr_pos.y -= 1
        time.sleep(6)