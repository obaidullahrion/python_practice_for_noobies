from pynput.keyboard import Key, Controller
import time 

keyboard = Controller()
#def split(words):
#    return[char for char in words]


time.sleep(3)
while True:
    keyboard.type("hi")
    keyboard.press(Key.enter)
    time.sleep(2)



