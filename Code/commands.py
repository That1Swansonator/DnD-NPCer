import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix = "!", intents=intents)

@client.command()
async def ping(ctx):
	await ctx.send('Pong!')