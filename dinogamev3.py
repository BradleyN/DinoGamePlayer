from PIL import ImageChops, ImageDraw
import pyautogui
from time import sleep
running = True
detectionIndex = 6
sleep(2)

def shot():
    reference = pyautogui.screenshot(region=(670,570,360,60))
    current = pyautogui.screenshot(region=(670,270,360,60))
    diff = ImageChops.difference(reference, current)
    return diff
semiClock = 0

print(round(sum(shot().getpixel((30,46))) / 3))
while running:
    color1 = round(sum(shot().getpixel((30,46))) / 3)
    color2 = round(sum(shot().getpixel((30,16))) / 3)
    color1Bool = color1 > 20
    color2Bool = color2 > 20
    if color1Bool or color2Bool:
        pyautogui.press("space")
        semiClock += 1
    if semiClock == 50:
        detectionIndex = 8
