import discord
from discord.ext import commands

class TestPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    async def whoisacer(self, ctx):
        await ctx.send("Some gay person")

    @whoisAcer.error
    async def whoisacer(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"{ctx.author.mention} you do not have permissions to run this command, Only co owner can")
        
def setup(bot):
    bot.add_cog(TestPlugin(bot))        
