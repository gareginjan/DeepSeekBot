# Инструкции по развертыванию Telegram бота

## Варианты хостинга для постоянной работы

### 1. Railway.app (Рекомендуется - бесплатно)

1. Зарегистрируйтесь на https://railway.app
2. Подключите GitHub аккаунт
3. Создайте репозиторий с кодом бота на GitHub
4. В Railway создайте новый проект из GitHub
5. В Environment Variables добавьте:
   - `TELEGRAM_BOT_TOKEN` = ваш токен бота
   - `OPENROUTER_API_KEY` = ваш ключ OpenRouter
6. Railway автоматически развернет бота

### 2. Render.com (Бесплатно с ограничениями)

1. Зарегистрируйтесь на https://render.com
2. Создайте Web Service из GitHub репозитория
3. Настройки:
   - Build Command: `pip install python-telegram-bot aiohttp requests`
   - Start Command: `python main.py`
4. Добавьте переменные окружения

### 3. Heroku (Бесплатно до 550 часов/месяц)

1. Установите Heroku CLI
2. Команды:
```bash
heroku create your-bot-name
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set OPENROUTER_API_KEY=your_key
git push heroku main
```

### 4. VPS/Сервер

1. Установите Python 3.11+
2. Загрузите код бота
3. Установите зависимости: `pip install python-telegram-bot aiohttp requests`
4. Настройте переменные окружения
5. Запустите: `python main.py`
6. Используйте systemd или screen для фоновой работы

## Переменные окружения

Обязательно установите на хостинге:
- `TELEGRAM_BOT_TOKEN` - токен вашего бота
- `OPENROUTER_API_KEY` - ключ OpenRouter API

## Файлы для развертывания

- `main.py` - основной файл бота
- `bot_config.py` - конфигурация
- `openrouter_client.py` - клиент AI API
- `message_memory.py` - память сообщений
- `keep_alive.py` - keep-alive система
- `Procfile` - для Heroku
- `Dockerfile` - для Docker
- `runtime.txt` - версия Python

## После развертывания

Бот будет работать постоянно 24/7 и отвечать на:
- Упоминания слова "Саныч"
- Ответы на свои сообщения
- Помнить 200 сообщений в каждом чате