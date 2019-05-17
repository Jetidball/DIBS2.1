import discord
from discord.ext import commands
import SoundEffect
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

class FFXIV:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ListCommands(self, ctx):
        ret = "quillboar, hostiles, yoshi, ohyeah, selfie, highnoon %d" % self.getFileCount(".txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'Level Down.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def ohyeah(self, ctx):
        ret = " %d" % self.getFileCount(".txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'ohyeah.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def selfie(self, ctx):
        ret = " %d" % self.getFileCount(".txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'lemmetakeaselfie.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def highnoon(self, ctx):
        #player = await asyncio.sleep(1)
        #voice = player.create_ffmpeg_player('its-high-noon.mp3')
        #voice.start()
        #while voice.is_playing():
        #    await asyncio.sleep(1)
        try:
           await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'its-high-noon.mp3')
        except AttributeError:
           print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def play(self, ctx, file):
        server = ctx.message.author.voice_channel
        voice_client = self.bot.voice_client_in(server)
        player = await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'its-high-noon.mp3')
        players[server.id] = player
        player.start()
    @commands.command(pass_context=True)
    async def voice(self, ctx):
        discord.play('its-high-noon.mp3', after=None)
        #try:
          # await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'its-high-noon.mp3')
        #except AttributeError:
           #print("Error: Failed in voice callback")
    @commands.command(pass_context=True)
    async def leeroy(self, ctx):
        ret = " %d" % self.getFileCount(".txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'Leeroyjenkis.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def quillboar(self, ctx):
        ret = " %d" % self.getFileCount(".txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'quillboar.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def hostiles(self, ctx):
        ret = " %d" % self.getFileCount("punCount.txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'the-division-isac-alert-hostiles.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def xanthe(self, ctx):
        ret = "Xanthe and his crazy puns are now at: %d" % self.getFileCount("punCount.txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'Level Down.mp3')
        except AttributeError:
            print("Error: Failed in xanthe callback")
    @commands.command(pass_context=True)
    async def yoshi(self, ctx):
        ret = "Yoshi has Creeped %d times now!" % self.getFileCount("meditationCount.txt")
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'creepybingha.mp3')
        except AttributeError:
            print("Error: Failed in pam callback")
    @commands.command(pass_context=True)
    async def steam(self, ctx):
        ret = "%d"
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'steam_notification.mp3')
        except AttributeError:
            print("Error: Failed in pam callback")
    # @commands.command(pass_context=True)
    # async def join(self, ctx):
    #     #if join.content.startswith($join):
    #     author = ctx.message.author
    #     channel = author.voice_channel
    #     if self.bot.author.voice_channel(channel) == ctx.message.author.voice_channel:
    #         self.bot.join_voice_channel(channel)
    #         await ctx.message.author.join_voice_channel('$leave')
    #    else if self.bot.voice_channel(channel) = author.voice_channel:
    #        self.bot.join_voice_channel(channel)
    @commands.command(pass_context=True)
    async def join(self, ctx):
            author = ctx.message.author
            channel = author.voice_channel
            joinvoice = self.bot.join_voice_channel
            timeout=1.0
            try:
                await client.wait_for(joinvoice, timeout)
            except asyncio.TimeoutError:
                await ctx.author.channel.send('bye')


            #def check(m):
            #    return m.content == '$leave' and m.channel == channel
            #    try:
            ##    except asyncio.TimeoutError:
            #        await channel.send('👎')
            #        msg = await client.wait_for('message', check=check)
            #        await

        #else if join.content.
        #else if join.content.('$leave'):
        #    author = ctx.message.author
        #    channel = author.voice_channel
        #    break


        #except
        #except AttributeError:
        #print("Error: Failed to join channel")
        #print(ctx.message.author.voice_channel, author)
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        #try:
        author = ctx.message.author
        channel = author.voice_channel
        await self.bot.leave(channel)
        #except AttributeError:
        #print("Error: Failed to join channel")
        print(ctx.message.author.voice_channel, author)
    @commands.command(pass_context=True)
    async def sounds(self, ctx):
        ret = "$yoshi, $xanthe, $hostiles, $quillboar, $highnoon, $leeroy, $selfie, $ohyeah"
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'creepybingha.mp3')
        except AttributeError:
            print("Error: Failed in pam callback")
    @commands.command(pass_context=True)
    async def commands(self, ctx):
        ret = "$yoshi, $xanthe, $hostiles, $quillboar, $highnoon, $leeroy, $selfie, $ohyeah"
        await self.bot.say(ret)
        try:
            await SoundEffect.playEffect(self.bot, ctx.message.author.voice_channel, 'creepybingha.mp3')
        except AttributeError:
            print("Error: Failed in pam callback")

    def getFileCount(self, filename):
        try:
            file = open(filename, "r+")
            value = int(file.readline())
            value += 1
            file.seek(0)
        except FileNotFoundError:
            file = open(filename, "a+")
            value = 1
        file.write(str(value))
        file.close()
        return value
