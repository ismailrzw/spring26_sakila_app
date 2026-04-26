# Modified by [m. Ismail] on [26-04-26]
# Sakila System Config

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))