#basic bot setup/ starter code
import discord
import random
from discord.ext import commands
from os import environ
from dotenv import load_dotenv

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
    if user_message == 'cum':
        await message.channel.send('i love it')
        return
    elif user_message == 'balls':
        await message.channel.send('i lick it')
        return
    elif user_message == 'am i hot':
        await message.channel.send('yes bb<3')
        return
    await client.process_commands(message)



if __name__== "__main__" :
    client.run(TOKEN)
