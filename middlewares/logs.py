from aiogram import BaseMiddleware


class LoggingMiddleware(BaseMiddleware):
	async def __call__(self, handler, event, data):
		log = f'Пользователь {event.from_user.username} активировал команду: {event.text}'
		print(log)
		with open('logs.txt', mode='a', encoding='UTF-8') as logs:
			logs.write(log + '\n')
		return await handler(event, data) # greet(message, {})


# obj = LoggingMiddleware()
#
# obj('start', 'message', {})





