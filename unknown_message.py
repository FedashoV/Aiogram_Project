from aiogram import Router
from aiogram.types import Message

UM_message = Router()


@UM_message.message()
async def unknown_message(message: Message):
    await message.answer('🤖 Я вас не понимаю. Пожалуйста выберите одну из кнопок ниже либо в случае их '
                         'отсутствия напишите /start')