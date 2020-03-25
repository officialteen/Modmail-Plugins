from discord.ext import commands
class HelloPlugin(commands.Cog):
    def __init__ (self.bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if  message.content.lower() == "hello":
            await message.channel.send("Hey")
        elif message.content.lower() == "yo":
            await message.channel.send("yo")
        elif message.content.lower() == "gm":
            await message.channel.send("Good Morning")
        elif message.content.lower() == "gn":
            await message.channel.send("Good Night")
        elif message.content.lower() == "good morning":
            await message.channel.send("Good Morning !")
        elif message.content.lower() == "good night":
            await message.channel.send("Good Night !")
        elif message.content.lower() == "hey":
            await message.channel.send("Hello !")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))