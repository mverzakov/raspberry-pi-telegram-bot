import os

ALLOWED_IDS = os.environ.get('ALLOWED_IDS', '').split(',')

BOT_ID = os.environ.get('BOT_ID')