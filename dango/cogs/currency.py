from discord.ext import commands
import discord
import dango

class Currency(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.cur = dango.managers.database.db_cursor(db)
    
    def get_balance(self, user):
        self.cur.execute("SELECT u.bal FROM Users u WHERE u.user_id = %s", (user.id,))
        return self.cur.fetchone()
    
    def modify_balance(self, user, amount):
        self.cur.execute("SELECT u.bal FROM Users u WHERE u.user_id = %s", (user.id,))
        bal = self.cur.fetchone()
        self.cur.execute("UPDATE Users SET bal = %s WHERE user_id = %s", (bal[0] + amount, user.id))
        self.db.commit()
    
    @commands.command(aliases = ['bal'])
    async def check_bal(self, ctx):
        """Check your balance"""
        user = ctx.message.author
        bal = self.cur.get_balance(user)
        if bal == None:
            bal = 0
        await ctx.send(f"{user.mention} you have {bal} {self.cur.get_currency_name()}")
    
    @commands.command(alias = ['give'])
    async def give(self, ctx, user: discord.User, amount: int):
        """Give currency to another user"""
        if amount < 1:
            await ctx.send("You can't give less than 1 currency")
            return
        if user.id == ctx.message.author.id:
            await ctx.send("You can't give currency to yourself")
            return
        if amount > self.cur.get_balance(ctx.message.author):
            await ctx.send("You don't have enough currency to give")
            return
        self.modify_balance(ctx.message.author, -amount)
        self.modify_balance(user, amount)
        await ctx.send(f"{ctx.message.author.mention} gave {amount} {self.cur.get_currency_name()} to {user.mention}")

def setup(bot, db):
    bot.add_cog(Currency(bot, db))