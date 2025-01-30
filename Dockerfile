# Base Python 3.12
FROM python:3.12-slim as python-base

# Configurações de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adiciona o Poetry e o ambiente virtual ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl build-essential libpq-dev gcc python3-distutils python3-setuptools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version

# Criar diretório de trabalho para dependências
WORKDIR $PYSETUP_PATH

# Copiar arquivos de dependência
COPY pyproject.toml poetry.lock ./

# Regenerar o arquivo poetry.lock
RUN poetry lock

# Instalar dependências do projeto sem as de desenvolvimento
RUN poetry install --no-dev --no-root

# Configurar diretório de trabalho para a aplicação
WORKDIR /app

# Copiar os arquivos do projeto
COPY . /app/

# Expor porta da aplicação
EXPOSE 8000

# Rodar aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
