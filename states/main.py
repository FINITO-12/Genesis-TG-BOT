from aiogram.dispatcher.filters.state import State, StatesGroup


class Dialog(StatesGroup):
    send_message = State()
    order = State()
