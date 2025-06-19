import pyautogui
import time

def wait_then(action, *args, delay=5, **kwargs):
    print(f"Waiting {delay} seconds before executing {action.__name__}...")
    time.sleep(delay)
    return action(*args, **kwargs)

pyautogui.PAUSE = 0.1

# === Movement ===
def move_forward(duration=1):
    wait_then(_move_forward, duration)

def _move_forward(duration):
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')

def move_backward(duration=1):
    wait_then(_move_backward, duration)

def _move_backward(duration):
    pyautogui.keyDown('s')
    time.sleep(duration)
    pyautogui.keyUp('s')

def move_left(duration=1):
    wait_then(_move_left, duration)

def _move_left(duration):
    pyautogui.keyDown('a')
    time.sleep(duration)
    pyautogui.keyUp('a')

def move_right(duration=1):
    wait_then(_move_right, duration)

def _move_right(duration):
    pyautogui.keyDown('d')
    time.sleep(duration)
    pyautogui.keyUp('d')

def sprint(duration=1):
    wait_then(_sprint, duration)

def _sprint(duration):
    pyautogui.keyDown('shift')
    _move_forward(duration)
    pyautogui.keyUp('shift')

def jump():
    wait_then(pyautogui.press, 'space')

def crouch():
    wait_then(pyautogui.press, 'ctrl')

# === Combat ===
def fire_weapon():
    wait_then(_fire_weapon)

def _fire_weapon():
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

def aim_down_sights(duration=1):
    wait_then(_aim_down_sights, duration)

def _aim_down_sights(duration):
    pyautogui.mouseDown(button='right')
    time.sleep(duration)
    pyautogui.mouseUp(button='right')

def reload():
    wait_then(pyautogui.press, 'r')

def throw_grenade():
    wait_then(pyautogui.press, 'g')

def melee():
    wait_then(pyautogui.press, 'v')

def switch_weapon_scroll(up=True):
    wait_then(pyautogui.scroll, 1 if up else -1)

def switch_weapon_slot(slot=1):
    wait_then(pyautogui.press, str(slot))

# === Interaction ===
def interact():
    wait_then(pyautogui.press, 'e')

def holster_weapon():
    wait_then(pyautogui.press, 'h')

def open_scanner():
    wait_then(pyautogui.press, 'f')

def toggle_flashlight():
    wait_then(pyautogui.press, 'l')

# === Menus ===
def open_inventory():
    wait_then(pyautogui.press, 'i')

def open_map():
    wait_then(pyautogui.press, 'm')

def open_missions():
    wait_then(pyautogui.press, 'l')

def open_character_menu():
    wait_then(pyautogui.press, 'tab')

def open_ship_menu():
    wait_then(pyautogui.press, 'b')

def pause_menu():
    wait_then(pyautogui.press, 'esc')

def quick_save():
    wait_then(pyautogui.press, 'f5')

def quick_load():
    wait_then(pyautogui.press, 'f9')

def scan_ping():
    open_scanner()
    time.sleep(0.5)
    pyautogui.click()
