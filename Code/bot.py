import discord
import os
import random as rand
import read_table as tab
from dotenv import load_dotenv

#initialization Code
#imports the Token from the TOKEN.env file (not included in the GitHub Repository)
load_dotenv()
token = os.getenv('TOKEN')

#Intializes the Intents function and disables discord features such as "<user> is typing" for performance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print("Logged in as a bot {0.user}".format(client))

#client.run(token)

#Bot Response Code
@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.author.name)
	user_message = str(message.content)
	print(f'Message {user_message} by {username} on {channel}')

	if message.author == client.user:
		return

	if channel == "random":
		if message.author.lower() == "hello" or message.author.lower() == 'hi':
			await message.channel.send(f'Hello {username}')
			return
		
		elif user_message.lower() == "bye":
			await message.channel.send(f'Bye {username}')

		elif user_message.lower() == "tell me a joke":
			jokes = [" Can someone please shed more light on how my lamp got stolen?", 
					 "Why is she called llene? She stands on equal legs.","What do you call a gazelle in a lions territory? Denzel."]
			await message.channel.send(rand.choices(jokes))

client.run(token)