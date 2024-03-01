from time import sleep
from settings import MAX_LOCATING_DURACTION
from utils import telegram_client
import pyautogui
import logging
from timeit import default_timer

def locate_fbtn():
    times = 0
    e = None
    while times != MAX_LOCATING_DURACTION:
        try:
            return pyautogui.locateCenterOnScreen("assets/f.png", confidence=.8)
        except Exception as err:
            e = err
            sleep(1)
            times += 1

    logging.error(e)
    telegram_client.send_message("Can't locate F button")
    raise e

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

        

def locate_image(path, confidence, except_message, sleep_time = 1):
    start = default_timer()

    times = 0
    e = None
    while times != MAX_LOCATING_DURACTION:
        try:
            pos = pyautogui.locateCenterOnScreen(path, confidence=confidence)
            logging.info(f"Locating time of \"{path}\" is: {default_timer() - start}")
            return pos
        except Exception as err:
            e = err
            sleep(sleep_time)
            times += 1

    logging.error(e)
    telegram_client.send_message(except_message)
    raise e

def fast_zone():
    start = default_timer()

    times = 0
    e = None
    while (default_timer() - start) < MAX_LOCATING_DURACTION:
        try:
            pos = pyautogui.locateCenterOnScreen("assets/zone.png", confidence=.7, region=[
                1016, 320,
                100, 600
            ])
            logging.info(f"Locating time of \"zone\" is: {default_timer() - start}")
            return pos
        except Exception as err:
            pass

    logging.error(e)
    telegram_client.send_message("Can't locate zone")
    raise e

def fast_locate(path, confidence, except_message):
    start = default_timer()

    times = 0
    e = None
    while (default_timer() - start) < MAX_LOCATING_DURACTION:
        try:
            pos = pyautogui.locateCenterOnScreen(path, confidence=confidence)
            logging.info(f"Locating time of \"{path}\" is: {default_timer() - start}")
            return pos
        except Exception as err:
            pass

    logging.error(e)
    telegram_client.send_message(except_message)
    raise e