import discord
from discord.ext import commands



client = commands.Bot(command_prefix = '!')

triggers = [
    '!klokken',
    '!commands'
]

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


client.run('NzU2NjI1MjYwMzkyMDg3NjIz.X2UkLw.PzEtwxWL1TI9LB1ocXM6GGVuvVo')