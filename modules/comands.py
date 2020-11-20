import re
from discord.ext import commands

class Comands(commands.Cog):
    """COG командами"""
    def __init__(self, client, main_channel_id):
        self.client = client
        self.main_channel_id = main_channel_id

    @commands.command()
    async def say(self, ctx):
        await ctx.channel.purge(limit=1)
        s = ctx.message.content
        s = s.replace('!say', '')
        s = re.sub(r'\\<@', '<@!', s)
        await ctx.channel.send(s)


