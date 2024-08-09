from aiogram import Bot, Dispatcher, executor
from bot.settings import settings
from bot.handlers import register_handlers

bot = Bot(token=settings.bot_token)
dp = Dispatcher(bot)

# Регистрация всех обработчиков
register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
