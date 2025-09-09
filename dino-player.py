import pyautogui
import mss
import numpy as np
import time
import cv2

def detect_edge(x, y):
    with mss.mss() as sct:
        # define region originiating from (x,y) to check for edges
        monitor = {"top": y, "left": x, "width": 20, "height": 10}
        #take a screenshot of the region
        screenshot = sct.grab(monitor)

        img = np.array(screenshot)
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect edges
        edges = cv2.Canny(blurred, 50, 150)

        # Optional code, allows you to see what edges were/weren't detected in the screenshot 
        #cv2.imshow('Edges', edges)
        #cv2.waitKey(1)

        #for the screenshot edges, it is 0 for pixels that are not edges, non zero for pixels that are
        return cv2.countNonZero(edges) > 0

if __name__ == "__main__":
    #define edges of the play area. Depending on your setup you may have to alter these
    left_edge = 600
    bottom_edge = 340

    #offsets allow us to use coordinates relative to the play space
    #adjust these as you please to try and get better results
    left_offset = left_edge + 140
    bottom_offset = bottom_edge - 50

    #The code will automatically press space for you to start the game
    time.sleep(3)
    pyautogui.press('space')

    begin = time.perf_counter()

    while True:
        time_running = time.perf_counter() - begin
        #current system for making dino jump earlier as time increases. 
        #needs to be improved
        adj_left_offset = left_offset + int(1.75 * time_running)

        cactus_check = detect_edge(adj_left_offset, bottom_offset)
        bird_check = detect_edge(adj_left_offset + 30, bottom_offset - 40)

        if cactus_check:
            pyautogui.press('space')
        elif bird_check:
            with pyautogui.hold('down'):
                time.sleep(0.5)