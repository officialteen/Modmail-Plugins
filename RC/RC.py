import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class RC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Fortnite Down    
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcf(self, ctx, member: discord.Member):
        fn_role = ctx.guild.get_role(641310880302104576)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(fn_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Fortnite recruit!",color = 0x06c9ff)
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
        text = "Enjoy your stay with Team Hope. we hope you enjoy!"
    )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)
        
    #Valorant Down    
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcv(self, ctx, member: discord.Member):
        v_role = ctx.guild.get_role(702607340867813476)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(v_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Valorant recruit!",color = 0x06c9ff)
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
        text = "Enjoy your stay with Team Hope. we hope you enjoy!"
    )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)
      
    #COD Down
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcc(self, ctx, member: discord.Member):
        c_role = ctx.guild.get_role(695379299292676117)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(c_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest COD recruit!",color = 0x06c9ff)
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
        text = "Enjoy your stay with Team Hope. we hope you enjoy!"
    )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)
        
    #Studios Down    
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rcs(self, ctx, member: discord.Member):
        s_role = ctx.guild.get_role(629986056606842880)
        hope_role = ctx.guild.get_role(614093090344402955)
        updates = self.bot.get_channel(662802293674082334)
        await member.add_roles(s_role)
        await member.add_roles(hope_role)
        embed = discord.Embed(description=f"Welcome {member.mention} as our newest Studios recruit!",color = 0x06c9ff)
        u = await updates.send(embed=embed)
        await u.add_reaction("🥳")
        await u.add_reaction("🔥")
        await u.add_reaction("😳")
        await u.add_reaction("💯")
        await u.add_reaction("🤩")
        embed = discord.Embed(
            title="Welcome to Team Hope",
            description=f"Welcome to Team Hope Studios Team, congratulations on getting recruited! Make sure to check out <#681985501737123997> to prevent being kicked from the team, this includes being professional and leaking things and much more, please check out the channel! Once you have been in Hope for a month, you may request free GFX from our GFX!",
            color=0x06c9ff,
        )
        embed.set_footer(
        text = "Enjoy your stay with Team Hope. we hope you enjoy!"
    )
        await member.send(embed=embed)
        embed = discord.Embed(
            title="Success",
            description=f"Successfully Recruited {member.mention}",
            color=0x06c9ff
        )
        await ctx.send(embed=embed)          

def setup(bot):
    bot.add_cog(RC(bot))
