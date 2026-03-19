import fluxer
import random
import asyncio
from bot_manager import *
from Data_utilities import data_utilities

@bot.command(name="work")
async def run(ctx):
    money = get_money()
    await ctx.send("You worked hard and earnt " + str(money) + f"{currency}")
    data_utilities.update_balance(str(ctx.author.id), data_utilities.get_balance(ctx.author.id) + money )

def get_money():
    return random.randint(800,1000)