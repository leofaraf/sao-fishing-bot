import requests
import logging
from settings import *

# Send telegram message to our bot with format like "[{BOT_NAME}] {text}"
def send_message(text):
    try:
        message = f"[{BOT_NAME}] {text}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_ADMIN_ID}&text={message}"
        logging.info(requests.get(url).json())
    except ConnectionError as e:
        logging.error(f"Telegram request error: {e}")