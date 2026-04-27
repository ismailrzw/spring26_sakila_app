# 1. Use a slim base image
FROM python:3.9-slim

# 2. Add Labels (Requirement 27)
LABEL maintainer="Muhammad Ismail Rana"
LABEL version="1.0"
LABEL description="Optimized Sakila Flask Application"

# 3. Set Working Directory
WORKDIR /app

# 4. Leverage Layer Caching: Install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY . .

# 6. Use a non-root user for security
RUN useradd -m sakilauser
USER sakilauser

# 7. Expose ONLY the necessary port
EXPOSE 5000

# 8. Include a HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/health || exit 1

# 9. Run the application
CMD ["python", "app.py"]