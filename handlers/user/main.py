from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from dataBase.main import DB
from handlers.text import faqs, choose_ur_operation, go_Back, sendMessage, message_sent, indexLanguage
from keyboards.inline import kb_ChooseLang, kb_Menu, kb_Back
from misc import TgKeys

base = DB("localhost", "root", "", "Genesis_bot")
attempts = 1

bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')


async def adminhandler(message: Message, call: CallbackQuery, state: FSMContext):
    if call.data == "sentmessage":
        user_id = message.chat.id


async def send_mes(message: Message, state: FSMContext):
    global attempts, indexLanguage

    admin_id = [761223254]

    text = "' " + str(message.text)+ " '" + " | " + str(message_sent[indexLanguage]) + str(message.chat.first_name)
    while attempts < 1:
        for x in range(len(admin_id)):
            shit = base.result_fetch(False, f"SELECT user_id FROM users WHERE user_id='%s'" % admin_id[x])
            await bot.send_message(admin_id[x], text)
            attempts = attempts + 1

    #shit = base.result_fetch(False, f"SELECT user_id FROM users WHERE user_id='%s'" % admin_id)
    # print(shit)
    # print(shit[0][0])



    # await bot.send_message(shit[0][0])


async def start(message: Message):
    base.insert_users(True, message)
    await message.answer(text="Dilinizi seçin | Выберите язык | Choose language:", reply_markup=kb_ChooseLang)


async def stage_two_start(message: Message):
    await message.answer(text=str(choose_ur_operation[indexLanguage]), reply_markup=kb_Menu(indexLanguage))

async def send(message: Message):
    await message.answer(text=str(sendMessage[indexLanguage]), reply_markup=kb_Back(indexLanguage))

async def faq(message: Message):
    await message.answer(text=str(faqs[indexLanguage]), reply_markup=kb_Back(indexLanguage))


async def query(call: CallbackQuery):
    global indexLanguage, attempts
    if call.data == "ENG":
        indexLanguage = 0
        attempts = 0
        await call.message.delete()
        await stage_two_start(message=call.message)
    if call.data == "RU":
        indexLanguage = 1
        attempts = 0
        await call.message.delete()
        await stage_two_start(call.message)
    if call.data == "AZE":
        indexLanguage = 2
        attempts = 0
        await call.message.delete()
        await stage_two_start(call.message)
    if call.data == "faq":
        attempts = 0
        await call.message.delete()
        await faq(message=call.message)
    if call.data == "back":
        attempts = 0
        await call.message.delete()
        await stage_two_start(message=call.message)
    if call.data == "sendmessage":
        attempts = 0
        await call.message.delete()
        await send(call.message)
        # await


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(query)
    dp.register_message_handler(send_mes, content_types=['text'])
