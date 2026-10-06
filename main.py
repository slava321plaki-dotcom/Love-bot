import asyncio
import datetime
import random
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вставьте сюда ваш токен от @BotFather
TOKEN = "8798102659:AAG80Ugxyv2K43VeChPvlJtvkXqSoclzFOE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Укажите вашу дату отношений (Год, Месяц, День)
START_DATE = datetime.date(2026, 10, 09)

COMPLIMENTS = [
    "Ты делаешь каждый день ярче! ✨",
    "Самая красивая улыбка во вселенной 😊",
    "С тобой даже самый обычный день становится праздником 🎉",
    "Напоминаю: ты невероятная! ❤️",
]

FOOD_IDEAS = ["Пицца 🍕", "Суши 🍣", "Домашняя паста 🍝", "Бургеры 🍔"]


def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="❤️ Комплимент")
    builder.button(text="🗓 Сколько мы вместе?")
    builder.button(text="🍕 Что поесть?")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\nЯ ваш личный семейный бот-помощник.",
        reply_markup=get_main_keyboard(),
    )


@dp.message(F.text == "❤️ Комплимент")
async def send_compliment(message: types.Message):
    compliment = random.choice(COMPLIMENTS)
    await message.answer(f"✨ {compliment}")


@dp.message(F.text == "🗓 Сколько мы вместе?")
async def days_together(message: types.Message):
    today = datetime.date.today()
    days = (today - START_DATE).days
    await message.answer(f"💖 Вы вместе уже **{days}** дней!")


@dp.message(F.text == "🍕 Что поесть?")
async def choose_food(message: types.Message):
    choice = random.choice(FOOD_IDEAS)
    await message.answer(f"🎲 Предлагаю сегодня: **{choice}**!")


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
