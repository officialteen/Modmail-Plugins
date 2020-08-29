import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="dothis")
    async def do_this_pls(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="DM For Help | StormServicing"))
        await ctx.send("Done")
    
def setup(bot):
    bot.add_cog(Test(bot))
