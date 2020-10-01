from decouple import config


HEROKU_URL = config('HEROKU_URL')
PORT = config('PORT', default=5000)
BOT_TOKEN = config('BOT_TOKEN')
MAX_MESSAGES = config('MAX_MESSAGES', default=10, cast=int)
HM_CHANCES = config('HM_CHANCES', default=0.4, cast=float)
DATABASE_URL = config(
    'DATABASE_URL',
    default='postgresql://postgres:admin@postgres:5432/postgres'
)
