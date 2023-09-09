from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Статус'
        )
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку \/')
