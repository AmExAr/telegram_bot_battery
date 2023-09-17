from aiogram import Bot
from aiogram.types import Message

from core.settings import settings
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, "Я запустился")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Я умер")
