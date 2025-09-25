import os
import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import config
from handlers import start, devices, subscription, referral, faq
from admin import router as admin_router
from db import close_pool, init_pool, ping


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await init_pool()
    assert await ping(), "DB ping failed"
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(devices.router)
    dp.include_router(subscription.router)
    dp.include_router(referral.router)
    dp.include_router(faq.router)
    dp.include_router(admin_router)

    try:
        await dp.start_polling(bot)
    finally:
        await close_pool()


if __name__ == "__main__":
    if os.name == "nt":
        # psycopg async не дружит с ProactorEventLoop
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
