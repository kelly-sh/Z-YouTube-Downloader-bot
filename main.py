from aiogram import *
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from pytubefix import YouTube
import os
import logging
import asyncio
import sys

TOKEN = "7299969557:AAF-fRqh_EtwLM6Gcc_sfuVJX5G4U51dT8Y"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет!\n"
                         "Я - бот, который скачивает видео с ютуба.\n"
                         "Просто скинь мне ссылку на видео, и я попробую его скачать :)")

#@dp.message(Command="Donation")
#async def donation(message: Message) -> None:
#   await message.answer("Хочешь поддержать проект?\n"
#"Вот мой Patreon")

@dp.message()
async def main_def(message: Message) -> None:
    chat_id = message.chat.id
    if message.text.startswith('https://youtu.be' or 'https://www.youtube.com/watch?'):
        url = str(message.text)
        yt = YouTube(url)
        await message.answer(f"<b>Начинаю загрузку видео</b>: <u>{yt.title}</u> <b>с канала</b>: <u>{yt.author}</u>")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="TEMP", filename=f"video_{chat_id}.mp4")
        await message.answer_video(types.FSInputFile(path=f"TEMP/video_{chat_id}.mp4"), caption="А вот и оно!")
        os.remove(f"TEMP/video_{chat_id}.mp4")
    else:
        await message.answer("Что-то пошло не так :(\n"
                             "Попробуй ещё раз")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())