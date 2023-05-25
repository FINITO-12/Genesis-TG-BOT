from aiogram import Dispatcher
from aiogram.types import *
from keyboards.inline import kb_ChooseLang, kb_MainMenu


async def start(message: Message):
    await message.answer("Choose your language: ", reply_markup=kb_ChooseLang)
async def stage_two_start(message: Message):
    await message.answer("Choose your operation: ", reply_markup=kb_MainMenu)

async def query(call: CallbackQuery):
    if call.data == "ENG":
        await call.message.delete()
        await stage_two_start(message=call.message)

def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(query)
