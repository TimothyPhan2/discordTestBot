from discord.ext import commands
import discord
BOT_TOKEN = "TOKEN"


# client = commands.Bot(command_prefix='/',intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print("Hello Bruh")
#     channel = bot.get_channel(CHANNEL_ID)
#     await channel.send("Hello Bruh")

# bot.run(BOT_TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("hello"):
        await message.channel.send("Hi! Welcome to the server!")
    await client.process_commands(message)

@client.command()
async def test(ctx, *args):
    arguments = " ".join(args)
    await ctx.send(arguments)

@client.command()
async def video(ctx):
    await ctx.send("https://www.youtube.com/watch?v=XJeN6Slkk_Q")

client.run(BOT_TOKEN)