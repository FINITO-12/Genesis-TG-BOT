from aiogram import Dispatcher
from aiogram.types import *

from dataBase.main import DB
from handlers.text import faqs, choose_ur_operation
from keyboards.inline import kb_ChooseLang, kb_Menu, kb_Back

base = DB("localhost", "root", "", "Genesis_bot")





async def start(message: Message):
    await message.answer(text="Dilinizi seçin | Выберите язык | Choose language:", reply_markup=kb_ChooseLang)


async def stage_two_start(message: Message):
    await message.answer(text=str(choose_ur_operation[indexLanguage]), reply_markup=kb_Menu(indexLanguage))


async def faq(message: Message):
    await message.answer(text=str(faqs[indexLanguage]), reply_markup=kb_Back(indexLanguage))


async def query(call: CallbackQuery):
    global indexLanguage
    if call.data == "ENG":
        indexLanguage = 0
        await call.message.delete()
        await stage_two_start(message=call.message)
    if call.data == "RU":
        indexLanguage = 1
        await call.message.delete()
        await stage_two_start(call.message)
    if call.data == "AZE":
        indexLanguage = 2
    if call.data == "faq":
        await call.message.delete()
        await faq(message=call.message)
    if call.data == "back":
        await call.message.delete()
        await stage_two_start(message=call.message)


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    dp.register_message_handler(start, commands=["start"])
    #dp.register_message_handler(shit, commands=['flex'])
    dp.register_callback_query_handler(query)
