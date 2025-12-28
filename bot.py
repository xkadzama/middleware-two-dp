import asyncio
import os

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import MagicData
from aiogram.types import Message
from dotenv import load_dotenv

from handlers.user import user as user_router
from handlers.admin import admin as admin_router
from handlers.group import group as group_router
from handlers.restaraunt import rest as rest_router
from handlers.inline import inline as inline_router

from middlewares.logs import LoggingMiddleware
from middlewares.ban_words import BannWordsMiddleware
from middlewares.subscribe import SubscribeMiddleware

from database.create_db import create_movies_tb

load_dotenv()
bot = Bot(token=os.getenv("API"))
dp = Dispatcher(maintenance_mode=False)

router = Router()
router.message.filter(MagicData(F.maintenance_mode.is_(True)))
router.callback_query.filter(MagicData(F.maintenance_mode.is_(True)))
router.inline_query.filter(MagicData(F.maintenance_mode.is_(True)))

user_router.message.middleware(LoggingMiddleware())
user_router.callback_query.middleware(LoggingMiddleware())
# user_router.message.middleware(BannWordsMiddleware())
# user_router.message.middleware(SubscribeMiddleware(-1003567272004, bot))
# admin_router.message.middleware(LoggingMiddleware())

dp.include_routers(router, user_router, admin_router, group_router, rest_router, inline_router)

create_movies_tb()

@router.message()
async def maintenance_handler(message: Message):
    await message.answer("Проводится тех. обслуживание!")


async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    print("GALO I RUN")
    asyncio.run(main())
    print("GALO I END")
