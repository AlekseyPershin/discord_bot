import random, asyncio, os, pathlib
from discord.ext import commands

class Reactions(commands.Cog):
    """COG со всеми методами-реакциями на различные действия"""
    def __init__(self, client, main_channel_id):
        self.client = client
        self.main_channel_id = main_channel_id


    @commands.Cog.listener()
    async def on_message(self, ctx):
        """Реакция на пост в showroom"""
        if ctx.channel.name == 'showroom':
            if len(ctx.attachments) > 0:
                await asyncio.sleep(10)
                main_channel = self.client.get_channel(self.main_channel_id) # Канал
                file = pathlib.Path(__file__).parent.parent.joinpath('txt').joinpath('showroom_reactions.txt')
                with file.open('r', encoding='utf-8') as f_obj:
                    data = f_obj.readlines()
                    say = random.choice(data)
                    if '@name' in say:
                        say = say.replace('@name', ctx.author.mention)
                    await main_channel.send(f'{ctx.jump_url} \n {say} \n {ctx.attachments[0].url}')
