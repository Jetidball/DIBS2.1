import asyncio
import discord

async def playEffect(client, channel, file):

    voice = client.join_voice_channel(channel)

    while await client.join_voice_channel(channel):
        player = voice.create_ffmpeg_player(file)
        player.start()
        while player.is_playing():
            await asyncio.sleep(1)
            print('completed returning1')
        return
    #except:
    #    await print('completed returning2')
    #    return
