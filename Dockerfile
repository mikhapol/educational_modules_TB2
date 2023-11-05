# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY pyproject.toml .
# Можно так: # COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root
# Если requirements тогда вот так # RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в контейнер
COPY . .
