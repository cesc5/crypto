FROM python:3.8-alpine

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers", "1", "app:app"]
