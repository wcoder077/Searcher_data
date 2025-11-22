import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
import wikipedia


API_TOKEN = "7705190775:AAHs74S-ROBiFXRzPMxkZW2x3FFVrFy4lc4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
wikipedia.set_lang("uz")


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    await message.reply("Xush kelibsiz bizning botimizga!")


@dp.message(F.text)
async def sendSearcher(message: Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == "__main__":
    import asyncio

    asyncio.run(dp.start_polling(bot))
