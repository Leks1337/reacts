import discord
import asyncio
from discord.ext import commands


#COMMAND PREFIX HERE XD
bot = commands.Bot(command_prefix = 'COMMAND PREFIX HERE')

@bot.event
async def on_ready():
	print('Bot Launched')
	###PLAYING GAME
	await bot.change_presence(game=discord.Game(name='TEXT HERE', type=0))
	###STREAMING
	#await bot.change_presence(game=discord.Game(name='TEXT HERE', type=1, url='LINK HERE'))
	###LISTENING TO
	#await bot.change_presence(game=discord.Game(name='TEXT HERE', type=2))
	###WATCHING
	#await bot.change_presence(game=discord.Game(name='TEXT HERE', type=3))
	
	print('Servers connected')
	print('')
	print('')
	print('')
	for server in bot.servers:
		print(server.name)
		
##############################################
#                   REACTS                   #
##############################################
# To find your ID enable developer mode in discord at Settings > Appearance > Advanced and Enable Developer Mode
# Then right click user in chat and press copy ID https://i.imgur.com/Ix1VkWG.png
# To find Emoji ID find an emoji, for example :fire: and in chat type \:fire: with the "\" in front of it https://i.imgur.com/YZ0py9M.png
# It will post the emoji and then just copy it to Emoji ID.
# If it's a custom emoji, do the same and it will give you a code. copy what's in between the "< >", for example a:mlem:515351832655036416
# To add more users/ID's, just copy and paste the code below.
@bot.event
async def on_message(message):

	if message.author.id == 'USER ID':
		await bot.add_reaction(message,'EMOJI ID')
	
##############################################
#                DO NOT DELETE               #
##############################################

	await bot.process_commands(message)


#############################################
#                BOT TOKEN                  #
#############################################
# To find bot token follow this well-written guide: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord
bot.run('BOT TOKEN HERE')



