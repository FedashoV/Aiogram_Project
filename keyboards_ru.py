from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)


main_menu_buttons = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🖨️ Распечатать 🖨️'),
                                                   KeyboardButton(text='⚡️ Основные вопросы 💢')],
                                                  [KeyboardButton(text='💲 Цены 💸'),
                                                   KeyboardButton(text='📝 Информация об организации 📚')]],
                                        resize_keyboard=True, input_field_placeholder='Выберите из списка:')

comeback = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🔙 Назад ↩️')]], resize_keyboard=True)

# buildings = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🏙️ Корпус 1 🏬'),
# KeyboardButton(text='🏙️ Корпус 2 🏦')]],
# resize_keyboard=True, input_field_placeholder='Выберите корпус:')

delete_delivery = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='❌ Отменить заказ')]],
                                      resize_keyboard=True)

yandex_disk = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text='📋 Расписание',
    url='https://disk.yandex.ru/d/WTGvYlu4Vvs1ow',
    callback_data='raspisanie')]])

payment1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='💸 Перейти к оплате')],
                                        [KeyboardButton(text='❌ Отменить заказ')]],
                               resize_keyboard=True, input_field_placeholder='Выберите действие:')

payment2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='💸 Перейти к oплате')],
                                        [KeyboardButton(text='❌ Отменить заказ')]],
                               resize_keyboard=True, input_field_placeholder='Выберите действие:')

keyboard_for_comment = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='❌ Отменить заказ')],
                                                     [KeyboardButton(text='⏭️ Пропустить')]],
                                           resize_keyboard=True, input_field_placeholder='Комментарий')

success_payment = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📕 В главное меню ⭐')]],
                                      resize_keyboard=True)
