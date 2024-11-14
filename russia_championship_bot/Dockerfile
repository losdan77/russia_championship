FROM python:3.12

RUN mkdir /bot

WORKDIR /bot

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

RUN chmod a+x /bot/docker/*.sh

CMD [ "python", "main.py" ]
