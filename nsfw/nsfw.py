import discord
from discord.ext import commands
import requests

from core import checks
from core.models import PermissionLevel

class NsfwPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    async def gif(self, ctx):
        """Sends a random porn gif"""
        g = requests.get("https://nekobot.xyz/api/image?type=pgif")
        g = g.json()
        url = g["message"]
        embed = discord.Embed()
        embed = discord.Embed(color=0x59E9FF())
        embed.set_image(url=url)
        embed.title = "Here it goes"
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(NsfwPlugin(bot))
