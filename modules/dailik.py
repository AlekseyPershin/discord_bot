import asyncio, datetime, pathlib

async def dailik(client, main_channel_id):
    await client.wait_until_ready()
    channel = client.get_channel(main_channel_id) # Чат для отправки

    while not client.is_closed():
        d = datetime.datetime.isoweekday(datetime.datetime.today())
        h = datetime.datetime.today().time().hour
        m = datetime.datetime.today().time().minute
        if d < 6:
            if h == 14 and m == 58:
                await channel.send(f'@everyone ДЕЙЛИК!!!')
                await asyncio.sleep(60)
            else:
                log_file = pathlib.Path(__file__).parent.parent.joinpath('txt').joinpath('log.txt')
                with log_file.open('a') as f_obj:
                    f_obj.write(str(datetime.datetime.today().time()) + '\n')
                await asyncio.sleep(60)
        else:
            await asyncio.sleep(18000)


# Локальное время на серваке на 3 часа отстает - это надо учитывать
