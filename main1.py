from bot_logic import *
import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.isdigit():
        await message.channel.send(gen_pass(int(message.content)))
    elif message.content.startswith('$flip_coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$gen_emodji'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run("MTE1MjYwMDQzMDEyNDIxMjI0NA.GQrjCi.gY5mr5ViW-65aYTHvU-p0ruYR5kDWj6k4t9ptA")
