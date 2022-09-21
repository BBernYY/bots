import pyautogui as pag
import keyboard as kb
import random
from time import sleep
def main():
    if kb.is_pressed('esc'):
        
        return 'ended'
    a = int((random.random())*1000000)
    types = [' graden Celsius', ' Kelvin']
    changes = {' graden Celsius': 273, ' Kelvin': -273}
    startmetric = random.choice(types)
    endmetric = types[types.index(startmetric)-1]
    b = a-changes[endmetric]

    return f'Wist je dat {str(a)+startmetric} {str(b)+endmetric} is?\n'
while True:
    loop = False
    while not loop:
        if kb.is_pressed('shift'):
            sleep(0.1)
            loop = True
    text = ""
    while loop:
        out = main()
        if out != 'ended':
            text += out
        else:
            loop = False
    open('text.txt', 'w').write(text)