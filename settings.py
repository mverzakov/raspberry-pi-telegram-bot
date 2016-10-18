import os

ALLOWED_IDS = [int(id) for id in os.environ.get('ALLOWED_IDS', '').split(',')]

BOT_ID = os.environ.get('BOT_ID')

TORRENT_DIRS = {
    'Music': 'path/to/music',
    'Movies': 'path/to/movies',
    'TV Series': 'path/to/series',
    'Other': 'path/to/other',
}