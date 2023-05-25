from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.text import faqs
from handlers.user.main import indexLanguage

# TODO: BUTTONS START


button_FAQ = InlineKeyboardButton(text="FAQ", callback_data="faq")
button_Order = InlineKeyboardButton(text="Order a VPS", callback_data="order")
button_ReportToAdmin = InlineKeyboardButton(text="Send message to admin", callback_data="sendmessage")

###

button_Russian = InlineKeyboardButton(text="Русский", callback_data="RU")
button_English = InlineKeyboardButton(text="English", callback_data="ENG")
button_Azerbaijani = InlineKeyboardButton(text="Azərbaycan dili", callback_data="AZE")

#

button_GoBack = InlineKeyboardButton(text="Go Back", callback_data="back")

# TODO: BUTTONS END

# TODO: KEYBOARDS START

kb_GoBack = InlineKeyboardMarkup().add(button_GoBack)

kb_ChooseLang = InlineKeyboardMarkup().add(button_Azerbaijani).add(button_Russian).add(button_English)

kb_MainMenu = InlineKeyboardMarkup().add(button_FAQ).add(button_Order).add(button_ReportToAdmin)

# TODO: KEYBOARDS END
