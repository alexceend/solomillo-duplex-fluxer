import fluxer
import os
from bot_manager import *
from dotenv import load_dotenv
from random import random, randint
import commands.slots
import commands.work
import commands.balance
from Data_utilities import data_utilities

import asyncio

load_dotenv()

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user.username}")
    data_utilities.load_users_inventory_data()
    print(f"on_ready finished {data_utilities.get_users_inventory()}")

@bot.command()
async def ping(ctx):
    print(ctx)
    await ctx.reply("Pong!")
    #await ctx.send("Pong!")

if __name__ == "__main__":
    TOKEN = os.getenv('TOKEN_BOT')
    bot.run(TOKEN)
