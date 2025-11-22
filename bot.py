import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiohttp import web
import wikipedia
import os

API_TOKEN = "7705190775:AAHs74S-ROBiFXRzPMxkZW2x3FFVrFy4lc4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
wikipedia.set_lang("uz")


@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    await message.reply(
        "Qidiruv botimizga 'Xush kelibsiz' \nHohlagan mavzuyingizdagi malumotni yozing. Maslahat (1 yoki 2 ta so'zdan iborat bo'lsa yaxshi malumot chiqarib beradi). Raxmat!"
    )


@dp.message(F.text)
async def sendSearcher(message: Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


async def handle(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.update_queue.put(update)
    return web.Response(text="ok")


app = web.Application()
app.router.add_post(f"/{API_TOKEN}", handle)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    web.run_app(app, host="0.0.0.0", port=port)
