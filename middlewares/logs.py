from aiogram import BaseMiddleware
from typing import Dict, Awaitable, Callable, Any
from aiogram.types import Message, CallbackQuery, TelegramObject

class LoggingMiddleware(BaseMiddleware):
	async def __call__(
			self,
			handler: Callable[[TelegramObject], Awaitable[Any]],
			event: TelegramObject,
			data: Dict[Any, Any]
	):
		if isinstance(event, CallbackQuery):
			log = f'Пользователь {event.from_user.username} активировал команду: {event.message.text}'
		elif isinstance(event, Message):
			log = f'Пользователь {event.from_user.username} активировал команду: {event.text}'


		with open('logs.txt', mode='a', encoding='UTF-8') as logs:
			logs.write(log + '\n')
		return await handler(event, data) # greet(message, {})









