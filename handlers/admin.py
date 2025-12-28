from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from database.create_db import connect_db

admin = Router()

admins_id = [8221154692]


@admin.message(F.from_user.id.in_(admins_id), Command("panel"))
async def panel(message: Message):
    print(message.from_user)
    await message.answer("Вы вошли в панель администратора!")


@admin.message(F.from_user.id.in_(admins_id), Command(commands=["block", "ban"]))
async def block_user(message: Message):
    print(message.from_user)
    await message.answer("Заблокировать")


@admin.message(F.from_user.id.in_(admins_id), Command("warn"))
async def warn(message: Message):
    await message.answer("Вы вынесли предупреждение!")


@admin.message(Command('addm')) # /addm Название | Описание | Ссылка на постер
async def add_movie(message: Message):
    no_cmd = message.text.replace('/addm', '').strip()
    items = [i.strip() for i in no_cmd.split("|")]
    if len(items) != 3:
        await message.answer('Некорректные данные:\n\n/addm Название | Описание | Ссылка на постер')
        return

    title, desc, poster_url = items
    print('Название фильма:', title)
    print('Описание:', desc)
    print('Ссылка на постер:', poster_url)
    # Добавить в БД
    conn, cursor = connect_db()
    cursor.execute('''
        INSERT INTO movies (title, description, poster_url)
        VALUES (?, ?, ?)
    ''', (title, desc, poster_url))
    conn.commit()

    await message.answer(f'Фильм {title} успешно добавлен ✅')






