import asyncio
import logging
import random
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Удалите импорт keep_alive отсюда
# from notmain import keep_alive

token = "7332915111:AAE6-IynzV_d9JOxei6Q_W7Bm89KOptAIa8"
dp = Dispatcher()

def get_keys():
    button = [[InlineKeyboardButton(text="Хочу анек", callback_data="anek")]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard

def get_anek():
    with open("res.txt", "r", encoding="utf_8") as text:
        return text.readlines()

@dp.message(CommandStart)
async def start(message: types.Message):
    await message.answer("Нажми на кнопку для анека", reply_markup=get_keys())

@dp.callback_query(F.data.startswith("anek"))
async def answer_anek(callback: types.CallbackQuery):
    await callback.message.edit_text(text=random.choice(get_anek()), reply_markup=get_keys())

async def main():
    from notmain import keep_alive  # Переместите импорт сюда
    keep_alive()
    bot = Bot(token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

