FROM python:3.10-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN apt install curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# install dependencies
COPY . /usr/src/app
ENV PATH=/root/.poetry/bin:${PATH}
RUN poetry install

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
