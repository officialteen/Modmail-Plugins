import discord
from discord.ext import commands

class testPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

@commands.command()
@commands.has_role("❰ CO OWNER ❱")
async def whoisAcer(self, ctx):
    await ctx.send("Some gay person")

@whoisAcer.error
async def whoisAcer(self, ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"{ctx.author.mention} you do not have permissions to run this command, Only co owner can")
        
def setup(bot):
    bot.add_cog(testPlugin(bot))        
