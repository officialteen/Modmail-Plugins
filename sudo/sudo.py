import discord
from discord.ext import commands

class Sudo(commands.Cog):
    """Sudo plugin by teen"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sudo(ctx, member: discord.Member, *, message=None):
        await ctx.message.delete()
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(str(message), username=member.name, avatar_url=member.avatar_url)
        
async def setup(bot):
    await bot.add_cog(Sudo(bot))
