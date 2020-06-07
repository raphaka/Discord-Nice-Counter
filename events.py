from discord import Message

async def on_message(msg: Message):
    keywords = ['nice', 'crap', 'fuck']
    if msg.content in keywords:
        await msg.channel.send(msg.author.display_name + " wrote " + msg.content)
