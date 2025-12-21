import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from utils.restaraunt import yesno_kb, save_reserv_to_file, pretty_info

rest = Router()




class ReservState(StatesGroup): # Наследование
	waiting_for_name = State() # Композиция
	waiting_for_date = State()
	waiting_for_phone = State()



@rest.message(Command('reserv'))
async def reserv(message: Message, state: FSMContext):
	await state.set_state(ReservState.waiting_for_name) # Установить состояние
	await message.answer('Здравствуйте, как к Вам обращаться?')

# Вводит свое имя

@rest.message(ReservState.waiting_for_name)
async def get_date(message: Message, state: FSMContext):
	if len(message.text.split()) != 1:
		await message.answer('Вводите только имя!')
		return # stop

	await state.update_data(name=message.text) # Добавление информации в словарь
	data = await state.get_data()
	print(data)
	await state.set_state(ReservState.waiting_for_date) # Добавление состояния в словарь
	await message.answer('Укажите дату бронирования')

# Вводит дату

@rest.message(ReservState.waiting_for_date)
async def get_phone(message: Message, state: FSMContext):
	date = message.text.split('/')
	if len(date) == 3:
		validate = [num.isdigit() for num in date] # ["10", "05", "2025"]
		if False in validate:
			await message.answer('❌ Некорректные данные')
			return
	else:
		await message.answer('❌ Некорректные данные\n\nПример: 10/05/2025')
		return

	await state.update_data(date=message.text)
	data = await state.get_data()
	print(data)
	await state.set_state(ReservState.waiting_for_phone)
	await message.answer('Укажите номер телефона')

# Вводит номера телефона

@rest.message(ReservState.waiting_for_phone)
async def finish(message: Message, state: FSMContext):
	phone = message.text
	if (phone.startswith('+7') or phone.startswith('8')) and len(message.text) == 12:
		await message.answer('Данные в обработке...')
		await state.update_data(phone=message.text)
		data = await state.get_data()

		markup = yesno_kb()

		await message.answer(pretty_info(data), reply_markup=markup)

		tg_id, username = message.from_user.id, message.from_user.username
		save_reserv_to_file(data, tg_id, username)
		await state.clear()

	else:
		await message.answer('❌ Некорректные данные')


@rest.callback_query(F.data == 'yes')
async def call_yes(callback: CallbackQuery):
	await callback.message.edit_text('Бронь зарегистрирована ✅')


@rest.callback_query(F.data == 'no')
async def call_no(callback: CallbackQuery):
	await callback.message.edit_text('Отмена брони ❌')
	await callback.message.answer('Введите команду /reserv для повтора')


# --------------------------------------------
# Практическое задание:
# Реализовать бота с FSM системой, которая:
# Регистрирует пассажиров на рейс
# 1. Запрашивать имя, фамилию, отчество
# 2. Дату рейса
# 3. Время рейса
# 4. Кол-во билетов
# 5. Страна перелета

# Сохранить всю информацию в файл avia.txt
# --------------------------------------------
# Бонусом:
# Реализовать систему подбора рейса по указанным данным
# (У вас есть готовые рейсы и вы предлагаете их клиенту по:
# дате перелета и стране)

# aviasales = [
#     {'company': 'Победа', 'date': '10/05/2025', 'country': 'Япония'},
#     {'company': 'S7 Airlines', 'date': '15/06/2024', 'country': 'Турция'},
#     {'company': 'Аэрофлот', 'date': '03/12/2024', 'country': 'Германия'},
#     {'company': 'Red Wings', 'date': '22/08/2024', 'country': 'Россия'},
#     {'company': 'Utair', 'date': '30/07/2024', 'country': 'Казахстан'},
#     {'company': 'Победа', 'date': '05/11/2024', 'country': 'Египет'},
#     {'company': 'Nordwind', 'date': '14/02/2025', 'country': 'Таиланд'},
#     {'company': 'Turkish Airlines', 'date': '19/09/2024', 'country': 'США'},
#     {'company': 'Emirates', 'date': '07/01/2025', 'country': 'ОАЭ'}
# ]