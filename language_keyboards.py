from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


languages = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🇷🇺 РУССКИЙ 🇷🇺')],
                                          [KeyboardButton(text='🇺🇸 В РАЗРАБОТКЕ 🇺🇸')]],
                                resize_keyboard=True,
                                input_field_placeholder='Выберите язык')

