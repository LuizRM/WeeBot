import os

from random import randint

from discord.ext import commands
from dotenv import load_dotenv

#CONSTANTS DEFINITION
kasino_gifs = ["https://gfycat.com/bettervacantarrowworm",
"https://gfycat.com/harmlessbrightirishsetter",
"https://gfycat.com/brownvacanteeve",
"https://gfycat.com/grippingunfinishediberianchiffchaff"]

frases=["AEEEE KASINAAAO","VAI DIJEEI","AS BALADAS","SUCESSO IN-TER-NACIONAL","O SOM DA NOITE","KASINO AEEEEE","ARREBENTA"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')      #TOKEN for the bot's login
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})\n')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Esse comando não é válido, seu animal. Sabe ler? Então digita `!help` pra aprender a usar esse bot")

@bot.command(name='gay',help="Descubra quanto cada um aqui é gay")
async def porcentagem(ctx):
    print("Chega pra nois bão")
    for member in ctx.guild.members:
        if member.name != bot.user.name:
            resultado = randint(0,100)
            resposta = f"- {member.name} é {resultado}% gay"
            await ctx.send(resposta)

@bot.command(name='senha',help='Qual é a senha pra o joguinho da turma?')
async def manda_senha(ctx):
    await ctx.send("A senha era, ainda é e sempre será: jmgay")

@bot.command(name='marcus',help='Marcus citou cachaça de novo? Chame esse comando pra registrar esse momento',brief='Adiciona ao numero de citações de cachaça')
async def marcus(ctx):
    valor = int(os.getenv("DISCORD_MARCUS"))
    await ctx.send(f"Marcus tinha citado cachaça {valor} vezes nesta call, adicionando mais uma vez. Que tristeza!")
    valor += 1
    os.environ["DISCORD_MARCUS"] = str(valor)

@bot.command(name='kasino',help='Este comando serve para invocar Gilberto Barros e seu convidado mais ilustre, Kasino',brief='AEEE KASINAAAO')
async def kasino(ctx):
    frase = frases[randint(0,len(frases)-1)]
    gif = kasino_gifs[randint(0,len(frases)-1)]
    await ctx.send(frase)
    await ctx.send(gif)

bot.run(TOKEN)
