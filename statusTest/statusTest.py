import discord
from discord.ext import commands
import asyncio

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def change_status_start(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="DM For Help | StormServicing"))
        await asyncio.sleep(5)
        await self.bot.change_presence(activity=discord.Game(name="DM For Purchases | StormServicing"))
        await ctx.send("Done")
    
def setup(bot):
    bot.add_cog(Test(bot))
