import os

import dotenv
from aiogram import Bot, Dispatcher

from bot.logger import logger_init
from .handlers import article_handler, inline_get_article, start_handler, text_handler

# Load dotenv
dotenv.load_dotenv()

# Configure logging
logger_init("INFO")


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
        dp.register_inline_handler(inline_get_article)
        await dp.start_polling()
    finally:
        await bot.close()
