# Dockerfile
FROM python:3.11-slim

LABEL author="mle-student"

# Создание рабочей директории
WORKDIR /app

# Копируем все файлы в рабочую директорию
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Указываем порт, который будет слушать приложение внутри контейнера
EXPOSE ${APP_PORT}

# Команда запуска FastAPI-приложения
CMD uvicorn ml_service.main:app --host 0.0.0.0 --port ${APP_PORT}

