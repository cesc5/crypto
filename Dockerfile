FROM python:3.8-alpine

ARG PORT
ARG WORKERS

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

ENV PORT ${PORT}
ENV WORKERS ${WORKERS}

EXPOSE ${PORT}

CMD gunicorn -w ${WORKERS} -b 0.0.0.0:${PORT} app:app
