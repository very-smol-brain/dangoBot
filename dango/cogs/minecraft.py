from discord.ext import commands, tasks
import os
import dango

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.minecraft_dir = dango.config.minecraft_logs()
    
    @tasks.loop(seconds = 5)
    async def print_logs(self):
        if os.path.getmtime(self.minecraft_dir) > dango.time.timestamp() + 6:
            with open(self.minecraft_dir, 'r') as f:
                logs = f.readlines()
                await self.bot.get_channel(dango.config.minecraft_channel()).send(logs[-1])

def setup(bot):
    bot.add_cog(Minecraft(bot))