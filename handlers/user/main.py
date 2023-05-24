from aiogram import Dispatcher
from aiogram.types import *


async def start(message: Message):
    await message.answer(text="Hello World")


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    dp.register_message_handler(start, commands=["start"])

