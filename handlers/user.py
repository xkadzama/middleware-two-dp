from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, and_f, or_f


user = Router()


@user.message(CommandStart())
async def start(message: Message):
	await message.answer('Hello')


@user.message(or_f(Command('help'), Command('info')))
async def help(message: Message):
	await message.answer('Доступные команды: \n/start')


@user.message(F.text.in_(['привет', 'hi', 'ассаламу 1алейкум']))
async def greet(message: Message):
	await message.answer('И тебе привет!')


# @user.message(F.text)
# async def greet(message: Message):
# 	await message.answer('Молодец!')

