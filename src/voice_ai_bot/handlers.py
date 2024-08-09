import openai
from aiogram import Dispatcher, types
from bot.settings import settings

openai.api_key = settings.openai_api_key

async def handle_voice_message(message: types.Message):
    # Получаем файл голосового сообщения
    file_info = await message.bot.get_file(message.voice.file_id)
    file_path = file_info.file_path
    file_url = f'https://api.telegram.org/file/bot{settings.bot_token}/{file_path}'

    # Преобразование аудио в текст
    response = openai.Audio.transcribe(file=open(file_url, "rb"))
    text = response['text']

    # Получение ответа от OpenAI Assistant
    response = await openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    answer_text = response.choices[0].message['content']

    # Озвучка ответа
    tts_response = openai.Audio.create(text=answer_text)
    audio_url = tts_response['audio_url']

    # Отправка голосового ответа
    await message.answer_voice(voice=audio_url)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_voice_message, content_types=types.ContentType.VOICE)
