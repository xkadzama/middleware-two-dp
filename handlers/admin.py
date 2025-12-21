from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command


admin = Router()

admins_id = [8221154692]

@admin.message(F.from_user.id.in_(admins_id), Command('panel'))
async def panel(message: Message):
	print(message.from_user)
	await message.answer('Вы вошли в панель администратора!')


@admin.message(F.from_user.id.in_(admins_id), Command(commands=['block', 'ban']))
async def block_user(message: Message):
	print(message.from_user)
	await message.answer('Заблокировать')


@admin.message(F.from_user.id.in_(admins_id), Command('warn'))
async def warn(message: Message):
	await message.answer('Вы вынесли предупреждение!')

# Задание
# Реализовать проверку на администратора 3-x хендлеров (сверху) через Middlewarex