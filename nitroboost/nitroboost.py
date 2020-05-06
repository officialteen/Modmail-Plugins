import discord
from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        print(message.type)
        if message.type == discord.MessageType.new_member:
            print(message.content)
            a = message.content.replace(" is here", "")
            embed = discord.Embed(title=f"**Nitro Boost**", description=f"{a} thank you so much for boosting <a:BoostingAnimated:707512475246919712> !", color=0xff0000)
            await message.channel.send(embed=embed)
            
def setup(bot):
    bot.add_cog(BoostPlugin(bot))
