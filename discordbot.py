import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}'
    )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {member.guild}!' 
    )

@bot.command(name='avocado', help = "Avocado")
async def avocado(message, number: int):
    await message.channel.send(f"Hello, {message.author}")
    avocado_types = ["Tomato", "Tomahto", "Potato", "Potahto",]

    for i in range(number):
        response = random.choice(avocado_types)
        await message.channel.send(response)

@bot.command(name='createchannel', help='Create a Channel (admins only)')
@commands.has_role('admin')
async def createchannel(message, channel_name: str):
    guild = message.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name)
    if not existing_channel:
        await message.channel.send(f'Creating new channel: {channel_name}')
        await guild.create_text_channel(channel_name)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')




bot.run(TOKEN)