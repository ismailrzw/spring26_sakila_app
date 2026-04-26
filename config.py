import os

# Muhammad Ismail Rana
# 26-04-2026

# Sakila Application Configuration
# This file handles the database connection settings.

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'supersecretpassword')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))