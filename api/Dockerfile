FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip3 install sqlalchemy
RUN pip3 install pymysql
RUN pip3 install cryptography

COPY ./app /app
