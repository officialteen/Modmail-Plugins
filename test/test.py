import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

import asyncio

class NoRcSub(commands.Cog)
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcmute(self, ctx, member : discord.Member):
        role = ctx.guild.get_role(721841017510428744)
        try:
            embed=discord.Embed(title="RC Muted!", description=f"You have been muted from sending RC's in <#586645992007532545> for 3 Days. This is due to sending many videos that do not contain our #'s. (#Hope10KRC - #HopeForHope - #HopeOnTop)", footer="Please be aware of this next time!")
            await member.send(embed=embed)
        except:
            pass

        embed=discord.Embed(title="RC Mute", description=f"{member.mention} has been RC Muted for 3 Days!")
        await ctx.send(embed=embed)

        await member.add_roles(role)
        await asyncio.sleep(259200)
        await member.remove_roles(role)

def setup(bot):
    bot.add_cog(NoRcSub(bot))
