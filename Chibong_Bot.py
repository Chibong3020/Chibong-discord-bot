import discord
import random

client = discord.Client()

token = "OTY3OTYzMzI2ODg3OTA3NDM4.YmX8GQ.sfbcySMyuwrSWsch0bKWpSxNa80"

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('cb!hello'):
        await message.channel.send('Hello from the other side!!!')
    
    if message.content.startswith('cb!meme'):
        with open('meme_list.txt', 'r') as f:
            memes = f.readlines()
        memes = random.choice(memes)[:-1]
        await message.channel.send(memes)

client.run(token)