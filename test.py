from time import sleep
from utils import logger, telegram_client
import pyautogui
import logging

def main():
    try:
        # TODO: Press F
        pyautogui.hotkey("f") # TODO: Press F
        
        sleep(0.25)
        
        exit() # TODO: Await active
        sleep(0.25)

        while True:
            exit() # TODO: Await while fish'll on attack
            pyautogui.hotkey("f") # TODO: Press F
            if True: # TODO: If fish is killed
                break
    except Exception as e:
        logging.error(f"Error: {e}")
        telegram_client.send_message(f"Error, please check logs")

if __name__ == "__main__":
    logger.configure_logger(True)
    main()