from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import TOKEN

import keyboards_ru as kb
import conditions_ru as cd

bot = Bot(token=TOKEN)
router = Router()


@router.message(F.text == '🇷🇺 РУССКИЙ 🇷🇺')
async def starting(message: Message):
    await message.answer('👋Привет!😄\n\n'
                         '❗Для более корректной работы бота🤖 не рекомендуется использовать браузерную'
                         ' версию Telegram❗\n\n'
                         'Здесь ты можешь распечатать любые документы в чёрно-белом формате🖨️ '
                         'к нужному времени! Если у тебя остались какие-либо вопросы, выбери соответствующие '
                         'кнопки ниже:', reply_markup=kb.main_menu_buttons)
    # await message.forward(-1002193083153, -1002193083153)
    # await SendMessage(chat_id=message.from_user.id, text=message.text)
    # await bot(SendMessage(chat_id=-1002193083153, text='+пользватель'))


@router.message(F.text == '🔙 Назад ↩️')
async def starting_not_new(message: Message):
    await message.answer('📑 Это главное меню! Выбери действие📙\n\n'
                         '', reply_markup=kb.main_menu_buttons)


@router.message(F.text == '📕 В главное меню ⭐')
async def starting_not_new2(message: Message):
    await message.answer('📑 Это главное меню! Выбери действие📙\n\n'
                         '', reply_markup=kb.main_menu_buttons)


@router.message(F.text == '💲 Цены 💸')
async def timetable(message: Message):
    await message.answer('💸💸 Цены на печать (за одну страницу) 💸💸\n\n'
                         '😤1-3 стр: <b>10₽</b>\n'
                         '😐4-6 стр:  <b>8₽</b>\n'
                         '🙂7-9 стр:  <b>7₽</b>\n'
                         '🥰10-29 стр: <b>6₽</b>\n'
                         '💖30+ стр:  <b>5₽</b>\n\n'
                         '❗Доставка до комнаты, первичный осмотр документа и поверхостное форматирование '
                         'по ГОСТу: <b>БЕСПЛАТНО</b>❗',
                         reply_markup=kb.comeback, parse_mode='HTML')


@router.message(F.text == '⚡️ Основные вопросы 💢')
async def questions(message: Message):
    await message.answer(f'<b>Есть ли возможность сделать ксерокс</b>❓\n\n — Нет, мы не владеем ксероксом. '
                         f'Можем '
                         f'предложить вам'
                         ' альтернативу. \n\nК примеру, если нужна копия паспорта, вы можете сделать фотографию со '
                         'своего телефона, после чего мы вам её распечатаем — принцип действия копировальной машины '
                         'тот же, что у фотоаппарата. Данная процедура выполнялась неоднократно на протяжении '
                         'предыдущего учебного года, поэтому нет повода для беспокойства😊\n\n\n'
                         f'<b>Если я принесу свою бумагу, будет ли дешевле</b>❓\n\n — Нет, мы '
                         f'используем исключительно '
                         'свой принтер и свою бумагу. Мы установили максимально низкую цену (с учётом '
                         'заправки картриджа, комиссий с платежей, '
                         'аренды серверов и пр. расходов). Итоговую стоимость старались '
                         'компенсировать бесплатной доставкой.\n\n\n'
                         f'<b>Скидки постоянным клиентам</b>❓\n\n — Безусловно мы ценим каждого нашего '
                         'клиента и несмотря на '
                         'ответ предыдущего вопроса, мы рассматриваем возможность введения промокодов/бонус-кодов. '
                         'Следите за новостями!\n\n\n'
                         f'<b>Можно ли за печатью обратиться в ЛС и/или оплачивать переводом/'
                         'наличными как в прошлом году</b>'
                         f'❓\n\n '
                         '— Пока '
                         'бот работает в тестовом режиме, у вас есть возможность оформить заказ лично у '
                         '@X_10_Pa3_3a_Ho4b_X .', reply_markup=kb.comeback,
                         parse_mode="HTML")


@router.message(F.text == '📝 Информация об организации 📚')
async def admin_info(message: Message):
    await message.answer(f'<b>ИНН:</b> 132436248527\n'
                         f'<b>ФИО:</b> Цыплаков Кирилл Александрович\n'
                         f'<b>Должность:</b> Директор (Самозанятый)\n'
                         f'<b>Фактический адрес:</b> 603163 г. Нижний Новгород, Деловая 9, корп 1\n'
                         f'<b>Вид деятельности:</b> Выпуск печатной продукции на заказ\n'
                         f'<b>Налоговый орган:</b> Управление Федеральной налоговой службы по Республике'
                         f' Мордовия\n',
                         parse_mode='HTML', reply_markup=kb.comeback)


@router.message(F.text == '❌ Отменить заказ')
async def comeback(message: Message, state: FSMContext):
    await message.answer('❌ Вы нажали на отмену заказа! Возвращение в главное меню...')
    await state.clear()
    await starting_not_new(message)


@router.message(F.text == '💸 Перейти к оплате')
async def pay_till_60rub(message: Message, state: FSMContext):
    await message.answer("✔️ Вы успешно закончили процедуру оформления заказа!\n\n"
                         "💰 Заказы до 60 рублей оплачиваются переводом по номеру!\n\n"
                         "Пожалуйста, оплатите заказ в течении 15 минут, в противном случае заказ "
                         "не будет доставлен.\n\n"
                         f"<b>СУММА:</b> {cd.pay} Руб.\n\n"
                         f"<b>ПЕРЕВОД НА ГАЗПРОМБАНК (через СБП) по номеру:</b> +79271932068",
                         parse_mode='HTML', reply_markup=kb.success_payment)
    await bot.send_message(-1002193083153, "=================================")


