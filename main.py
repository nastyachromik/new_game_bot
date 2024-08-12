import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import return_config
from handlers import user_handlers, other_handlers
from keyboards.set_menu import set_menu

logger = logging.getLogger(__name__)
format = '%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)

async def main():
    config = return_config()
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    await set_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
