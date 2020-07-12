#!/usr/bin/env python
import discord
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_ID')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')
MC_ADMIN_ROLE = os.getenv('DISCORD_ADMIN_ROLE_ID')

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
        await start_server(client, message)
    if('!stop' == message.content):
        await stop_server(client, message)

async def is_admin(client, author):
    #get guild by id
    guild = client.get_guild(int(GUILD))
    #get mc admin role from discord api
    role = guild.get_role(int(MC_ADMIN_ROLE))
    #get members for mc admin role
    mc_admins = role.members
    #check if message author is in list of admins
    return (author in mc_admins)

async def start_server(client, message):
    #check if message author is in list of admins
    if(await is_admin(client, message.author)):
        #if yes, start server
        await message.channel.send('weh would start server')
    else:
        await message.channel.send('you are not an admin, weh')

async def stop_server(client, message):
    #check if message author is in list of admins
    if(await is_admin(client, message.author)):
        #if yes, stop server
        await message.channel.send('weh would stop server')
    else:
        await message.channel.send('you are not an admin, weh')

client.run(TOKEN)
