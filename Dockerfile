FROM python:3.8

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
COPY ./src /app/

CMD ["python", "main.py"]
