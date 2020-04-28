import discord
from discord.ext import commands
class TeenPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    async def tender(self, ctx):
        await ctx.send("Is good")

def setup(bot):
    bot.add_cog(TeenPlugin(bot))
