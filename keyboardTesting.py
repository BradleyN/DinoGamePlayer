import pyautogui #
import time
pyautogui.moveTo(400,350)
time.sleep(2)
lastColor1 = None
lastColor2 = None
lastColor3 = None
lastColor4 = None
lastbackgroundColor = None
while True:
    color1 = pyautogui.pixel(760,365)
    color2 = pyautogui.pixel(760,345)
    color3 = pyautogui.pixel(700,345)
    color4 = pyautogui.pixel(700,365)
    backgroundColor = pyautogui.pixel(400,350)
    colorBool = (color1 != lastColor1) or (color2 != lastColor2) or (color3 != lastColor3) or (color4 != lastColor4)
    print(colorBool)
    if colorBool and (backgroundColor == lastbackgroundColor):
        pyautogui.keyDown("space")
        time.sleep(0.1)
        pyautogui.keyUp("space")
    lastColor1 = color1
    lastColor2 = color2
    lastColor3 = color3
    lastColor4 = color4
    lastbackgroundColor = backgroundColor