import discord
from discord.ext import commands

class Fakeban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = self.bot.main_color
        
    @commands.command()
    async def fban(self, ctx, member: discord.Member = None, reason = None):
        embed = discord.Embed(title="Ban", description=f"{member.mention} Has been banned for {reason}!", color=self.color)
        await ctx.send(embed=embed)           
        
def setup(bot):
    bot.add_cog(Fakeban(bot))
