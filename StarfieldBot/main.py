import pyautogui
import time
from SFFunctions import fire_weapon, holster_weapon, open_scanner,reload

print("Starting Starfield bot in 5 seconds. Switch to game window!")
time.sleep(5)
#pyautogui.PAUSE = 0.1

fire_weapon()
holster_weapon(1)
open_scanner(2)
reload(3)
