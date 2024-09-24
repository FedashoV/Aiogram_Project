from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage
from config import TOKEN

import keyboards_ru as kb
import handlers_ru as hd

bot = Bot(token=TOKEN)
con_router = Router()
pay = 0
timeout_cnt = 0


class Order(StatesGroup):
    name = State()
    room = State()
    time = State()
    papers = State()
    comment = State()
    document = State()


@con_router.message(F.text == "🖨️ Распечатать 🖨️")
async def user_name(message: Message, state: FSMContext):
    await state.set_state(Order.name)
    await message.answer('🗣 Как к вам обращаться?', reply_markup=kb.delete_delivery)


@con_router.message(Order.name)
async def user_room(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Order.room)
    await message.answer(f'🚪 Введите разборчиво номер вашей комнаты и корпус\n\n'
                         f'<b><i>💡 Пример: 417 (2)</i></b>', reply_markup=kb.delete_delivery,
                         parse_mode='HTML')


@con_router.message(Order.room)
async def time(message: Message, state: FSMContext):
    await state.update_data(room=message.text)
    await state.set_state(Order.time)
    await message.answer('🕓 Введите удобное время для получения заказа.\n\n'
                         f'<i>💡 Пример: 24.04.2024 (18:00)</i>', parse_mode='HTML',
                         reply_markup=kb.delete_delivery)
    await message.answer('🗓️ Доступные интервалы вы можете посмотреть, нажав на ссылку:',
                         reply_markup=kb.yandex_disk)


@con_router.message(Order.time)
async def count_of_paper(message: Message, state: FSMContext):
    await state.update_data(timing=message.text)
    await state.set_state(Order.papers)
    await message.answer('🗐 Введите количество страниц, которое необходимо распечатать',
                         reply_markup=kb.delete_delivery)


@con_router.message(Order.papers)
async def comment(message: Message, state: FSMContext):
    await state.update_data(paper=message.text)
    await state.set_state(Order.comment)
    await message.answer(f'💬 Сейчас вы можете написать комментарий к заказу',
                         parse_mode='HTML', reply_markup=kb.keyboard_for_comment)


@con_router.message(Order.comment)
async def comm(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await state.set_state(Order.document)
    await message.answer(f'🖼️ Пожалуйста, отправьте файлы или фотографии (до 10 штук) <b>ОДНИМ</b> сообщением!',
                         parse_mode='HTML', reply_markup=kb.delete_delivery)


@con_router.message(Order.document)
async def payment(message: Message, state: FSMContext):
    full_information = await state.get_data()
    try:
        count = int(full_information["paper"])
        await pay_pay(message, state)

    except ValueError:
        await message.answer("❌Ошибка! Вы ввели неверное количество листов! Совершите заказ заново и укажите "
                             "количество цифрой!")
        await state.clear()
        await hd.starting(message)


@con_router.message(F.text == "КОД22548962152253КОД")
async def pay_pay(message: Message, state: FSMContext):
    global pay
    global timeout_cnt
    full_information = await state.get_data()
    paper_count = int(full_information["paper"])
    flag = False
    if 1 <= paper_count <= 3:
        pay = 10 * paper_count
        flag = True
    elif 4 <= paper_count <= 6:
        pay = 8 * paper_count
        flag = True
    elif 7 <= paper_count <= 9:
        pay = 7 * paper_count
        flag = True
    elif 10 <= paper_count <= 29:
        pay = 6 * paper_count
        flag = True
    elif 30 <= paper_count <= 1000000:
        pay = 5 * paper_count
        flag = True

    else:
        await message.answer("❌Ошибка! Вы ввели неверное количество листов! Совершите заказ заново и укажите "
                             "количество цифрой!")
        await state.clear()
        await hd.starting(message)

    if flag is True:
        if 0 < pay < 60:
            await message.answer(text='⚙️Обработка...Нажмите на кнопку ниже.', reply_markup=kb.payment1)
            await documentation(message, state)

        elif 60 <= pay < 1000000:
            await message.answer(text='⚙️Обработка...Нажмите на кнопку ниже.', reply_markup=kb.payment2)
            await documentation(message, state)

        else:
            await message.answer("Произошла неизвестная ошибка. Попробуйте сделать заказ ещё раз либо "
                                 "попробуйте позже!")


async def documentation(message: Message, state: FSMContext):
    global pay
    full_information = await state.get_data()
    await bot(SendMessage(chat_id=-1002193083153,
                          text=f'<b>НОВЫЙ ЗАКАЗ!!!!!</b>\n\n'
                               f'<b>ИМЯ:</b> {full_information["name"]}\n'
                               f'<b>КОМНАТА:</b> {full_information["room"]}\n'
                               f'<b>ВРЕМЯ: </b>{full_information["timing"]}\n\n'
                               f'<b>КОММЕНТАРИЙ: </b>{full_information["comment"]}',
                          parse_mode='HTML'))
    await bot.forward_message(-1002193083153, message.from_user.id, message.message_id)
    await state.clear()



