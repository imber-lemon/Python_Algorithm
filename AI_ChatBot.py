import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from ollama import chat

TOKEN = "8755267058:AAEMaWBqRpQ9ITZrrCJ_SfG8bDG9XDRFgC8" #неправильный

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_model = {}

models = {
    "🧠 Qwen 3.5": "qwen3.5",
    "🔍 DeepSeek": "deepseek",
    "⚡ Mistral": "mistral",
    "🌐 Gemma": "gemma3:4b"
}

#старт
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Напиши /models чтобы выбрать модель")

#команда выбора модели
@dp.message(Command("models"))
async def models_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=value)]
            for name, value in models.items()
        ]
    )
    await message.answer("Выбери модель:", reply_markup=keyboard)

#выбор модели
@dp.callback_query()
async def choose_model(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    model = callback.data

    user_model[user_id] = model

    await callback.message.answer(f"Модель выбрана: {model}")
    await callback.answer()

#обработка сообщений
@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id

    if user_id not in user_model:
        await message.answer("Сначала выбери модель: /models")
        return

    model = user_model[user_id]
    text = message.text

    response = chat(
        model=model,
        messages=[{'role': 'user', 'content': text}],
    )

    await message.answer(response.message.content)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
