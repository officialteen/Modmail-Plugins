import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime

class allInOne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x00FF00

    @tasks.loop(seconds=10)
    async def loopy(self):
        guild = self.bot.get_guild(717859817032515755)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"SSC | DM FOR HELP | {guild.member_count} MEMBERS"))
        await asyncio.sleep(5)

    @commands.command(name="start_status")
    async def start_the_status(self, ctx):
        self.loopy.start()
        await ctx.send("Started! If you are encountering any issues please run this command again!")

    @commands.command(name="rule")
    async def rule_command(self, ctx, ruleNum = None):
        if not ruleNum:
            await ctx.send("Hey there! This is the rules command, please include the Rule Number and ill let you know what it is!")
        else:
            if ruleNum == 1:
                await ctx.send("Discord Terms of Service can be found here: https://discord.com/new/terms. Discord needs you to be 13 or above to join this server.")
            elif ruleNum == 2:
                await ctx.send("YT Terms of Service can be found here: https://www.youtube.com/static?template=terms, Twitch Terms of Service can be found here: https://www.twitch.tv/p/legal/terms-of-service/")
            elif ruleNum == 3:
                await ctx.send("No swearing, gory language, 18+ images or text should be posted here. This is a family friendly server and if you do that you will be punished. Don't have your status, name or profile picture say anything inappropriate. Please have ping-able names, this means at least having a few normal characters where staff can ping you if necessary.")
            elif ruleNum == 4:
                await ctx.send("Only advertise in the correct areas, look above in the FAQ for a list of all the advertising channels possible. Only promote in the correct areas. Please do not direct message members with any sort of promotion as that will be a ban.")
            elif ruleNum == 5:
                await ctx.send("All punishment is up to staff and if you think you were falsely punished or want to report a staff <@735200954026033286>. Staff can punish you at any time for any reason and have the final say.")
            elif ruleNum == 6:
                await ctx.send("Do not talk about self harm or suicide here. While it is important this is not the right place, if you or a friend is contemplating suicide call this number: 1-800-273-8255. Please do not post downloadable files or anything that is spyware, malware or any type of ip grabber or hack. The bots advertised in <@720712592812671057> are use at your own risk.")
            elif ruleNum > 6 or ruleNum <= 0:
                await ctx.send("This rule has not been found!")

    @commands.command(name="welcome", aliases=['wel'])
    async def welcome_cmd(self, ctx):
        await ctx.send("Welcome to the server, we hope you have a great time here!")

    @commands.command(name="topic")
    async def topic_cmd(self, ctx):
        await ctx.send("Welcome to the server, we hope you have a great time here!")

    @commands.command(name="patreon")
    async def patreon_cmd(self, ctx):
        await ctx.send("https://www.patreon.com/smallcreatorscommunity")

    @commands.command(name="boost")
    async def boost_cmd(self, ctx):
        await ctx.send("The booster rewards are, a free growth raid, and access to all 3 premium advertising channels, along with all chat perms!")

    @commands.command(name="verify")
    async def verify_cmd(self, ctx):
        await ctx.message.add_reactions("✅")
        await asyncio.sleep(3)
        await ctx.message.delete()
        # Verify roles
        role1 = ctx.guild.get_role(718174958936653884)
        role2 = ctx.guild.get_role(726859506339938365)
        role3 = ctx.guild.get_role(725807695990358057)
        role4 = ctx.guild.get_role(726853712320004227)
        role5 = ctx.guild.get_role(726862277965512816)
        # Add the role
        await ctx.author.add_roles(role1, role2, role3, role4, role5)
        # Send the log msg
        log_channel = ctx.guild.get_channel(718214230658252851)
        embed = discord.Embed(
            title="Someone just verified!",
            description=f"**{ctx.author}** just verified!\n\nHis ID is: {ctx.author.id}\nHis name is: {ctx.author.name}\nHis discriminator is: {ctx.author.discriminator}\n\nThe message ID is: {ctx.message.id}\nThe channel ID is: {ctx.message.channel.id}\n\nMessage was sent at {datetime.utcnow()} UTC",
            color=self.color,
            timestamp=ctx.message.created_at
        )
        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 720012169567010836:
            if message.author.id != 735200954026033286: # The Bot ID
                await message.delete()
            else:
                return
        else:
            return

def setup(bot):
    bot.add_cog(allInOne(bot))
