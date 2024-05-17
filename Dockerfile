FROM python:3.10-alpine

ENV TZ=Europe/Berlin

WORKDIR /bot

COPY mensa_menu_bot.py /bot
COPY requirements.txt /bot


RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

ENV API_TOKEN: ${API_TOKEN}
ENV CHANNEL_ID: ${CHANNEL_ID}

CMD ["python", "mensa_menu_bot.py"]