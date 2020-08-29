import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listiner()
    async def on_plugin_ready():
        await self.bot.change_presence(activity=discord.Game(name="DM For Help | StormServicing"))
    
def setup(bot):
    bot.add_cog(Test(bot))
