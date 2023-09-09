from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
import json

async def start_command(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Я готов к работе',
                            reply_markup=reply_keyboard)
