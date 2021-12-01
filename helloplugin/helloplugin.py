from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if message.channel.id == "887731496876646444":
            if message.content.lower().startswith("!") or message.content.lower().startswith("?") or message.content.lower().startswith("-") or message.content.lower().startswith("=")or message.content.lower().startswith("*"):
                await message.channel.send("Please only use bot commands in <#888427048882823168>")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
