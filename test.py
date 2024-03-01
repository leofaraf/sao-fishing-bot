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
                    telegram_client.send_message("finded")
                    logging.info("Fish menu has found")
                    break
                except:
                    logging.info("We aren't in menu. Trying again")
                    continue
            
            # TODO: Attack while fish isn't killed
            while True:
                try:
                    zone = locator.fast_zone()
                    logging.info("We aren't killed fish. Trying again")
                except:
                    try:
                        exit_btn = locator.fast_locate("assets/x.png", .8, "Can't locate X")
                        mouse.safety_click(exit_btn)
                        logging.info("Fish menu has found")
                        break
                    except: 
                        logging.info("We aren't in menu, but we can't found X button")
                
                while True:
                    cur = locator.fast_locate("assets/cur.png", .7, "Can't locate current position of fishing")
                    defer = zone.y - cur.y
                    logging.info(f"Zone is {zone}, current is {cur}")
                    if -50 <= defer <= 50:
                        break
                        
                pydirectinput.press('f')
                logging.info("Pressing F")

                sleep(1)
                

        except Exception as e:
            logging.exception(e)
            telegram_client.send_message(f"Error, please check logs")

            pydirectinput.press('backspace')
            sleep(3)

if __name__ == "__main__":
    logger.configure_logger(True)
    main()