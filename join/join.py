import discord
from discord.ext import commands

class JoinHope(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if all(word in message.content.lower() for word in ("how", "become", "staff")):
            embed = discord.Embed(description="If you are looking to join Team Hope, make sure to check out the <#681999546028392639> channel! Please watch the video relating to what team you want to join: Valorant, COD, or Fortnite.\n\nHere are some extra tips to help you join!\n`1` Use our tags (#Hope8KRC, #HopeOnTop, #HopeWZRC, #HopeVLTRC)\n`2` Be active in our discord server! This is one of the best ways to get recognised!  Good luck grinding!",color=0x06c9ff)
            embed.set_author(name="How to join Team Hope",icon_url="https://cdn.discordapp.com/attachments/639774534639288330/710608697906167908/Hope_new_bot_logo_blue.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/639774534639288330/710609985221951558/extra-bot-logo2.png")
            await message.author.send(embed=embed)
            embed = discord.Embed(
                description= f"Hey {message.author.mention}, You have been sent a DM on how to join Team Hope!",
                color= 0x06c9ff
            )
            await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(JoinHope(bot))
