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

bot = commands.Bot(command_prefix="+")
@bot.event
async def on_ready():
    print("Bot is ready")

bot.run("")
