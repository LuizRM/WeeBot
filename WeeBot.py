import os

from random import randint
import praw

from discord.ext import commands
from dotenv import load_dotenv

#CONSTANTS DEFINITION
kasino_gifs = ["https://gfycat.com/bettervacantarrowworm",
"https://gfycat.com/harmlessbrightirishsetter",
"https://gfycat.com/brownvacanteeve",
"https://gfycat.com/grippingunfinishediberianchiffchaff"]

frases=["AEEEE KASINAAAO","VAI DIJEEI","AS BALADAS","SUCESSO IN-TER-NACIONAL","O SOM DA NOITE","KASINO AEEEEE","ARREBENTA"]


#ENVIRONMENT SETTINGS
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')      #TOKEN for the bot's login
GUILD = os.getenv('DISCORD_GUILD')

reddit = praw.Reddit(client_id='Ipmh7JRwQcNMNA',
                         client_secret="7lhfK2BGbidMt3X8nFDAc2fk5qo",
                         user_agent='prawtutorialV1')


bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')

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

# @bot.command(name='urss',help='Está na hora de tomar os meios de produção?Deixa que o bot aqui ajuda na ambientação.',brief='GLÓRIA À MÃE RUSSIA')
# async def urss(ctx):
#     autor = ctx.author
#     voice_client = await autor.voice.channel.connect()
#     print(f"{autor.name} solicitou musica do bot no canal {voice_client.channel.name}")
    #https://www.youtube.com/watch?v=4whPRKpbA4Qs

# @bot.command(name='stop')
# async def sair(ctx):
#     for client in bot.voice_clients:
#         if client.guild == ctx.guild:
#             voice = client
#     await voice.disconnect()

@bot.command(name='olhos',help='Viu algo que se arrependeu? Receba uma imagem ou gif com a solução: desinfetante visual',brief='Limpa seus olhos')
async def olhos(ctx):
    eyebleach = reddit.subreddit("eyebleach")
    hot = eyebleach.hot(limit=10)
    posts = []
    for submission in hot:
        posts.append((submission.title,submission.url))
    resultado = posts[randint(0,len(posts)-1)]
    print(resultado)
    await ctx.send(resultado[0])
    await ctx.send(resultado[1])

@bot.command(name='clear',help="Limpa todas as mensagens do canal")
async def clear(ctx):
    await ctx.message.channel.purge()

bot.run(TOKEN)
