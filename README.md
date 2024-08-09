# Voice AI Bot

This README is available in other languages:
- [Русский](README.ru.md)
- [English](README.md)

This is a Telegram bot built using the Aiogram framework. The bot processes voice messages from users by converting them to text using OpenAI's Whisper API, generating responses using the OpenAI Assistant API, and converting the responses back into voice using OpenAI's TTS API.

## Features

- **Voice-to-Text Conversion:** Converts user voice messages to text using Whisper API.
- **AI-Powered Responses:** Generates contextually relevant responses using OpenAI Assistant API.
- **Text-to-Speech:** Converts the generated text responses into speech using OpenAI TTS API.

## How It Works

1. **User Interaction:** The user sends a voice message to the bot.
2. **Voice-to-Text:** The bot downloads the voice message and uses the Whisper API to transcribe it into text.
3. **AI Response Generation:** The transcribed text is sent to the OpenAI Assistant API, which generates a response based on the input.
4. **Text-to-Speech:** The generated response is then converted back to speech using OpenAI TTS API.
5. **Response Delivery:** The bot sends the voice response back to the user in Telegram.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/voice-ai-bot.git
   cd voice-ai-bot
   ```

2. **Install Dependencies:**
   Make sure you have PDM installed, then run:
   ```bash
   pdm install
   ```

3. **Configuration:**
   Create a `.env` file in the root directory with the following content:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the Bot:**
   Start the bot using:
   ```bash
   pdm run python src/tgBot/main.py
   ```

## Dependencies

- `aiogram`: Telegram Bot API framework.
- `openai`: OpenAI API client.
- `pydantic`: Data validation and settings management.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
