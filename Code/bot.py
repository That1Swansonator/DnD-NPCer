import discord
import os
import read_table as tab
import random as rand
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

	if message.content.startswith('!hi'):
		await message.channel.send('Hello!')

	if message.content.startswith('!encounter wildeness'):
		out_tab = tab.wild_combat()
		await message.channel.send(out_tab)

	if message.content.startswith('!dice'):  # Format: !dice dn q where n = n sided dice and q = How many times to roll
		command = str(message.content)
		dice = tab.roll_dice(command)
		await message.channel.send(dice)
# Runs Code
client.run(token)