from time import sleep
from timeit import default_timer
from settings import MAX_LOOP_DURACTION
from utils import logger, telegram_client, locator, mouse
import pyautogui, pydirectinput
import logging

class TooLongLoopException(Exception): pass

def main():
    sleep(5)

    while True:
        try:
            fishing()

        except TooLongLoopException:
            telegram_client.send_message(f"Too long fishing (more than {MAX_LOOP_DURACTION}s)")
            pydirectinput.press('backspace')
            sleep(3)

        except locator.CurLocatingException:
            logging.warning("Can't locate cur")
            pydirectinput.press('backspace')
            sleep(3)

        except Exception as e:
            logging.exception("Error")
            telegram_client.send_message(f"Error, please check logs")

            pydirectinput.press('backspace')
            sleep(3)

def fishing():
    # TODO: Press F while it isn't in fishing menu
    start = default_timer()
    while True:
        if (default_timer() - start) >= MAX_LOOP_DURACTION:
            raise TooLongLoopException()

        pydirectinput.press('f')
        sleep(.1)

        logging.info("Pressing F")
        try:
            pyautogui.locateCenterOnScreen("assets/kill_bar.png", confidence=.7)
            logging.info("Fish menu has found")
            break
        except:
            logging.info("We aren't in menu. Trying again")
            continue
    
    # TODO: Attack while fish isn't killed
    while True:
        if (default_timer() - start) >= MAX_LOOP_DURACTION:
            raise TooLongLoopException()
        
        try:
            zone = locator.fast_locate("assets/zone.png", .7, "Can't locate \"green\" zone")
            logging.info("We aren't killed fish. Trying again")
        except:
            pydirectinput.press('backspace')
            sleep(3)
            break
        
        while True:
            if (default_timer() - start) >= MAX_LOOP_DURACTION:
                raise TooLongLoopException()
        
            cur = locator.fast_cur()
            defer = zone.y - cur.y
            logging.info(f"Zone is {zone}, current is {cur}")
            if -50 <= defer <= 50:
                pydirectinput.press('f')
                logging.info("Pressing F")
                break

        sleep(2)

if __name__ == "__main__":
    logger.configure_logger(True)
    try:
        main()
    except:
        telegram_client.send_message("CRASH. Bot is crashed. Please rerun it or check logs.")