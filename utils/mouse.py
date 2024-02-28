from time import sleep
from settings import MOUSE_MOVE_DURACTION
import pyautogui

def safety_click_xy(x, y):
    pyautogui.moveTo(
        x, y,
        duration=MOUSE_MOVE_DURACTION
    )
    sleep(0.5)
    pyautogui.click()

def safety_click(position):
    pyautogui.moveTo(
        position.x, position.y,
        duration=MOUSE_MOVE_DURACTION
    )
    sleep(0.5)
    pyautogui.click()

def safety_drag(position_1, position_2):
    pyautogui.moveTo(
        position_1.x, position_1.y,
        duration=MOUSE_MOVE_DURACTION
    )
    sleep(0.5)
    pyautogui.dragTo(
        position_2.x, position_2.y,
        button='left', duration=MOUSE_MOVE_DURACTION
    )
    sleep(0.2)