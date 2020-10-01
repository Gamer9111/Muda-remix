#Dependencies/Modules (whatever you like to call them i call them modules) START
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio 
#Deps/Modules END

#Variables START
bot = discord.Client()
prefix = commands.Bot(command_prefix = "?")
botversion = "vBETA-4 GithubRelease"
botid = "491724307378995219"
owner = "Alej0hio"
botinfo = discord.AppInfo
error = bot.on_error()
#Variables END

#Events START
@bot.event
async def on_ready():
    print ("MY BOT IS READY")
    print (botid)
    print ("Muda")

@bot.event
async def on_message(message):
    if message.content.upper().startswith('?test'):
        await bot.send_message("whoa! it works" + bot.ping)
    if message.content.upper().startswith('?bruh'):
        await bot.send_message("test")
    if message.content.upper().startswith('React'):
        mesID = message.id
        await bot.add_reaction(message, "👍")
        await bot.add_reaction(message, "👎")
        await bot.add_reaction(message, "🤷")
#Events END



#most important part 
bot.run("TOKEN")
