import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# BotFather'dan olgan tokeningizni shu yerga yozasiz
TOKEN = "8364307525:AAE_83VGIYvpP4V3DPtCPnjLKWna2TFkQcg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i uchun javob
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom! Men bulutda ishlayotgan botman. Kompyuteringizni o'chirsangiz ham ishlayveraman! 🚀")

# Har qanday matnli xabarga javob
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())