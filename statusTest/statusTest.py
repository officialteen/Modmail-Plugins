import discord
from discord.ext import commands
import asyncio

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_plugin_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="DM For Help | StormServicing"))
        await asyncio.sleep(5)
        await self.bot.change_presence(activity=discord.Game(name="DM For Purchases | StormServicing"))
    
def setup(bot):
    bot.add_cog(Test(bot))
