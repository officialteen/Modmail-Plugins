import discord
from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        print(message.type)
        if message.type == discord.MessageType.new_member:
            booster = message.mentions[0]
            embed = discord.Embed(title="Nitro Boost", description=f"{booster.mention}, thank you so much for boosting!", color=0xff0000)
            await message.channel.send(embed=embed)
            
def setup(bot):
    bot.add_cog(BoostPlugin(bot))
