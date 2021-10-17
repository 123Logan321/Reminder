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
    embed = discord.Embed(title="Help", description=(
        "This is a Reminder Bot\nCreate reminds in the format of (24h Format):\n`remind 'name' Year/Month/Day Hour:Minute"), color=discord.Colour.blue())
    await ctx.send(author, embed=embed)


@bot.command(pass_context=True)
async def date(ctx):
    await ctx.send(time.time())


@bot.command(pass_context=True)
async def remind(ctx, message, date, time):
    author = ctx.message.author
    date = date.split("/")
    time = time.split(":")
    embed = discord.Embed(title=message, description=('You have now been reminded'),color=discord.Color.dark_teal())
    await asyncio.sleep(datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1])).timestamp()-datetime.datetime.today().timestamp())
    await ctx.send('<@'+str(author.id)+'>\n', embed=embed)


bot.run("updated to a new code")
