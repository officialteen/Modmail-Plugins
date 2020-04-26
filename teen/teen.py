import discord
from discord.ext import commands
class TeenPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "+fleg" in message.content.lower():
            await message.channel.send("fled = bad (jk)")

def setup(bot):
    bot.add_cog(TeenPlugin(bot))
