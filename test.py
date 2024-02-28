from time import sleep
from utils import logger, telegram_client, locator, mouse
import pyautogui, pydirectinput
import logging

def main():
    sleep(5)

    fbtn = locator.locate_fbtn()
    logging.info(f"button position: {fbtn}")

    try:
        # TODO: Press F while it isn't in fishing menu
        while True:
            pydirectinput.press('f')
            sleep(.1)

            logging.info("Pressing F")
            try:
                pyautogui.locateCenterOnScreen("assets/kill_bar.png", confidence=.8)
                telegram_client.send_message("finded")
                logging.info("Fish menu has found")
                break
            except:
                logging.info("We aren't in menu. Trying again")
                continue
        
        zone = locator.locate_image("assets/zone.png", .8, "Can't locate \"green\" zone")

        # TODO: Attack while fish isn't killed
        while True:
            while True:
                cur = locator.locate_image("assets/cur.png", .7, "Can't locate current position of fishing", 0)
                defer = zone.y - cur.y 
                if -150 <= defer <= 150:
                    break
                else:
                    logging.info(f"Deference between current and target zone is: {defer}px")
            pydirectinput.press('f')
            logging.info("Pressing F")

            sleep(1)
            try:
                zone = locator.locate_image("assets/zone.png", .8, "Can't locate \"green\" zone")
                logging.info("We aren't killed fish. Trying again")
            except:
                try:
                    exit_btn = locator.locate_image("assets/x.png", .8, "Can't locate X", .5)
                    mouse.safety_click(exit_btn)
                    logging.info("Fish menu has found")
                    break
                except: 
                    pass

    except Exception as e:
        logging.exception(e)
        telegram_client.send_message(f"Error, please check logs")

if __name__ == "__main__":
    logger.configure_logger(True)
    main()