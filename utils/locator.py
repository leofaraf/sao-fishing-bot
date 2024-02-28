from time import sleep
from settings import MAX_LOCATING_DURACTION
from utils import telegram_client
import pyautogui
import logging

def locate_images(except_message, *images):
    times = 0
    e = None
    while times != MAX_LOCATING_DURACTION:
        for image in images:
            try:
                return pyautogui.locateCenterOnScreen(image[0], confidence=image[1])
            except Exception as err:
                e = err

        sleep(1)
        times += 1
    
    try:
        logging.info("BAD LOCATING. trying to get but not stable")
        return pyautogui.locateCenterOnScreen(images[-1][0], confidence=.4)
    except:
        logging.error(e)
        telegram_client.send_message(except_message)
        raise e

        

def locate_image(path, confidence, except_message):
    times = 0
    e = None
    while times != MAX_LOCATING_DURACTION:
        try:
            return pyautogui.locateCenterOnScreen(path, confidence=confidence)
        except Exception as err:
            e = err
            sleep(1)
            times += 1

    logging.error(e)
    telegram_client.send_message(except_message)
    raise e
