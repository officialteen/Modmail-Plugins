import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class RC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Fortnite Down
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcf(self, ctx, member: discord.Member):
        fn_role = ctx.guild.get_role(641310880302104576)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(fn_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Fortnite recruit!", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title="Welcome to Team Hope",
            description=f"Welcome to Team Hope Fortnite, congratulations on getting recruited! Make sure to check out<#681985501737123997> to prevent being kicked from the team, this includes being professional and leaking things and much more, please check out the channel! Once you have been in Hope for a month, you may request free GFX from our GFX!",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. we hope you enjoy!"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # Valorant Down
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcv(self, ctx, member: discord.Member):
        v_role = ctx.guild.get_role(702607340867813476)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(v_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Valorant recruit!", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title="Welcome to Team Hope",
            description=f"Welcome to Team Hope Valorant, congratulations on getting recruited! Make sure to check out <#681985501737123997> to prevent being kicked from the team, this includes being professional and leaking things and much more, please check out the channel! Once you have been in Hope for a month, you may request free GFX from our GFX!",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. we hope you enjoy!"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # COD Down
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcc(self, ctx, member: discord.Member):
        c_role = ctx.guild.get_role(695379299292676117)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(c_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest COD recruit!", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title="Welcome to Team Hope",
            description=f"Welcome to Team Hope COD, congratulations on getting recruited! Make sure to check out <#681985501737123997> to prevent being kicked from the team, this includes being professional and leaking things and much more, please check out the channel! Once you have been in Hope for a month, you may request free GFX from our GFX!",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. we hope you enjoy!"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # Studios Down
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcs(self, ctx, member: discord.Member):
        s_role = ctx.guild.get_role(629986056606842880)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(s_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Studios recruit!", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title="Welcome to Team Hope",
            description=f"Welcome to Team Hope Studios Team, congratulations on getting recruited! Make sure to check out <#681985501737123997> to prevent being kicked from the team, this includes being professional and leaking things and much more, please check out <#617115135340707879> if you are a GFX, this is where people can ask for GFX! Don't worry, after 1 month we pay you, so please do not ask them for money.",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. we hope you enjoy!"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # TM Down
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rctm(self, ctx, member: discord.Member):
        tm_role = ctx.guild.get_role(640662157079609364)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(tm_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Trial Moderator!", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title=f"**Welcome to Team Hope as a TRIAL MANAGER**",
            description=f"Congratulations, you have been accepted into Team Hope as a Trial Moderator!\nHere are the things you need to know:\n\n*If you would like to warn someone, type +warn (user)\n*You can delete other member's messages. (The same way you delete your own)\n*You now have access to <#594810585154191400>, if you have any enquires or concerns, let us know there.\n*You can now add reactions to other people's messages.",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. We hope you enjoy!"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # Discord Managers DOWN
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcdm(self, ctx, member: discord.Member):
        dm_role = ctx.guild.get_role(696778139900313710)
        m_role = ctx.guild.get_role(674329845920038952)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(dm_role)
        await member.add_roles(m_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Discord Manager!", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title=f"**Welcome to Team Hope as a DISCORD MANAGER**",
            description=f"Congratulations, you have been accepted into Team Hope as a Discord Manager!\nHere are the things you need to know:\n\n*You can now view audit log.\n*You can use `+warn (@user)` `+mute (@user)` `+tempmute (@user)` `+kick (@user)` and `+ban (@user)`. \n*You can @everyone, @here, etc. \n*You can now drag, mute, and deafen other people in voice calls.\nAny abuse of these permissions will result in a **RED STRIKE** or a **DEMOTION** depending on the situation, so please use these responsibly!\n\nPlease remember, your job is to keep our discord running smoothly. You can lock <#664213577770729473> by using `%lock #😳general-chat (time)`.\nIf you wish to know other useful commands, please let us know in <#594810585154191400>. ",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. We hope you enjoy!"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # Leave Good Terms DOWN
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def lg(self, ctx, member: discord.Member):
        h_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.remove_roles(h_role)
        embed = discord.Embed(description=f"{member.mention} has left the team on good terms", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("<a:sadgun:717453885949608006>")
        await u.add_reaction("<a:711587415042686986:717453742416461905>")
        await u.add_reaction("<:glass_cry:717453760095453226>")
        await u.add_reaction("<a:sad:717359038710415410>")
        await u.add_reaction("😢")
        embed = discord.Embed(
            title=f"**Goodbye**",
            description=f"We hope you had a really great time in Team Hope, and we are very sad to see you go.\n\nWe hope you have a good time in the future!",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="- Team Hope",
            icon_url="https://cdn.discordapp.com/attachments/639774534639288330/717363151250915369/logo_no_outline.png"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            description="Done",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

    # GENERAL Managers DOWN
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcgm(self, ctx, member: discord.Member):
        gm_role = ctx.guild.get_role(696778139900313710)
        m_role = ctx.guild.get_role(674329845920038952)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(gm_role)
        await member.add_roles(m_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest General Manager", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title=f"**Welcome to Team Hope as a GENERAL MANAGER**",
            description=f"Congratulations, you have been accepted into Team Hope as a General Manager!\nHere are the things you need to know:\n\n*Whenever you are available, we may ask you to gather content/collect VFX/GFX. \n*You have access to <#594810585154191400>, so if you require assistance, please tag us there.\nAny abuse of these permissions will result in a **RED STRIKE** or a **DEMOTION** depending on the situation, so please use these responsibly!\n\nPlease remember, your job is practically helping us; however, we too want to help you! If you have any enquires, make sure to check out <#594810585154191400>!",
            color=0x06c9ff,
        )
        embed.set_footer(
            text="Enjoy your stay with Team Hope. We hope you enjoy!",
            icon_url = "https://cdn.discordapp.com/attachments/639774534639288330/717363151250915369/logo_no_outline.png"
        )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)
        
    # Leave Bad Terms DOWN
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def lb(self, ctx, member: discord.Member):
        await ctx.message.delete()
        h_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.remove_roles(h_role)
        embed = discord.Embed(description=f"{member.mention} has left the team", color=0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("<a:sadgun:717453885949608006>")
        await u.add_reaction("<a:711587415042686986:717453742416461905>")
        await u.add_reaction("<:glass_cry:717453760095453226>")
        await u.add_reaction("<a:sad:717359038710415410>")
        await u.add_reaction("😢")
        embed = discord.Embed(
            description="Done",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(RC(bot))
