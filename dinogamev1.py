import pyautogui
from time import sleep
jumps = 0
lastColor1 = None
lastColor2 = None
detectionIndex = 6
bgColor = pyautogui.pixel(370,370)

lastbgColor = bgColor
while True:
    color1 = pyautogui.pixel(20 * detectionIndex + 680,310)
    color2 = pyautogui.pixel(20 * detectionIndex + 680,285)
    bgColor = pyautogui.pixel(370,370)
    color1bool = color1 != bgColor
    color2bool = color2 != bgColor
    if bgColor != lastbgColor:
        print("Transition! Jumps:",jumps)
        print(bgColor)
    if color1bool or color2bool:
        pyautogui.press("space")
        jumps += 1
    if jumps == 50:
        detectionIndex = 8
    lastbgColor = bgColor
    lastColor1 = color1
    lastColor2 = color2
