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


async def video_download(url, chat_id, message):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(f'TEMP_{chat_id}', f"{chat_id}_{yt.title}.mp4")
    with open(f"TEMP_{chat_id}/{chat_id}_{yt.title}.mp4", 'r') as video:
        await message.answer
        os.remove(f"TEMP_{chat_id}/{chat_id}_{yt.title}.mp4")



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! Send me the link of YouTube video You want to download and I'll try to download It!")



@dp.message()
async def main_def(message: Message) -> None:
    chat_id = message.chat.id
    url = str(message.text)
    yt = YouTube(url)
    if message.text.startswith('https://youtu.be' or 'https://www.youtube.com/watch?'):
        await message.answer(f"Initializing downloading video: {yt.title} from {yt.author}")
        stream = yt.streams.get_highest_resolution()
        stream.download(f'TEMP_{chat_id}', f"{chat_id}_{yt.title}.mp4")
        await message.answer_video(types.FSInputFile(path=f"TEMP_{chat_id}/{chat_id}_{yt.title}.mp4"), caption="Here It is!")
        os.remove(f"TEMP_{chat_id}/{chat_id}_{yt.title}.mp4")
    else:
        await message.answer("Invlaid link :(")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())