import dango

def __init__():
    print(""" 
    █▀ █▀▀ ▀█▀ █░█ █▀█
    ▄█ ██▄ ░█░ █▄█ █▀▀
    """)
    
    bot_token = input("Bot Token: ")
    
    db_host = input("Database Host (localhost or ip): ")
    db_password = input("Database Password: ")
    db_user = input("Database Username: ")
    print("Assume the database name is dangobot since I don't want to mess up stuff. (N-not because I'm lazy)")
    db_database = "dangobot"
    
    try:
        config = f"""CONFIG_VERSION = "{dango.config_version()}"
BOT_TOKEN = "{bot_token}"
DB_HOST = "{db_host}"
DB_DATABASE = "{db_database}"
DB_USER = "{db_user}"
DB_PASSWORD = "{db_password}"
"""
        open('./.env', 'w').write(config)
        print("\n[*] Successfully created .env file!")
    except Exception as e:
        print("\n[!] An error occurred when creating config file.\n" + str(e))
        quit()