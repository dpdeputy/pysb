# Stage 1: Builder
FROM python:3.12-slim as builder

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency definition files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv pip install --system --no-cache .

# Copy the application source code
COPY src/ ./src/

# Stage 2: Final Image
FROM python:3.12-slim

WORKDIR /app

# Create a non-root user
RUN useradd --create-home appuser
USER appuser

# Copy installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy the application source code
COPY --chown=appuser:appuser src/ ./src/

EXPOSE 8888

CMD ["python", "-m", "{{ module_name }}.main"]
