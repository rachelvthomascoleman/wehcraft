#!/usr/bin/env python
import discord
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_ID')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #get the weh guild
    guild = client.get_guild(int(GUILD))
    #get the bot testing channel
    channel = guild.get_channel(int(CHANNEL))
    #send message to the channel
    await channel.send('weh')

@client.event
async def on_message(message):
    if(message.author.bot):
        return
    if('weh' in message.content.lower()):
        await message.channel.send('weh')
    if('!start' == message.content):
        await start_server(message)
    if('!stop' == message.content):
        await stop_server(message)

async def start_server(message):
    await message.channel.send('weh would start server')

async def stop_server(message):
    await message.channel.send('weh would stop server')

client.run(TOKEN)
