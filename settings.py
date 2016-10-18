import os

ALLOWED_IDS = [int(id) for id in os.environ.get('ALLOWED_IDS', '').split(',')]

BOT_ID = os.environ.get('BOT_ID')