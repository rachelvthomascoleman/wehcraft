#!/usr/bin/env python
import boto3
import discord
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_ID')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')
MC_ADMIN_ROLE = os.getenv('DISCORD_ADMIN_ROLE_ID')
MINECRAFT_INSTANCE_ID = os.getenv('MINECRAFT_INSTANCE_ID')
REGION = os.getenv('AWS_REGION')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

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
        
        #make an ec2 client
        ec2 = boto3.client('ec2', region_name = REGION)

        #get the JSON response from starting the minecraft instance
        response = ec2.start_instances(
            InstanceIds = [MINECRAFT_INSTANCE_ID]
        )

        #get the status of the instance from the response
        #resopnse structure:
        #{
        #   'StartingInstances': [
        #        {
        #            'CurrentState': {
        #                'Code': 123,
        #                'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
        #            },
        #            'InstanceId': 'string',
        #            'PreviousState': {
        #                'Code': 123,
        #                'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
        #            }
        #        },
        #    ]
        #}
        status = response['StartingInstances'][0]['CurrentState']['Name']

        await message.channel.send(f'new server status: {status}, weh')
    else:
        await message.channel.send('you are not an admin, weh')

async def stop_server(client, message):
    #check if message author is in list of admins
    if(await is_admin(client, message.author)):
        #if yes, stop server
        
        #make an ec2 client
        ec2 = boto3.client('ec2', region_name = REGION)

        #get the JSON response from stopping the minecraft instance
        response = ec2.stop_instances(
            InstanceIds = [MINECRAFT_INSTANCE_ID]
        )

        #get the status of the instance from the response
        #resopnse structure:
        #{
        #   'StoppingInstances': [
        #        {
        #            'CurrentState': {
        #                'Code': 123,
        #                'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
        #            },
        #            'InstanceId': 'string',
        #            'PreviousState': {
        #                'Code': 123,
        #                'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
        #            }
        #        },
        #    ]
        #}
        status = response['StoppingInstances'][0]['CurrentState']['Name']

        await message.channel.send(f'new server status: {status}, weh')
    else:
        await message.channel.send('you are not an admin, weh')

client.run(TOKEN)
