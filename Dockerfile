FROM python:3.10-buster

WORKDIR /bbct

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN apt install curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# install dependencies
COPY pyproject.toml /bbct
COPY poetry.lock /bbct
ENV PATH=/root/.poetry/bin:${PATH}
RUN poetry install
COPY . /bbct

EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
