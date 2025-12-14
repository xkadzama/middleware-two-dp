from aiogram import Router, F, Bot
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import CommandStart, Command, and_f, or_f


group = Router()


@group.my_chat_member() # <-- взаимодействие с ботом в беседах
async def touch_bot(event: ChatMemberUpdated, bot: Bot):
	group_name = event.chat.title
	bot_name = event.old_chat_member.user.first_name
	old_status = event.old_chat_member.status
	new_status = event.new_chat_member.status
	if new_status == 'left' or new_status == 'kicked':
		print(f'Бота {bot_name} кикнули с {group_name}')
		await bot.send_message(8221154692, 'bca')
	elif old_status == 'member' and new_status == 'administrator':
		log = f'Бота {bot_name} повысили с {old_status} до {new_status}'
		await bot.send_message(8221154692, log)



@group.chat_member() # <-- взаимодействие с пользователями в беседах (бот должен присутствовать там)
async def touch_user(event: ChatMemberUpdated):
	user_name = event.old_chat_member.user.username
	old_status = event.old_chat_member.status
	new_status = event.new_chat_member.status
	print(f'Пользователь: {user_name}')
	print(f'Старый статус: {old_status}')
	print(f'Новый статус: {new_status}')
