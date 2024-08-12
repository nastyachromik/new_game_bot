from aiogram import Router
from aiogram.types import Message
from lexicon.commands_dict import LEXICON_RU
from keyboards.main_keyboard import yes_no_keyboard

router = Router()
@router.message()
async def start_func(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'], reply_markup=yes_no_keyboard)