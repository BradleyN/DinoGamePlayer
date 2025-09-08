import pyautogui
import mss
import numpy as np
import keyboard
import time
       
def get_pixel_color(x, y):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = np.array(sct.grab(monitor))
        r, g, b = (int(c) for c in img[0, 0][:3])
        return (r, g, b)        

if __name__ == "__main__":
    #Step 1: Calibration
    print("Calibration: Enter the game and press esc to create a blue border around the play area.\n")

    #Start the game manually and press esc. Then, use the blue border to
    left_edge = 919
    #print("place your mouse over any part of the top edge of the blue border and press \'t\'")
    top_edge = 158
    #print("place your mouse over any part of the right edge of the blue border and press \'t\'")
    right_edge = 1643
    #print("place your mouse over any part of the bottom edge of the blue border and press \'t\'")
    bottom_edge = 340

    width = right_edge - left_edge
    height = bottom_edge - top_edge

    #how far from the left edge should it begin checking for obstacles?
    left_offset = left_edge + 145
    #how many pixels should it check forwards from the left edge of the band?
    band_width = 30
    #what height should the band be at with respect to the bottom of the canvas (down = positive, up = negative)?
    bottom_offset = bottom_edge - 40
    #birds are higher

    time.sleep(3)
    pyautogui.press('space')
    begin = time.perf_counter()

    while(True):
        time_running = time.perf_counter() - begin
        adj_left_offset = left_offset + int(1.75 * time_running)

        cactus_check = get_pixel_color(adj_left_offset,bottom_offset) != (36,33,32)
        bird_check = get_pixel_color(adj_left_offset + 30,bottom_offset - 40) != (36,33,32)

        if cactus_check:
            pyautogui.press('space')
        elif bird_check:
            print(bird_check)
            with pyautogui.hold('down'):
                time.sleep(0.5)