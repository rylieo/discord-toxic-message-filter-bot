import discord

# Setup intents untuk mendapatkan akses ke pesan
intents = discord.Intents.default()
intents.message_content = True  # Untuk mengakses konten pesan

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is online as {client.user}')

@client.event
async def on_message(message):
    # Menghindari bot membalas pesannya sendiri
    if message.author == client.user:
        return 

    # Perintah !ping
    if message.content == '!ping':
        await message.channel.send('Pong!')

    # Perintah !hello
    elif message.content == '!hello':
        await message.channel.send('Hello, world!')

    # Perintah tambahan lainnya
    elif message.content == '!bye':
        await message.channel.send('Goodbye!')

    # Perintah tambahan lainnya
    elif message.content == '!siapa yang paling jelek':
        await message.channel.send('tegar, erik, dan rafka!')

    # Perintah tambahan lainnya
    elif message.content == '!siapa yang paling ganteng':
        await message.channel.send('ga ada yang ganteng disini!')

    # Menambahkan pengecekan untuk kata 'yatim', 'piatu', atau 'kontol' dan menghapus pesan jika ditemukan
    if any(word in message.content.lower() for word in ['yatim', 'piatu']):
        await message.delete()
        await message.channel.send(f'Pesan dari {message.author} mengandung kata yang tidak pantas dan telah dihapus.')

# Jalankan bot menggunakan token yang sudah kamu salin dari Discord Developer Portal
client.run('your_discord_bot_token')