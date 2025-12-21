from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def yesno_kb() -> InlineKeyboardMarkup:
	in_kb = [
		[InlineKeyboardButton(text='✅ Да', callback_data='yes'),
		 InlineKeyboardButton(text='❌ Нет', callback_data='no')]
	]
	markup = InlineKeyboardMarkup(inline_keyboard=in_kb)
	return markup


def save_reserv_to_file(data, id, username) -> None:
	with open('client_reserv.txt', mode='a', encoding='UTF-8') as file:
		file.write('-----------------------------------\n')
		file.write(f'Имя: {data.get("name")}\n')
		file.write(f'Дата: {data.get("date")}\n')
		file.write(f'Номер телефона: {data.get("phone")}\n')
		file.write(f'ID: {id}\n')
		file.write(f'Пользователь: @{username}\n')
		file.write('-----------------------------------\n')


def pretty_info(data) -> str:
	txt = (f'Имя: {data.get("name")}\n'
	 f'Дата: {data.get("date")}\n'
	 f'Номер телефона: {data.get("phone")}\n\n'
	 f'Все ли корректно?')

	return txt
