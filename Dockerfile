FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN apk add curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# install dependencies
COPY . /usr/src/app
# for requests
RUN apk add gcc musl-dev libffi-dev
# for cryptography
RUN apk add rust
ENV PATH=/root/.poetry/bin:/root/.cargo/bin:${PATH}
RUN poetry install

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
