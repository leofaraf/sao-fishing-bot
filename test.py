from time import sleep
from utils import logger, telegram_client, locator, mouse
import pyautogui, pydirectinput
import logging

def main():
    sleep(5)

    while True:
        try:
            # TODO: Press F while it isn't in fishing menu
            while True:
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
                try:
                    zone = locator.fast_locate("assets/zone.png", .7, "Can't locate \"green\" zone")
                    logging.info("We aren't killed fish. Trying again")
                except:
                    pydirectinput.press('backspace')
                    sleep(3)
                    break
                
                is_cur_available = True
                while True:
                    try:
                        cur = locator.fast_cur()
                        defer = zone.y - cur.y
                        logging.info(f"Zone is {zone}, current is {cur}")
                        if -50 <= defer <= 50:
                            pydirectinput.press('f')
                            logging.info("Pressing F")
                            break
                    except:
                        logging.exception("Can't locate current position")
                        is_cur_available == False
                if not is_cur_available:
                    break

                sleep(2)

        except Exception as e:
            logging.exception(e)
            telegram_client.send_message(f"Error, please check logs")

            pydirectinput.press('backspace')
            sleep(3)

if __name__ == "__main__":
    logger.configure_logger(True)
    try:
        main()
    except:
        telegram_client.send_message("CRASH. Bot is crashed. Please rerun it or check logs.")