import pyautogui
import keyboard
import random
from time import sleep
odds = {
    'a': 0.75,
    's': 0.5,
    'd': 0.25,
    'w': 0
}
switch = True
key = 'w'
sleep(2)
while switch:
    rng = random.random()
    pyautogui.keyUp(key)
    for k, v in odds.items():
        if rng > v:
            key = k
            pyautogui.press(k)
            break
        if keyboard.is_pressed(']'):
            switch = False