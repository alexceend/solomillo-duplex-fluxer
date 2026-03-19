import fluxer
import random
import asyncio
from bot_manager import *
import data_utilities

symbols = [" :bell: ", " :four_leaf_clover: ", " :seven: "]
reaction_waits = {}

@bot.command(name="slots")
async def run(ctx):
    if data_utilities.get_balance(ctx.author.id) < 100:
        await ctx.send(f"No tienes dinero !! eres pobre XD\nNecesitas 100{currency} para apostar")
    else:
        msg = await ctx.send("Start to roll slots!")
        await msg.add_reaction("🎰")

        event = asyncio.Event()
        reaction_waits[msg.id] = (event, ctx.author.id, "🎰")

        try:  
            await asyncio.wait_for(event.wait(), timeout=30.0)  
            await msg.edit("Rolling slots.\n" + get_shot())
            await msg.edit("Rolling slots..\n" + get_shot())
            await msg.edit("Rolling slots...\n" + get_shot())
            await msg.edit("Rolling slots\n" + get_shot())
            await msg.edit("Rolling slots.\n" + get_shot())
            await msg.edit("Rolling slots..\n" + get_shot())
            await msg.edit("Rolling slots...\n" + get_shot())
            result = get_shot()
            await msg.edit("-----RESULT-----\n" + result)
            if won(result):
                await ctx.send("YOU WON!")
                data_utilities.update_balance(ctx.author.id, data_utilities.get_balance(ctx.author.id) * 2)
            else:
                await ctx.send("gl next time!")
                data_utilities.update_balance(ctx.author.id, data_utilities.get_balance(ctx.author.id) - 100)

        except asyncio.TimeoutError:  
            await msg.edit("Timed out waiting for reaction!")  
        finally:  
            reaction_waits.pop(msg.id, None)  

@bot.event  
async def on_raw_reaction_add(event):  
    if event.message_id in reaction_waits:
        wait_event, user_id, expected_emoji = reaction_waits[event.message_id]

        if event.user_id == user_id and str(event.emoji) == expected_emoji:
            wait_event.set()

def won(result):
    raw = result.strip()
    return raw[1] == raw[2] == raw[3]

def get_shot():
    return "| " + symbols[random.randint(0, len(symbols) - 1)] + " " + symbols[random.randint(0, len(symbols) - 1)] + " " + symbols[random.randint(0, len(symbols) - 1)] + " |"