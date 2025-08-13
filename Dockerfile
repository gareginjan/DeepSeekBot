FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install python-telegram-bot==22.3 aiohttp==3.12.15 requests==2.32.4

CMD ["python", "main.py"]