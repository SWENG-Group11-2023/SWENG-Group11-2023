FROM python:3.10.5-buster

RUN mkdir build

WORKDIR /app

COPY ./requirements.txt .
COPY ./app/*.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD python -m uvicorn main:app --host 0.0.0.0 --port 80