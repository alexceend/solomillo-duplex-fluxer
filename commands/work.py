import fluxer
import random
import asyncio
from datetime import datetime
from bot_manager import *
from Data_utilities import data_utilities

works = [
    ("Has lamido los zapatos de un empresario, por pena te ha dado ",(50,100)),
    ("Enhorabuena, has cubrido una baja de 1 mes en el McDonalds, salario: ",(100,200)),
    ("Has estado todo el día limpiando los parabrisas de los coches en una gasolinera por ",(25,50)),
    ("Estás de suerte, te has encontrado a Cristiano Ronaldo por la calle y por hacerle una foto te ha dado ",(500,1000))
    ]

@bot.command(name="work")
async def run(ctx):
    work, money = get_work()
    await ctx.send(work + str(money) + f"{currency}")
    data_utilities.update_balance(str(ctx.author.id), data_utilities.get_balance(ctx.author.id) + money )

def get_work():
    #print(datetime.now().total_seconds())
    work = works[random.randint(0, len(works) - 1)]
    return work[0], random.randint(work[1][0],work[1][1]),