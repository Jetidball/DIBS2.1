import asyncio
import discord

class SoundVoice:
    async def playEffect(ctx, file):
        try:
            if not client.is_voice_connected(ctx.message.server):
                voice = await client.join_voice_channel(ctx.message.author.voice_channel)
            else:
                voice = client.voice_client_in(ctx.message.server)
        
            player = await voice.create_ytdl_player(url, after=toggle_next)
            await songs.put(player)
        
            client.loop.create_task(audio_player_task())
        except:
            return
        
        player = voice.create_ffmpeg_player(file)
        player.start()
        if player.is_playing():
            await asyncio.sleep(5)
        await voice.disconnect() 

