import discord
from discord.ext import commands

class RenzoBanAppeal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        msg = thread.genesis_message

        def check(payload):
            return payload.emoji.name in "✅❌" and payload.message_id == msg.id and not payload.member.bot

        for emoji in "✅":
            await msg.add_reaction(emoji)

def setup(bot):
    bot.add_cog(RenzoBanAppeal(bot))
