import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content == '!ping':
        await message.channel.send('Pong!')

    elif message.content == '!hello':
        await message.channel.send('Hello, world!')

    elif message.content == '!bye':
        await message.channel.send('Goodbye!')

    if any(word in message.content.lower() for word in ['goblok', 'begok', 'anjing', 'babi']):
        await message.delete()
        await message.channel.send(f'Pesan dari {message.author} mengandung kata yang tidak pantas dan telah dihapus.')

client.run('your_discord_bot_token')