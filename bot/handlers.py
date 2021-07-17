import logging
from aiogram import types

from bot.queries import create_user, get_article, get_blog
from bot.models import User
from bot.buttons import main_btn, article_menu


async def start_handler(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    input_json = {
        "user_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
    }
    user = User(**input_json)
    create_user(user)
    await message.answer("Hi!", reply_markup=main_btn("Мой блог"))


async def text_handler(message: types.Message):
    """Text message handler"""

    if message.text == "Мой блог":
        blog = get_blog(message.from_user.id)
        text = "Список ваших статей:\n\n"
        for i, article in enumerate(blog.articles, 1):
            text += f"{str(i)}: {article.title}\n"
        await message.answer(text, reply_markup=article_menu(blog.articles))


async def article_handler(query: types.CallbackQuery):
    try:
        article = get_article(query.data)
        text = f"<b>{article.title}</b>\n\n{article.text}"
        await query.message.edit_text(text, parse_mode="html")
    except Exception as e:
        logging.ERROR(e)
