from aiogram import BaseMiddleware


class BannWordsMiddleware(BaseMiddleware):
	async def __call__(self, handler, event, data):
		if event.text in ['придурок', 'дурачек', 'нигер']:
			await event.answer('Вынесено предупреждение!')
			return

		return await handler(event, data)