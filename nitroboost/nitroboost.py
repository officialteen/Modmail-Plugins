from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if message.type == discord.MessageType.new_member:
            await message.channel.send("TEST")
            
def setup(bot):
    bot.add_cog(BoostPlugin(bot))
