from discord.ext import commands
# import lavalink -> halp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Music(bot))