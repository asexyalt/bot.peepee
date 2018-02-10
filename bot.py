import discord  
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot=commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
    print ("My nickname is " + bot.user.name)
    print("my ID is: " + bot.user.id)
    print ("I'm ready to get cori to succ your peepee cheezy")
	
	
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong! :ping_pong:")
	
	
	
	
	
	
bot.run("")