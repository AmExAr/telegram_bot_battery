from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import asyncio

from core.settings import settings
from core.handlers.basic import start_command
from core.handlers.status_battery import get_status
from core.handlers.apsched import send_message_interval, send_message_time
from core.handlers.bot_status import start_bot, stop_bot



async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

    dp = Dispatcher()
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10), kwargs={'bot': bot})
    scheduler.add_job(send_message_interval, trigger='interval', hours=5, kwargs={'bot': bot})
    scheduler.start()

    dp.message.register(start_command, Command(commands=['start', 'run']))
    dp.message.register(get_status, F.text.lower() == 'статус')
    dp.message.register(get_status, F.text.lower() == 'status')
    dp.message.register(get_status, Command(commands=['status']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
