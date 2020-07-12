FROM python:3.8-alpine
RUN apk add build-base
RUN mkdir /app
WORKDIR /app
COPY "requirements.txt" .
RUN pip install -r requirements.txt
COPY discord_bot.py .
CMD ["python", "discord_bot.py"]
