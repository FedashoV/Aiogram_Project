from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import language_keyboards as kb_main

main_router = Router()


@main_router.message(Command('start'))
async def choose_language(message: Message):
    await message.answer("🇷🇺 Добро пожаловать! Выбери язык 🇷🇺 \n\n"
                         "🇬🇧🇺🇲 Welcome! Choose a language! 🇺🇲🇬🇧",
                         reply_markup=kb_main.languages)
