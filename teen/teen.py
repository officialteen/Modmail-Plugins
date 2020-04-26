import discord
from discord.ext import commands
class TeenPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "+fled" in message.content.lower():
            await message.channel.send("isnt bad")
        elif "+solve" in message.content.lower():
            await message.channel.send("is cute")
        elif "+falls" in message.content.lower():
            await message.channel.send("is a good grinder!")
        elif "+Hecktikz" in message.content.lower():
            await message.channel.send("loves goats")    

def setup(bot):
    bot.add_cog(TeenPlugin(bot))
