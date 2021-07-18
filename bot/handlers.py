from bot.states import States
import hashlib

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle
import loguru

from bot.queries import create_user, get_all_articles, get_article, get_blog
from bot.models import User
from bot.buttons import back_btn, main_btn, article_menu


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
    elif message.text == "🔍 Поиск":
        await States.search.set()
        await message.answer("🔎 Просто отправьте боту любой текст.", reply_markup=back_btn())
    elif message.text == "👤 Подписки":
        await States.follows.set()
        await message.answer("🔎 Просто отправьте боту любой текст.", reply_markup=back_btn())


async def article_handler(query: types.CallbackQuery):
    try:
        article = get_article(query.data)
        text = f"<b>{article.title}</b>\n\n{article.text}"
        await query.message.edit_text(text, parse_mode="html")
    except Exception as e:
        loguru.logger.error(e)


async def search_function(message: types.Message, state: FSMContext):
    articles = get_all_articles()
    text = "<b>Результаты по вашему запросу:</b>\n\n"
    if message.text == "⬅️ Назад":
        await state.finish()
        await message.answer("Hi!", reply_markup=main_btn("Мой блог"))
        return
    for article in articles:
        if message.text.lower() in article.title.lower():
            text += f"{article.title}\n"

    await message.answer(text, parse_mode="html")


async def inline_get_article(inline_query: InlineQuery):
    articles = get_all_articles()
    item = []
    for article in articles:
        if inline_query.query.lower() in article.title.lower():
            text = f"{article.title}\n\n{article.text}"
            input_content = InputTextMessageContent(text)
            result_id: str = hashlib.md5(article.title.encode()).hexdigest()
            item.append(InlineQueryResultArticle(
                id=result_id,
                title=f'Result {article.title!r}',
                description=article.text,
                input_message_content=input_content,
            ))

    await inline_query.answer(results=item, cache_time=300)
