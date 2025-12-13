from aiogram import BaseMiddleware, Bot

class SubscribeMiddleware(BaseMiddleware):
	def __init__(self, chat_id, bot: Bot):
		self.chat_id = chat_id
		self.bot = bot

	async def __call__(self, handler, event, data):

		is_join = await self.bot.get_chat_member(
			self.chat_id,
			event.from_user.id
		)
		print(is_join) # creator administrator member left
		if is_join.status in ['creator', 'administrator', 'member']:
			return await handler(event, data)

		await event.answer('Вы не состоите в беседе ❌')
		await event.answer('Ссылка на канал: ...')

