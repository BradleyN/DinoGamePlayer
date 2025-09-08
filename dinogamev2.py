from pyautogui import screenshot, press 
from time import sleep
from PIL import ImageStat
sleep(5)
running = True

def scan():
    img = screenshot(region=(670,280,130,120)) #takes a screenshot of an area in front of the dino
     #converts image to binary for more direct processing (although it could do without it)
    stat = ImageStat.Stat(img) #gets stats of the image
    avg_brightness = stat.mean[0] #finds the average brightness
    return round(avg_brightness) #returns it

img = screenshot(region=(670,280,130,120))
img.show()