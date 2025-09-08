import pyautogui
from time import sleep
jumps = 0
bgColor = pyautogui.pixel(370,370)
lastcolor1 = None
lastcolor2 = None
lastbgColor = bgColor
print(bgColor)
print(round(sum(bgColor) / 3))
'''
while True:
    color1 = pyautogui.pixel(800,310)
    color2 = pyautogui.pixel(840,285)
    bgColor = pyautogui.pixel(370,370)
    color1bool = color1 != lastcolor1
    color2bool = color2 != lastcolor2
    if color1bool or color2bool:
        print(lastcolor1,color1)
        sleep(0.1)
        jumps += 1
    lastcolor1 = color1
    lastcolor2 = color2
'''