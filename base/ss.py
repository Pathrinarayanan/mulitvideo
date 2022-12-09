from time import sleep
import pyautogui

while True:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("C:\\Users\\sys\\Downloads\\abc.png")
    sleep(1)
        