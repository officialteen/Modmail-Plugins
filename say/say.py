@commands.command()
async def say(self,ctx,* ,message):
    """Make the bot say something"""
    msg = escape(message,mass_mentions=True)
    await ctx.send(msg)
