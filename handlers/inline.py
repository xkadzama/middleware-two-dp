import sqlite3
from uuid import uuid4

import telebot.asyncio_helper
import telebot.types
from aiogram import Router
from aiogram.types import (Message, InlineQuery,
                           InlineQueryResultPhoto, InlineQueryResultArticle,
                           InputTextMessageContent)

inline = Router()


@inline.inline_query()
async def show_movies(query: InlineQuery):
	search = query.query
	with sqlite3.connect('database.db') as conn:
		cursor = conn.cursor()
		cursor.execute('''
			SELECT * FROM movies WHERE title LIKE ?
		''', (f'%{search}%',))

		result = cursor.fetchall()
		print(result)
		cards = []
		for row in result:
			title, desc, poster_url = row[1], row[2], row[3]

			card = InlineQueryResultPhoto(
				id=str(uuid4()),
				photo_url=poster_url,
				thumbnail_url=poster_url,
				title=title,
				description=desc,
				caption=f'Название фильма: {title}\n\nОписание: {desc}',
				show_caption_above_media=True
			)

			# card = InlineQueryResultArticle(
			# 	id=str(uuid4()),
			# 	title=title,
			# 	description=desc,
			# 	input_message_content=InputTextMessageContent(
			# 		message_text=f'Название фильма: {title}\n\nОписание: {desc}'
			# 	),
			# 	thumbnail_url=poster_url
			# )


			cards.append(card)

		await query.answer(results=cards, cache_time=1, is_personal=True)

# Реализовать момент с добавлением фильма в избранные







