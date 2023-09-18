from discord.ext import commands
import discord
BOT_TOKEN = "MTE1MzM2MDY2NzAxMzgxNjQ1MA.G63cGU.owf1bGvzf3ia7Nu0330AC7OFi2q5qcXCNPE0PU"
CHANNEL_ID = "951770614610407474"

# client = commands.Bot(command_prefix='/',intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print("Hello Bruh")
#     channel = bot.get_channel(CHANNEL_ID)
#     await channel.send("Hello Bruh")

# bot.run(BOT_TOKEN)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='-', help_command=None, intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
@client.command(name="test")
async def test(ctx, arg):
    await ctx.send(arg)

client.run(BOT_TOKEN)