import os

# Muhammad Ismail Rana
# 26-04-2026

# Sakila Application Configuration
# This file handles the database connection settings.
# Combined Configuration

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))