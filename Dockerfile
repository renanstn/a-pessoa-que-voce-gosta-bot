FROM python:3.8

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

CMD ["python", "main.py"]
