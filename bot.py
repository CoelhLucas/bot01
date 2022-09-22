import discord
import os
from datetime import datetime

client = discord.Client()
today = datetime.today()
msg = str(today) + " Hello"
# print(today)

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(msg)

async def create_channel(ctx, channel_name):
	guild = ctx.guild
	channel = await guild.create_text_channel(channel_name)


client.run('c7b1a43278960182992e6a328a19064b7b811e772ec1f8d23344c9cafb661bf4')