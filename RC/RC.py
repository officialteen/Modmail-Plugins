import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class RC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rc_f(self, ctx, member: discord.Member):
        fn_role = ctx.guild.get_role(641310880302104576)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_role(fn_role)
        await member.add_role(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Fortnite recruit!",color = 0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title="Welcome to Team Hope",
            description=f"Make sure to check out <#681985501737123997> to prevent being kicked from the team, this includes being professional and leaking things and much more, please check out the channel! Once you have been in Hope for a month, you may request free GFX from our GFX!",
            color=0x06c9ff,
        )
        embed.set_footer(
        text = "Enjoy your stay with Team Hope. we hope you enjoy!"
    )
        await member.send(embed=embed)

def setup(bot):
    bot.add_cog(RC(bot))
