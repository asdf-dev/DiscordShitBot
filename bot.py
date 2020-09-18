import discord
import os
from discord.ext import commands

triggers = [
    '!klokken',
    '!commands'
]

Token = "NzU2NjI1MjYwMzkyMDg3NjIz.X2UkLw.PzEtwxWL1TI9LB1ocXM6GGVuvVo" #fake btw

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot ready')


@client.command(aliases=['klokken'])
async def BuyMonner(ctx):
    try:
        await ctx.send('Det monner tid!')
    except TypeError as e:
        print("TypeError:", e)
    except discord.HTTPException as e:
        print("http fuckup: ", e)


#How to run with env's
#docker run -e Token=test ... <image-name> ...
if "Token" in os.environ:
    Token = os.environ['Token']
    pass


client.run(Token)