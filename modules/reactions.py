import random, asyncio, pathlib
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
                await asyncio.sleep(10) # Сообщение отправляется через 10 секунд после появления в шоуруме
                main_channel = self.client.get_channel(self.main_channel_id) # Канал
                file = pathlib.Path(__file__).parent.parent.joinpath('txt').joinpath('showroom_reactions.txt')
                with file.open('r', encoding='utf-8') as f_obj:
                    data = f_obj.readlines()
                    say = random.choice(data) # Случайная фраза из txt/showroom_reactions.txt
                    if '@name' in say:
                        say = say.replace('@name', ctx.author.mention)
                    message = ctx.content # Сообщение автора
                    await main_channel.send(f'{ctx.jump_url} \n >{message}\n {say} {ctx.attachments[0].url}')
