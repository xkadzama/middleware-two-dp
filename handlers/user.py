from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command, and_f, or_f



user = Router()


@user.message(CommandStart())
async def start(message: Message):
	in_kb = [
		[InlineKeyboardButton(text='Кнопка 1', callback_data='btn1')]
	]
	markup = InlineKeyboardMarkup(inline_keyboard=in_kb)
	await message.answer('Hello', reply_markup=markup)


@user.callback_query(F.data == 'btn1')
async def reaction(callback: CallbackQuery):
	await callback.message.answer('Ты нажал кнопку!')


@user.message(or_f(Command('help'), Command('info')))
async def help(message: Message):
	await message.answer('Доступные команды: \n/start')


@user.message(F.text.in_(['привет', 'hi', 'ассаламу 1алейкум']))
async def greet(message: Message):
	await message.answer('И тебе привет!')





# @user.message(F.text)
# async def greet(message: Message):
# 	await message.answer('Молодец!')

