FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV HOST="0.0.0.0"
ENV PORT=8000

EXPOSE 8000

CMD ["python", "main.py"]
