import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class userID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def userid(self, ctx):
        member = ctx.thread.recipient
        if member == None:
            member = ctx.author
        await ctx.send(f"{member.mention}'s ID is {member.id}")

def setup(bot):
    bot.add_cog(userID(bot))
