# Инструкция по переносу проекта в GitHub

## Шаг 1: Подготовка файлов

Ваш проект уже готов для GitHub со всеми необходимыми файлами:

### Основные файлы бота:
- `main.py` - основной файл бота
- `bot_config.py` - конфигурация  
- `openrouter_client.py` - клиент AI API
- `message_memory.py` - память сообщений
- `keep_alive.py` - keep-alive механизм

### Файлы для развертывания:
- `Procfile` - для Heroku
- `Dockerfile` - для Docker/Railway
- `runtime.txt` - версия Python
- `.gitignore` - исключения для Git

### Документация:
- `README.md` - описание проекта
- `deploy_instructions.md` - инструкции по развертыванию

## Шаг 2: Создание репозитория на GitHub

1. Зайдите на https://github.com
2. Нажмите "New repository"
3. Название: `telegram-bot-sanych-deepseek`
4. Описание: `Telegram бот с DeepSeek R1 AI через OpenRouter`
5. Сделайте репозиторий Public или Private
6. НЕ добавляйте README, .gitignore (у нас уже есть)
7. Нажмите "Create repository"

## Шаг 3: Загрузка кода

### Вариант A: Через веб-интерфейс GitHub
1. Скачайте все файлы проекта из Replit
2. На странице нового репозитория нажмите "uploading an existing file"
3. Перетащите все файлы проекта
4. Добавьте commit message: "Initial commit: Telegram bot with DeepSeek R1"
5. Нажмите "Commit new files"

### Вариант B: Через Git командную строку
```bash
git clone https://github.com/ваш-username/telegram-bot-sanych-deepseek.git
cd telegram-bot-sanych-deepseek
# Копируйте все файлы проекта в эту папку
git add .
git commit -m "Initial commit: Telegram bot with DeepSeek R1"
git push origin main
```

## Шаг 4: Проверка загрузки

Убедитесь что все файлы загружены:
- ✅ main.py
- ✅ bot_config.py  
- ✅ openrouter_client.py
- ✅ message_memory.py
- ✅ keep_alive.py
- ✅ README.md
- ✅ Procfile
- ✅ Dockerfile
- ✅ .gitignore

## Шаг 5: Развертывание на Railway.app

1. Зайдите на https://railway.app
2. Нажмите "Start a New Project"
3. Выберите "Deploy from GitHub repo"
4. Подключите GitHub аккаунт
5. Выберите репозиторий `telegram-bot-sanych-deepseek`
6. Railway автоматически обнаружит Python проект
7. Добавьте переменные окружения:
   - `TELEGRAM_BOT_TOKEN` = ваш токен бота
   - `OPENROUTER_API_KEY` = ваш OpenRouter ключ
8. Нажмите "Deploy"

## Шаг 6: Проверка работы

После успешного развертывания:
- Бот будет работать 24/7
- Никаких дополнительных настроек не нужно
- Проверьте работу написав "Саныч" в чат

## Готово!

Ваш бот теперь:
✅ Размещен на GitHub
✅ Работает постоянно на Railway
✅ Отвечает на "Саныч" с AI
✅ Помнит 200 сообщений
✅ Полностью автономен