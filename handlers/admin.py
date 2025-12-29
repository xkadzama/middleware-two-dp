import sqlite3

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

# CRUD
# CREATE
@admin.message(Command('addm')) # /addm Название | Описание | Ссылка на постер
async def add_movie(message: Message):
    no_cmd = message.text.replace('/addm', '').strip()
    items = [i.strip() for i in no_cmd.split("|")]
    if len(items) != 3:
        await message.answer('Некорректные данные:\n\n/addm Название | Описание | Ссылка на постер')
        return

    title, desc, poster_url = items
    if not poster_url[0:4] in ('http', 'https'):
        await message.answer('Неправильная ссылка на постер')
        return

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

# READ
@admin.message(Command('showm')) # Форпост
async def show_movies(message: Message):
    cmd = message.text.replace('/showm', '').strip() # Форпост
    if cmd == '-10': # Форпост == '-10'
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM movies
            ''')
            films = cursor.fetchall()[0:10]
            for film in films:
                title, desc, poster_url = film[1], film[2], film[3]
                await message.answer_photo(
                    poster_url, caption=f'Название фильма: {title}\n\nОписание: {desc}'
                )
            return

    if len(cmd) >= 3: # 7 >= 3 = True
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM movies WHERE title == ?
            ''', (cmd,))
            film = cursor.fetchone()
            title, desc, poster_url = film[1], film[2], film[3]
            await message.answer_photo(
                poster_url, caption=f'Название фильма: {title}\n\nОписание: {desc}'
            )


# DELETE
@admin.message(Command('delm')) # /delm Название
async def del_movie(message: Message):
    title = message.text.replace('/delm', '').strip()
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM movies WHERE title == ?
        ''', (title,))
        conn.commit()

    await message.answer(f'Фильм {title} успешно удален!')


# UPDATE
# Пример команд:
# ------------------------
# /upd Мстители [описание](Это такой-то фильм...)
# ------------------------
# /upd Название [описание](текст нового описания)
# /upd Название [постер](ссылка на новый постер)
# /upd Название [название](новое название фильма)












