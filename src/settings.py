from decouple import config


BOT_TOKEN = config('BOT_TOKEN')
DATABASE_URL = config('DATABASE_URL')
MAX_MESSAGES = config('MAX_MESSAGES', default=10, cast=int)
