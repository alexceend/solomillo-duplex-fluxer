import fluxer
import random
import asyncio
from bot_manager import *
from Data_utilities import data_utilities

@bot.command(name="balance")
async def run(ctx):
    await ctx.reply("You currently have " + str(data_utilities.get_balance(ctx.author.id)) + f"{currency}")