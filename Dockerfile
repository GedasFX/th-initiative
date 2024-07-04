FROM python:3.12-alpine

RUN pip3 install requests uvicorn bs4 fastapi

COPY main.py .

ENTRYPOINT [ "python3", "./main.py" ]