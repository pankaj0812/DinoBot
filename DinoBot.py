from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np

class coordinates():
    replaybutton = (360, 214)
    dinosaur = (149, 239)

def restartGame():
    pyautogui.click(coordinates.replaybutton)
    pyautogui.keyDown('down')

def press_space():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    time.sleep(0.10)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (coordinates.dinosaur[0]+30, coordinates.dinosaur[1],
           coordinates.dinosaur[0]+120, coordinates.dinosaur[1]+2)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getColors())
    print(a.sum())
    return a.sum()

restartGame()
while True:
    if(imageGrab()!= 435):
        press_space()
        time.sleep(0.1)