import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class PingApplePlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.blurple = 0xFF2B2B

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def pingapple(self, ctx):
        if ctx.channel.id == 679741078630563842:
            await ctx.send(f"<@239357569125187588>")
            await ctx.send(f"<@239357569125187588>")
            await ctx.send(f"<@239357569125187588>")
            await ctx.message.delete()
        else:
            await ctx.message.delete()
                
def setup(bot):
    bot.add_cog(PingApplePlugin(bot))
