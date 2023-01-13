import discord
import os
# import read_table as tab
from dotenv import load_dotenv

# initialization Code
# imports the Token from the TOKEN.env file (not included in the GitHub Repository)
load_dotenv()
token = os.getenv('TOKEN')

# Initializes the Intents function with all intents and sets the command prefix
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


@client.event
async def on_ready():
	print("Logged in as a bot {0.user}".format(client))


# Bot Response Code
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('hi'):
		await message.channel.send('Hello!')


# Runs Code
client.run(token)