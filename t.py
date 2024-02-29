from utils import logger, telegram_client

logger.configure_logger(True)
telegram_client.send_message("test")