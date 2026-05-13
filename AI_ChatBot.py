import asyncio
import aiosqlite

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from ollama import chat
from google import genai

client = genai.Client(api_key="ТВОЙ_API_KEY")
# SETTINGS
TOKEN = ""

DB_NAME = "bot.db"

# BOT
bot = Bot(token=TOKEN)
dp = Dispatcher()

# MODELS

models = {
    "🌐 Gemma 3 (быстро)": "gemma3:4b",
    "Gemini (с распознованием изображений)" : "gemini-3-flash-preview",
}

# DATABASE
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            model TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role TEXT,
            content TEXT
        )
        """)

        await db.commit()


async def set_user_model(user_id, model):
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT OR REPLACE INTO users
            (user_id, model)
            VALUES (?, ?)
            """,
            (user_id, model)
        )

        await db.commit()


async def get_user_model(user_id):
    async with aiosqlite.connect(DB_NAME) as db:

        async with db.execute(
            "SELECT model FROM users WHERE user_id = ?",
            (user_id,)
        ) as cursor:

            row = await cursor.fetchone()

            return row[0] if row else None


async def save_message(user_id, role, content):
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO messages
            (user_id, role, content)
            VALUES (?, ?, ?)
            """,
            (user_id, role, content)
        )

        await db.commit()


async def get_history(user_id, limit=10):
    async with aiosqlite.connect(DB_NAME) as db:

        async with db.execute(
            """
            SELECT role, content
            FROM messages
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (user_id, limit)
        ) as cursor:

            rows = await cursor.fetchall()

            return [
                {
                    "role": role,
                    "content": content
                }
                for role, content in reversed(rows)
            ]


# COMMANDS
@dp.message(Command("start"))
async def start(message: types.Message):

    text = (
        "🤖 AI Chat Bot\n\n"
        "Команды:\n"
        "/models — выбрать модель\n"
        "/clear — очистить память\n\n"
        "После выбора модели просто отправь сообщение."
    )

    await message.answer(text)


@dp.message(Command("models"))
async def models_menu(message: types.Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=name,
                    callback_data=value
                )
            ]
            for name, value in models.items()
        ]
    )

    await message.answer(
        "Выбери модель:",
        reply_markup=keyboard
    )


@dp.message(Command("clear"))
async def clear_history(message: types.Message):

    user_id = message.from_user.id

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            "DELETE FROM messages WHERE user_id = ?",
            (user_id,)
        )

        await db.commit()

    await message.answer("🧹 История очищена")


# MODEL SELECT
@dp.callback_query()
async def choose_model(callback: types.CallbackQuery):

    user_id = callback.from_user.id
    model = callback.data

    await set_user_model(user_id, model)

    await callback.message.answer(
        f"✅ Модель выбрана:\n{model}"
    )

    await callback.answer()

# CHAT
@dp.message()
async def handle_message(message: types.Message):

    user_id = message.from_user.id
    text = message.text

    model = await get_user_model(user_id)

    if not model:
        await message.answer(
            "Сначала выбери модель:\n/models"
        )
        return

    try:

        # сохраняем сообщение пользователя
        await save_message(
            user_id,
            "user",
            text
        )

        # история
        history = await get_history(user_id)

        # typing...
        await bot.send_chat_action(
            message.chat.id,
            "typing"
        )

        # запрос к модели
        if model == "gemma3:4b":
            response = chat(
                model=model,
                messages=history
            )
            answer = response.message.content
        else:
            response = client.models.generate_content(
                model="gemini-3.0-flash-preveiew",
                contents=message
            )

            print(response.text)

        # сохраняем ответ
        await save_message(
            user_id,
            "assistant",
            answer
        )

        # отправляем
        await message.answer(answer)

    except Exception as e:

        print("ERROR:", e)

        await message.answer(
            "❌ Ошибка при генерации ответа"
        )


async def main():

    print("Бот запущен")

    await init_db()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())