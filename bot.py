# Work with Python 3.6
import discord
import events

TOKEN = 'NzE1MzA2NzQ4NjQyMTk3NTU0.Xt0Rhw.ZpwYUbZVNvrZAfM9XbZyn7jzlrg'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    await events.on_message(message)
   

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN) 
