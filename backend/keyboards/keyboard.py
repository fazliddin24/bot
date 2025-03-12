from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
CHANNEL_LINK = "https://t.me/Tonsale_uzbek"

def start_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("Admin bilan boglnish")],
        # [KeyboardButton(""), KeyboardButton("3")],
    ], resize_keyboard=True)

    return kb


def start_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Admin userini olish', callback_data='1', url=CHANNEL_LINK)],
        [InlineKeyboardButton("Habar qolirish", callback_data='2')]
    ])

    return ikb
