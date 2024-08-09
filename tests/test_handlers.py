# src/tests/test_handlers.py

import pytest
from aiogram import types
from tgBot.handlers import handle_voice_message
from tgBot.settings import settings  # Удалите, если не используете


@pytest.mark.asyncio
async def test_handle_voice_message(mocker):
    # Мокируем методы, чтобы не вызывать реальные API
    mock_get_file = mocker.patch('aiogram.Bot.get_file')
    mock_openai_transcribe = mocker.patch('openai.Audio.transcribe')
    mock_openai_chat = mocker.patch('openai.ChatCompletion.create')
    mock_openai_tts = mocker.patch('openai.Audio.create')
    
    # Настройка mock-объектов
    mock_get_file.return_value = types.File(file_id="file_id", file_path="file_path")
    mock_openai_transcribe.return_value = {"text": "Привет, как дела?"}
    mock_openai_chat.return_value = {"choices": [{"message": {"content": "Все хорошо, спасибо!"}}]}
    mock_openai_tts.return_value = {"audio_url": "https://example.com/audio.mp3"}
    
    # Создаем фейковое сообщение
    message = types.Message(voice=types.Voice(file_id="file_id"), chat=types.Chat(id=1), message_id=1)
    
    # Вызываем обработчик
    await handle_voice_message(message)
    
    # Проверяем, что вызовы были сделаны правильно
    mock_get_file.assert_called_once()
    mock_openai_transcribe.assert_called_once()
    mock_openai_chat.assert_called_once()
    mock_openai_tts.assert_called_once()

