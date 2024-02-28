from time import sleep
from utils import logger, telegram_client, locator, mouse
import pyautogui
import logging

def main():
    sleep(5)

    try:
        # TODO: Press F while it isn't in fishing menu
        while True:
            pyautogui.hotkey("F") # TODO: Press F
            logging.info("Pressing F")
            try:
                pyautogui.locateCenterOnScreen("assets/kill_bar.png", confidence=.8)
                telegram_client.send_message("finded")
                break
            except:
                logging.info("We aren't in menu. Trying again")
                continue
        
        sleep(0.25)
        
        exit() # TODO: Await active
        sleep(0.25)

        while True:
            exit() # TODO: Await while fish'll on attack
            pyautogui.hotkey("f") # TODO: Press F
            if True: # TODO: If fish is killed
                exit_btn = locator.locate_image("assets/x.png", .7, "Can't locate exit after killing a fish")
                mouse.safety_click(exit_btn)
    except Exception as e:
        logging.error(f"Error: {e}")
        telegram_client.send_message(f"Error, please check logs")

if __name__ == "__main__":
    logger.configure_logger(True)
    main()