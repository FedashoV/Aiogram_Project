from aiogram import Bot, Router, F
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from config import PAY_TEST

import conditions_ru as cd
import keyboards_ru as kb

payment_router = Router()


@payment_router.message(F.text == '💸 Перейти к oплате')
async def payment(message: Message, bot: Bot):
    rub = cd.pay
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Выпуск печатной продукции на заказ',
        description='Оплата заказа (нажмите кнопку ниже)!',
        payload='payment through the bot',
        provider_token=PAY_TEST,
        # provider_token=PAY_LIVE,
        currency='rub',
        prices=[
            LabeledPrice(
                label="Печать",
                amount=rub * 100)
        ],
        start_parameter='printer6_bot',
        provider_data=None,
        need_name=False,
        need_email=True,
        need_phone_number=False,
        need_shipping_address=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        reply_markup=None,
        max_tip_amount=200000,
        suggested_tip_amounts=[500, 1000, 2000, 5000],
        request_timeout=60,
    )


async def pre_check_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def g_successful_payment(message: Message, bot: Bot):
    await message.answer(f'✅ Вы успешно оплатили заказ на сумму '
                         f'{message.successful_payment.total_amount // 100} рублей!'
                         f'\n\n'
                         f'🕓 Ожидайте доставку в указанное вами время.',
                         reply_markup=kb.success_payment)
    await bot.send_message(-1002193083153, "Успешная оплата!")
    await bot.send_message(-1002193083153, "=================================")


