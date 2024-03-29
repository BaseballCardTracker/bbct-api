FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat

# install curl
RUN apt install -y curl

# create user
RUN useradd -ms /bin/bash bbct
RUN mkdir -p /bbct/static
RUN chown -R bbct /bbct
USER bbct

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# install dependencies
WORKDIR /bbct
COPY pyproject.toml /bbct
COPY poetry.lock /bbct
ENV PATH=/home/bbct/.local/bin:${PATH}
RUN poetry install
COPY --chown=bbct . /bbct

EXPOSE 8000
ENTRYPOINT ["/bbct/entrypoint.sh"]
