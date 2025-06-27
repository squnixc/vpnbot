import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import config
from handlers import start, devices, subscription, referral, faq, admin


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(devices.router)
    dp.include_router(subscription.router)
    dp.include_router(referral.router)
    dp.include_router(faq.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
