from bot.buttons import article_menu
import os
import logging

import dotenv
from aiogram import Bot, Dispatcher

from .handlers import start_handler, text_handler, article_handler


# Load dotenv
dotenv.load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


async def main():
    """Main function"""

    # Initialize bot and dispatcher
    bot = Bot(token=os.getenv("API_TOKEN"))
    try:
        dp = Dispatcher(bot)
        # start_handler register
        dp.register_message_handler(
            start_handler, commands={"start"})
        # text_handler register
        dp.register_message_handler(
            text_handler, content_types="text")
        dp.register_callback_query_handler(article_handler)
        await dp.start_polling()
    finally:
        await bot.close()
