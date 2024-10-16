from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
from aiogram.filters import CommandStart, Command
from aiogram import Bot, F, types
import sys
import logging
import asyncio
import random
from server import keep_alive

token = "7332915111:AAE6-IynzV_d9JOxei6Q_W7Bm89KOptAIa8"
dp = Dispatcher()


def get_keys():
    button = [[types.InlineKeyboardButton(text="Хочу анек", callback_data="anek")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def get_anek():
    with open("res.txt","r",encoding="utf_8") as text:
        lst = text.readlines()
        text.close()
    return lst
print(len(get_anek()))


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer("Нажми на кнопку для анека", reply_markup=get_keys())


@dp.callback_query(F.data.startswith("anek"))
async def answer_anek(callback:types.CallbackQuery):
    await callback.message.edit_text(text=get_anek()[random.randint(0,len(get_anek()))],reply_markup=get_keys())


async def main():
    bot = Bot(token)
    await dp.start_polling(bot)

keep_alive()
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
