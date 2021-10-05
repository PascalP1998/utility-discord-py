import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
	print(f'--Logged in as {bot.user.name}--')

@bot.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(1000*bot.latency)}')
	
bot.run('token here!')