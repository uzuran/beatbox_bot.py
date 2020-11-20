import os
import random
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
        await message.channel.send('Hello! Check this out : https://www.facebook.com/czechbeatboxcommunity/ ')
### random bot answer
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'Beatbox 💯 cool!!','Trénuj chlapče.','Možná ti to ukáže Shoter :robot:',
        'Jooooo!!Tak to byla šupa.',
        (
            'Cože?Jak jsi to udělal? bumck cack clack crack?'
            'Není to tak špatný no.Slyšel jsem že DeepLow to umí lépe.'
        ),
    ]

    if message.content == 'beatbox' or 'Beatbox':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run('')
