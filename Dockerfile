FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Скачиваем wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

CMD ["sh", "-c", "/app/wait-for-it.sh db:5432 -- alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
