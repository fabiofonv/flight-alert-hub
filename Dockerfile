FROM python:3.13-slim

# Instala ferramentas do sistema e uv
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Copia arquivos de dependência
COPY pyproject.toml uv.lock ./

# Instala dependências do Python
RUN uv sync --frozen --no-cache

# Instala navegadores do Playwright e dependências do SO
RUN uv run playwright install --with-deps chromium

COPY . .

CMD ["uv", "run", "python", "main.py"]