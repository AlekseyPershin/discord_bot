import asyncio, json, random
from discord.ext import commands
from modules.dailik import dailik
from modules.reactions import Reactions
from modules.utilites import status


client = commands.Bot(command_prefix='!')

with open('information.json', 'r', encoding='utf-8') as f_obj:
    data = json.load(f_obj)
    token = data['token']
    main_channel_id = data['main_channel_id']
    # main_channel_id = 750112491450925220


client.add_cog(Reactions(client, main_channel_id)) #Добавление COG с реакциями на сообщения и др. действия

@client.event
async def on_ready():
    """Индикация подключения бота"""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(dailik(client, main_channel_id)) # Вызов на дейлик
client.loop.create_task(status(client)) # Смена статуса


client.run(token)