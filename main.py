import asyncio
from aiogram import Bot, Dispatcher, F
from handlers_ru import router
from conditions_ru import con_router
from handlers_language import main_router
from unknown_message import UM_message
from payment import payment, pre_check_query, g_successful_payment
from payment import payment_router
from config import TOKEN


async def main():  # обращение к серверу в телеграм.
    bot = Bot(token=TOKEN)
    dp = Dispatcher()  # обработчик сообщений от пользователя
    dp.include_router(main_router)
    dp.include_router(router)
    dp.include_router(payment_router)
    dp.include_router(con_router)
    dp.include_router(UM_message)
    dp.message.register(payment, F.text == '💸 Перейти к oплате')
    dp.pre_checkout_query.register(pre_check_query)
    dp.message.register(g_successful_payment, F.successful_payment)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен! Постарайтесь пожалуйста сделать тех. работы в срок чтобы не упустить клиентов!")

