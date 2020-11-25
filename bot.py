import asyncio, json, random, re, os, pathlib
from discord.ext import commands
import modules.dailik, modules.comands, modules.reactions, modules.utilites


client = commands.Bot(command_prefix='!')

info_file = os.path.normpath(os.path.dirname(__file__)) + os.sep + 'information.json'
info_file = pathlib.Path(__file__).parent.joinpath('information.json')
with info_file.open('r', encoding='utf-8') as f_obj:
    data = json.load(f_obj)
    token = data['token']
    main_channel_id = data['main_channel_id']
    # main_channel_id = 750112491450925220 # Канал для теста


client.add_cog(modules.reactions.Reactions(client, main_channel_id)) #Добавление COG с реакциями на сообщения и др. действия
client.add_cog(modules.comands.Comands(client, main_channel_id))

@client.event
async def on_ready():
    """Индикация подключения бота"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(modules.dailik.dailik(client, main_channel_id)) # Вызов на дейлик
client.loop.create_task(modules.utilites.status(client)) # Смена статуса


client.run(token)