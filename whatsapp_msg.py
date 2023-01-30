from itertools import count
import pyautogui
import time
time.sleep(4)
count = 0
while count<=50:
    pyautogui.typewrite('Hey')
    pyautogui.press('Enter')
    count+=1