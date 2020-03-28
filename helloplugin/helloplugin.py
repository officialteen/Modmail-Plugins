from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "hello" in message.content.lower():
            await message.channel.send("Hey")
        elif "yo" in message.content.lower():
            await message.channel.send("yo")
        elif "gm" in message.content.lower():
            await message.channel.send("Good Morning")
        elif "gn" in message.content.lower():
            await message.channel.send("Good Night")
        elif "good morning" in message.content.lower():
            await message.channel.send("Good Morning !")
        elif "good night" in message.content.lower(): ==
            await message.channel.send("Good Night !")
        elif "hey" in message.content.lower():
            await message.channel.send("Hello !")
        elif "sup" in message.content.lower():
            await message.channel.send("Sup")
        elif "hi" in message.content.lower():
            await message.channel.send("Hello!")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
