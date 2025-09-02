FROM python:3.13-alpine3.21

RUN pip install tornado

COPY . /app
WORKDIR /app
CMD ["python", "back.py"]