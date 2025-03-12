from aiogram import Dispatcher, Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from backend.keyboards.keyboard import start_keyboard, start_inline_keyboard

bot = Bot('7811012298:AAHx9VYtYMqdGj84AKWXHXY3-T4sSuFwFK8')
dp = Dispatcher(bot, storage=MemoryStorage())

storage = MemoryStorage()
CHANNEL_LINK = "https://t.me/Tonsale_uzbek"

async def on_startup(_):
    print("Bo't ishga tushdi.")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, '👋 Assalomu alaykum  botimizga xush kelibsiz.✍🏻 Kino kodini yuboring...',
                           reply_markup=start_keyboard())




@dp.message_handler(commands=['start'])
async def start(message: Message):
    user_mention = f"[{message.from_user.full_name}](tg://user?id={message.from_user.id})"
    await message.answer(f"👋 Assalomu alaykum {user_mention} botimizga xush kelibsiz.✍🏻 Kino kodini yuboring... {user_mention}!", parse_mode="MarkdownV2")


@dp.message_handler(Text(equals="Admin bilan boglnish"))
async def start_ask_word(message: types.Message):
    print(message)
    await bot.send_message(message.chat.id, 'Qaysi biri maqul', reply_markup=start_inline_keyboard())


# @dp.callback_query_handler(text='1')
# async def answer_word(callback: types.CallbackQuery):
#     await callback.message.answer(f"@tonsale_uzbek")


# @dp.message_handler(Text(equals="2"))
# async def start_ask_word(message: types.Message):
#     await bot.send_message(message.chat.id, '1', reply_markup=start_inline_keyboard())


@dp.callback_query_handler(text='2')
async def answer_word(callback: types.CallbackQuery):
    await callback.message.answer(f"Habarni yozib qoldiring <3")




@dp.message_handler(text='salom')
async def text(message: types.Message):
    await bot.send_message(message.chat.id, 'qalesan bodiringbosh')


@dp.message_handler()
async def text(message: types.Message):
    await bot.send_message(message.chat.id, 'So\'rov qabul qilindi')


executor.start_polling(dp, on_startup=on_startup)
