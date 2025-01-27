# Define a imagem base com Python 3.12
FROM python:3.12-slim as python-base

# Configuração de variáveis de ambiente para Python, pip e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH" \
    PYSETUP_PATH="/opt/pysetup"

# Atualiza pacotes e instala dependências de sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry e verifica a versão
RUN curl -sSL https://install.python-poetry.org | python - \
    && $POETRY_HOME/bin/poetry --version

# Define o diretório de trabalho para instalar dependências
WORKDIR $PYSETUP_PATH

# Copia os arquivos de dependências do projeto
COPY poetry.lock pyproject.toml ./

# Instala as dependências de produção
RUN $POETRY_HOME/bin/poetry install --no-root --no-dev

# Define o diretório de trabalho para o código da aplicação
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app/

# Expõe a porta usada pela aplicação
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]