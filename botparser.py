import asyncio
import logging

import aiogram
import aiogram.filters



from config import TOKEN
from app.handlers import router



dp = aiogram.Dispatcher()
bot = aiogram.Bot(token=TOKEN)






async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')