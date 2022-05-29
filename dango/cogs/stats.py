from pickle import NONE
from discord.ext import commands
import discord
import dango

class Stats(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.cur = dango.managers.database.db_cursor(db)
    
    def get_zid(self, user):
        self.cur.execute("SELECT zid FROM Users WHERE user_id = %s", (user.id,))
        return self.cur.fetchone()
    
    @commands.command(aliases = ['zid'])
    async def zid(self, ctx, user: discord.User):
        """Get zid mentioned by user"""
        zid = self.get_zid(user)
        if zid == None:
            await ctx.send(f"{user.mention} has no zid")
        else:
            await ctx.send(f"{user.mention}'s zid is {zid[0]}")
    
def setup(bot, db):
    bot.add_cog(Stats(bot, db))