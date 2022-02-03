import discord
from ossapi import *
from minesweeper import minesweeper
api = OssapiV2("your stuff goes there")

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
	
	async def on_message(self, message):
		channel = message.channel
		if message.content.startswith("&help"):
			await channel.send("help page")
		
		elif message.content.startswith("&playstyle"):
			username = message.content.replace("&playstyle ", "")
			username = username.replace(" ", "%20")
			playstyle = str(api.user(username).playstyle).replace("PlayStyles.", "")
			formatted = playstyle.split("|")
			if len(formatted) == 1:
				await channel.send("This user is playing with {}".format(formatted[0].lower()))
			elif len(formatted) == 2:
				await channel.send("This user is playing with {} and {}".format(formatted[0].lower(), formatted[1].lower()))
			else:
				await channel.send("This user is playing with {}, {} and {}".format(formatted[0].lower(), formatted[1].lower(), formatted[2].lower()))
	
		elif message.content.startswith("&minesweeper"):
			await minesweeper(self, message)
		
			
client = MyClient()
client.run('token here')
