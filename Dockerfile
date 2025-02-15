FROM python:3.11

WORKDIR /app

# Install UV and system dependencies
RUN pip install uv && \
    uv pip install --system --upgrade pip setuptools

# Copy dependency files
COPY pyproject.toml .

# Install project dependencies system-wide
RUN uv pip install --system . --verbose

# Copy application code
COPY app/ app/

EXPOSE 5000

CMD ["python", "app/main.py"]