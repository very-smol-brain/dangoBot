import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from os.path import join, dirname
import dango

print("🍡 Loading DangoBot...")

load_dotenv(join(dirname(__file__), '.env')) # Gets env file in current directory

if os.getenv('CONFIG_VERSION') != dango.config_version():
    if os.path.isfile('.env'):
        print("Invalid environment configuration. Please delete .env and run DangoBot.py again")
        exit()
    print("Setting up environment...")
    dango.setup.__init__() # Runs setup.py


db = dango.managers.database.__init__() # Initialises db


intents = discord.Intents.default() # Sets intents and prefix
intents.members = True
intents.typing = False

bot = commands.Bot(intents = intents, command_prefix = dango.config.prefix())

@bot.event
async def on_ready(): # Initialises on_ready and cogs
    print("\n[*] DangoBot is ready!\n")
    dango.cogs.cmds.setup(bot) 
    dango.cogs.currency.setup(bot, db)
    dango.cogs.minecraft.setup(bot)
    dango.cogs.music.setup(bot)
    dango.cogs.speechify.setup(bot)
    dango.cogs.stats.setup(bot, db)
    
    user_list = bot.get_all_members()
    for user in user_list:
        dango.managers.database.add_user(user)
    
    await bot.change_presence(activity = discord.Game(name = dango.config.bot_status()))

@bot.event 
async def on_member_join(member):
    dango.managers.database.add_user(member)
    print("\n[*] {} has joined the server!\n".format(member.name))

try: # Try to connect to discord api
    bot.run(dango.config.token())
except Exception as err:
    print("\n[!] Unable to connect to discord!\n {}".format(err))
    exit()
    
# Decouple currency from Users table later