FROM python:latest
LABEL authors="blockmento"

ADD app .

RUN pip install telethon requests
ENTRYPOINT ["python3", "./main.py"]