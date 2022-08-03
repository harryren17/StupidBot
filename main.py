#basic bot setup/ starter code 
import discord
import random
from discord.ext import commands
from discord import FFmpegPCMAudio
from os import environ
from dotenv import load_dotenv
import youtube_dl
import os

import helper

load_dotenv()
TOKEN = environ["TOKEN"]
client = commands.Bot(command_prefix = '!')

#initialize
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#command message reply
@client.command()
async def test(ctx):
    await ctx.send("akl;sujhfglaiserughl;asirugh")

@client.command()
async def shitpost(ctx):
    await ctx.send(helper.getImageLink())
    await ctx.send(helper.getRandomCaption()) 

#join VC
@client.command(pass_context = True)
async def join(ctx):
    #if user in VC, join same VC
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("join a vc dumb bitch, idk where to go")

#leave VC
@client.command(pass_context = True)
async def leave(ctx):
    #if bot in VC already, disconnect
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("im out bitch")
    else:
        await ctx.send("i aint here hoe")

#play VC fixed
@client.command(pass_context = True)
async def play(ctx, url:str):
    song_exist = os.path.isfile("song.mp3")
    try:
        if song_exist:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("error 1")
        return
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild =ctx.guild)

        #download the vid

    ydl_opts = {
        'format':'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
        


#message replys (no command)
@client.event
async def on_message(message):
    #debugging
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username},{user_message},{channel}')
    
    #stops bot replys to self
    if message.author == client.user:
        return

    #only testing channel
    #if message.channel.name == 'testing':
    if random.random() > 0.99:
        await message.channel.send(helper.getImageLink())
        await message.channel.send(helper.getRandomCaption()) 
    elif user_message == 'balls':
        await message.channel.send('i lick it')
        return
    await client.process_commands(message)



if __name__== "__main__" :
    client.run(TOKEN)
