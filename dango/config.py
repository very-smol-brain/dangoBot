import os 

def bot_token():
    return os.getenv('BOT_TOKEN')

def bot_prefix():
    return ['$d', '$D']

def bot_status():
    return "🍡"

def db_host():
    return os.getenv('DB_HOST')

def db_database():
    return os.getenv('DB_DATABASE')

def db_user():
    return os.getenv('DB_USER')

def db_password():
    return os.getenv('DB_PASSWORD')

def minecraft_logs():
    return os.getenv('MINECRAFT_LOGS')

def minecraft_channel():
    return os.getenv('MINECRAFT_CHANNEL')