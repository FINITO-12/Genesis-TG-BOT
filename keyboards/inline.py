from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.text import faqs, order, adm_message, faqs_button_text, go_Back


def kb_Menu(indexLang):
    kb_MM = InlineKeyboardMarkup()
    button_A = InlineKeyboardButton(text=faqs_button_text[indexLang], callback_data="faq")
    button_B = InlineKeyboardButton(text=order[indexLang], callback_data="order")
    button_C = InlineKeyboardButton(text=adm_message[indexLang], callback_data="sendmessage")
    kb_MM.add(button_A).add(button_B).add(button_C)
    return kb_MM

def kb_Back(indexLang):
    kb_GoBack = InlineKeyboardMarkup()
    button_GoBack = InlineKeyboardButton(text=go_Back[indexLang], callback_data="back")
    kb_GoBack.add(button_GoBack)
    return kb_GoBack


# TODO: BUTTONS START


'''button_FAQ = InlineKeyboardButton(text="FAQ", callback_data="faq")
button_Order = InlineKeyboardButton(text="Order a VPS", callback_data="order")
button_ReportToAdmin = InlineKeyboardButton(text="Send message to admin", callback_data="sendmessage")
'''
###

button_Russian = InlineKeyboardButton(text="Русский", callback_data="RU")
button_English = InlineKeyboardButton(text="English", callback_data="ENG")
button_Azerbaijani = InlineKeyboardButton(text="Azərbaycan dili", callback_data="AZE")

#

#button_GoBack = InlineKeyboardButton(text="Go Back", callback_data="back")

# TODO: BUTTONS END

# TODO: KEYBOARDS START

#kb_GoBack = InlineKeyboardMarkup().add(button_GoBack)

kb_ChooseLang = InlineKeyboardMarkup().add(button_Azerbaijani).add(button_Russian).add(button_English)

'''kb_MainMenu = InlineKeyboardMarkup().add(button_FAQ).add(button_Order).add(button_ReportToAdmin)
'''
# TODO: KEYBOARDS END
