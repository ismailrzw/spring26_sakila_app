
# Muhammad Ismail Rana
# 26-04-2026

# Configuration for Sakila
# This file handles the database connection settings.
# Combined Configuration

import os

class Config:
    """Base configuration class for the Sakila Flask application."""
    
    # Database Settings
    # Task A2: Using 'sakila-db-server' as the default host
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    # Connection and Performance Settings
    # Task A2: Added timeout and health check variables
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')
