import discord
from discord.ext import commands
import asyncio

class RenzoBanAppeal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread):
        msg = thread.genesis_message

        def check(payload):
            return payload.emoji.name in "✅" and payload.message_id == msg.id and not payload.member.bot

        for emoji in "✅":
            await msg.add_reaction(emoji)

        try:
            payload = await self.bot.wait_for("raw_reaction_add", timeout=None, check=check)
        except asyncio.TimeoutError:
            pass

        else:
            if payload.emoji.name == "✅":
                try:
                    await thread.recipient.ban()
                    embed = discord.Embed(
                        title="Declined and Banned",
                        description=f"{payload.member.mention} declined {thread.recipient.mention}'s appeal.\n\n{thread.recipient.mention} has been banned.",
                        color=0x0000FF
                    )
                    await thread.channel.send(embed=embed)
                    await thread.close(closer=payload.member)
                except:
                    return await msg.channel.send(f"Couldn't Ban {thread.recipient}! :(")


def setup(bot):
    bot.add_cog(RenzoBanAppeal(bot))