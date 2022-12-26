FROM python:3.10.8-slim

LABEL name = "ziwoo"

# ARG BOT_TOKEN
# ENV slack_token=$BOT_TOKEN

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "chuucar.py" ]