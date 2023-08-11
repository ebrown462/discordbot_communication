# This script runs a discord bot that transfers a line of text (or other variable) to another PC running a different discord bot.

import discord
from discord.ext import commands, tasks

# ID and token
ID = "YOU ID HERE"
token = "YOUR TOKEN HERE"

# As of discord.py 2.3.2 you need to enable indents
intents = discord.Intents.all()
intents.members = True
intents.presences = True

# Sets prefix to ! (this has to be different from whatever the other bot is using)
client = commands.Bot(command_prefix='!', intents=intents)

# Startup text
@client.event
async def on_ready():
    print("Bot Started")


@client.event
async def on_message(message):
    testData = 'INSERT SECRET DATA HERE'
    if message.author.id == "OTHER BOT'S ID" and message.content.startswith('TRANSFER PROTOCOL'):
        await message.channel.send(testData)
    await client.process_commands(message)

client.run(token)
