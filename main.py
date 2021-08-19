import discord
import random
import time
import sys
import re
import os
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
from discord import User
from datetime import datetime
from time import gmtime, strftime
import asyncio
import datetime

bot = commands.Bot(command_prefix="`")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Colour.blue())
    embed.set_author(name = 'Help')
    await ctx.send(author, embed=embed)

@bot.command(pass_context=True)
async def date(ctx):
   await ctx.send(time.time())

@bot.command(pass_context=True)
async def remind(ctx, message):
    embed = discord.Embed(title="New Reminder!",description=("Hello"),color=discord.Color.dark_teal())
    await ctx.send(embed=embed)

bot.run("ODc3NzA2ODI4MzU0NTU1OTc0.YR2iLg.f73m8XO31jvxsxZFpurIsE9Y8NQ")
