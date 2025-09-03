import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import config
from handlers import start, devices, subscription, referral, faq
from admin import router as admin_router
from db import init_db


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    init_db()
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(devices.router)
    dp.include_router(subscription.router)
    dp.include_router(referral.router)
    dp.include_router(faq.router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
