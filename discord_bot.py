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

client.run(TOKEN)
