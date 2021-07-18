import pathlib
from bot.states import States
import os

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import PickleStorage

from bot.logger import logger_init
from .handlers import article_handler, inline_get_article, search_function, start_handler, text_handler

# Load dotenv
dotenv.load_dotenv()

# Configure logging.
# 4-levels for logging: INFO, DEBUG, WARNING, ERROR
logger_init("INFO")


async def main():
    """Main function"""

    # Initialize bot and dispatcher
    bot = Bot(token=os.getenv("API_TOKEN"))
    try:
        storage = PickleStorage(pathlib.Path("db"))
        dp = Dispatcher(bot, storage=storage)
        # start_handler register
        dp.register_message_handler(
            start_handler, commands={"start"}, state="*")
        # text_handler register
        dp.register_message_handler(
            text_handler, content_types="text")
        # register search_function
        dp.register_message_handler(
            search_function, state=States.search)
        # inline buttons handler
        dp.register_callback_query_handler(article_handler)
        # inline mode handler
        dp.register_inline_handler(inline_get_article)
        await dp.start_polling()
    finally:
        await bot.close()
