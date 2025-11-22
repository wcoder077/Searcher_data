import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
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
        "Qidiruv botimizga 'Xush kelibsiz'\n"
        "Hohlagan mavzuyingizdagi malumotni yozing. "
        "Maslahat: 1 yoki 2 ta so'z bo'lsa yaxshi natija beradi."
    )


@dp.message()
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


async def root(request):
    return web.Response(text="Bot ishlayapti!")


app = web.Application()
app.router.add_post(f"/{API_TOKEN}", handle)
app.router.add_get("/", root)


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    # Webhookni Telegramga o‘rnatish
    import asyncio

    async def on_startup():
        await bot.set_webhook(f"https://YOUR_RENDER_URL/{API_TOKEN}")

    web.run_app(app, host="0.0.0.0", port=PORT, startup=on_startup())
