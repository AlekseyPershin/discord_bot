import discord, datetime, asyncio

async def status(client):
    """Установка статуса бота"""
    await client.wait_until_ready()
    while not client.is_closed():
        cur_time = datetime.datetime.today().minute
        if cur_time > 6 and cur_time < 21: #время с учетом +3 ко времени сервака
            await client.change_presence(status=discord.Status.online)
        else:
            await client.change_presence(status=discord.Status.idle)
        await asyncio.sleep(60)
