from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Проверка работы бота'
        ),
        BotCommand(
            command='status',
            description='Статус работы'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
