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

bot.run("80671bed1e4695b4a113d54b5fcf0c2eceb9303e2733e4a84ce92bd15c7cf883")