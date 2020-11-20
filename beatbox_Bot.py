import discord
import youtube_dl
from discord.ext import commands

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

### Message content start with $hello
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('')

client.run('')
