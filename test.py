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
        
        # TODO: Attack while fish isn't killed
        while True:
            pydirectinput.press('f')
            sleep(.1)

            logging.info("Pressing F")
            try:
                exit_btn = locator.locate_image("assets/x.png", .7, "Can't locate exit after killing a fish")
                mouse.safety_click(exit_btn)
                logging.info("Fish menu has found")
                break
            except:
                logging.info("We aren't in menu. Trying again")
                continue
            
    except Exception as e:
        logging.error(f"Error: {e}")
        telegram_client.send_message(f"Error, please check logs")

if __name__ == "__main__":
    logger.configure_logger(True)
    main()