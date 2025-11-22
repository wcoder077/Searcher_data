from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import wikipedia
import asyncio

API_TOKEN = "7705190775:AAHs74S-ROBiFXRzPMxkZW2x3FFVrFy4lc4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
wikipedia.set_lang("uz")


@dp.message(Command(commands=["start", "help"]))
async def welcome(message: types.Message):
    await message.reply(
        "Qidiruv botimizga 'Xush kelibsiz'\n"
        "Hohlagan mavzuyingizdagi malumotni yozing. "
        "Maslahat: 1 yoki 2 ta so'z bo'lsa yaxshi natija beradi."
    )


@dp.message()
async def search_wikipedia(message: types.Message):
    try:
        await message.answer(wikipedia.summary(message.text))
    except:
        await message.answer("Maqola topilmadi.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
