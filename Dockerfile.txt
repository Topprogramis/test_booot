FROM python:3.11-slim

# Указываем рабочую директорию
WORKDIR /app

# Переменная окружения для данных
ENV DATA_DIR=/app/data

# Устанавливаем зависимости (используем vk-api через дефис, так надежнее для pip)
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir vk-api

# Создаем папку для данных и даем полные права
RUN mkdir -p /app/data && chmod 777 /app/data

# Копируем все файлы проекта в контейнер
COPY . .

# Запускаем напрямую без лишних скриптов
CMD ["python", "main.py"]
