import pyautogui as pag
import numpy as np
import mss
import cv2
import keyboard



mon = {'left': 44, 'top': 277, 'width': 900, 'height': 900}


def screenshot(sct):
    screenshot = sct.grab(mon)
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    # uncomment to save screengrab
    # mss.tools.to_png(screenshot.rgb, screenshot.size, output='output.png')  # type: ignor


def checkcolor(x,y,img):
    pixel = tuple(img[y-mon["top"],x-mon["left"]])
    print(pixel,end='\r',flush=True)



with mss.mss() as sct:
    while True:



        # uncomment to get mouseposition
        x, y = pag.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='\r')
            
        img = screenshot(sct)
        # uncomment checkcolor() to get rgb values
        # checkcolor(x,y,img)

        if keyboard.is_pressed('e'):
            break
        
    
    