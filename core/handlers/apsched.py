from aiogram import Bot

from core.settings import settings
from status import get_battery_status


async def send_message_time(bot: Bot):
    await bot.send_message(settings.bots.admin_id, get_battery_status())

async def send_message_interval(bot: Bot):
    await bot.send_message(settings.bots.admin_id, get_battery_status())
