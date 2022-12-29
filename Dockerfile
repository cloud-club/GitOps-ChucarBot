FROM python:3.10.8-slim

LABEL name = "ziwoo"


WORKDIR /usr/src/app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "chuucar.py" ]