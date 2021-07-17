from aiogram import types
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup

from .models import Article


def main_btn(custom: str) -> ReplyKeyboardMarkup:
    """Main button"""
    buttons = ["⭐️ Рекомендации",
               "👤 Подписки",
               "🔍 Поиск"]

    # If custom is exists add to buttons list
    if custom:
        buttons.append(custom)

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menu.add(*buttons)
    return menu


def article_menu(articles: list[Article]) -> types.InlineKeyboardMarkup:
    """Article menu"""
    menu = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for article in articles:
        buttons.append(types.InlineKeyboardButton(
            article.title, callback_data=article.id))
    menu.add(*buttons)

    return menu
