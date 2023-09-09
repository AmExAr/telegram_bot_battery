from aiogram import Bot
from aiogram.types import Message

from status import get_battery_status
from core.settings import settings

async def get_status(message: Message, bot: Bot):
    await message.answer(get_battery_status) if message.from_user.id == settings.bots.admin_id else await message.answer(f'Это не для тебя. И тебе этого не надо')
