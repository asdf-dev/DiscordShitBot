import discord
import os
from datetime import date
from discord.ext import commands

triggers = [
    '**!commands** - *denne besked*',
    '**!settilbud** - *eg. !settilbud monner 10kr netto*',
    '**!tilbud** - *se tilbud*'
]
Token = "NzU3MTk3NDMwOTgxNjU2NTk2.X2c5Dw.o0v-HcoMhBpNgmxHRyzRJlBaw8g" #fake btw

SpottetTilbud = ""

#How to run with env's
#docker run -e Token=test ... <image-name> ...
if "Token" in os.environ:
    Token = os.environ['Token']
    pass


client = commands.Bot(command_prefix = '!', help_command=None)


@client.event
async def on_ready():
    print('Bot ready')


@client.command(aliases=['commands'])
async def Commands(ctx):
    try:
        svar = 'Commands:\n' + '\n'.join(triggers)
        await ctx.send(svar)
    except TypeError as e:
        print("TypeError:", e)
    except discord.HTTPException as e:
        print("http fuckup: ", e)

@client.command(aliases=['settilbud']) #bedre navn plx husk at rette i commands
async def NytTilbud(ctx, *spot):
    try:
        SetTilbud(" ".join(spot), ctx.message.author.name) #bruger name - da display navn kan skiftes efter kald.
        await ctx.message.add_reaction("👍")
    except TypeError as e:
        print("TypeError:", e)
    except discord.HTTPException as e:
        print("http fuckup: ", e)



@client.command(aliases=['tilbud'])
async def GetTilbudBot(ctx):
    try:
        await ctx.send(getTilbud())
    except TypeError as e:
        print("TypeError:", e)
    except discord.HTTPException as e:
        print("http fuckup: ", e)

def SetTilbud(tilbud, navn):
    global SpottetTilbud
    Idag = date.today().strftime("%d/%m/%Y")
    _tilbud = "{}: {} \nSidst opdateret: {}".format(navn, tilbud, Idag)
    SpottetTilbud = _tilbud

def getTilbud():
    if not SpottetTilbud:
        return "intet fundet" 
    return SpottetTilbud

client.run(Token)