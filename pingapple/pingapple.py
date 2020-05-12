import discord
from discord.ext import commands

class PingApplePlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.blurple = 0xFF2B2B

    @commands.command()
    async def pingapple():
        if ctx.channel.id == 679741078630563842
        await ctx.send(f"<@239357569125187588>")
        await ctx.send(f"<@239357569125187588>")
        await ctx.send(f"<@239357569125187588>")

    @pingapple.error
    async def pingapple_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(
                title = "Error"
                description = f"This command can only be used in <#679741078630563842>"
                color = self.blurple
            )
            await ctx.send(embed=embed)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(PingApplePlugin(bot))
