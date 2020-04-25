FROM python:3.8-alpine
RUN mkdir /app
WORKDIR /app
COPY test.py .
CMD ["python", "test.py"]
