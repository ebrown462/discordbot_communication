import discord
from discord.ext import commands, tasks

ID = "YOU ID HERE"
token = "YOUR TOKEN HERE"
intents = discord.Intents.all()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Bot Started")

@client.event
async def on_message(message):
    testData = 'INSERT SECRET DATA HERE'
    if message.author.id == 708824298177167481 and message.content.startswith('TRANSFER PROTOCOL'):
        await message.channel.send(testData)
    await client.process_commands(message)

client.run(token)