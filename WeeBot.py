#imports
import os

from random import randint,choices
import praw

from discord import File, Embed, Colour
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import string

#LINKS DEFINITION
kasino_gifs = ["https://gfycat.com/bettervacantarrowworm",
"https://gfycat.com/harmlessbrightirishsetter",
"https://gfycat.com/brownvacanteeve",
"https://gfycat.com/grippingunfinishediberianchiffchaff",
"https://gfycat.com/decisivesoftbarnswallow"]

frases=["AEEEE KASINAAAO","VAI DIJEEI","AS BALADAS","SUCESSO IN-TER-NACIONAL","O SOM DA NOITE","KASINO AEEEEE","ARREBENTA"]

bola = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes – definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]


#ENVIRONMENT SETTINGS
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')      #TOKEN for the bot's login
REDDIT_SECRET = os.getenv('REDDIT_SECRET')

reddit = praw.Reddit(client_id='Ipmh7JRwQcNMNA',
                         client_secret=REDDIT_SECRET,
                         user_agent='my_agent')

#----------------------------------------------------------BOT COMMANDS-------------------------------------------------------------------
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')

@bot.event
async def on_command_error(ctx,error):
    print(f"Command error! Guild ID:{ctx.guild.id}")
    print(error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Esse comando não é válido, seu animal. Sabe ler? Então digita `!help` pra aprender a usar esse bot")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Você não me deu algum argumento necessário para fazer este comando. Como tu quer que eu trabalhe assim? Digite `!help <nome_do_comando>` para ver seu uso")

@bot.command(name='gay',help="Descubra quanto cada um aqui é gay")
async def porcentagem(ctx):
    print("Chega pra nois bão")
    for member in ctx.guild.members:
        if not (member.bot):
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

#Comandos para streamar musica. Não funcionaram, então por enquanto estão parados aqui
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
    eyebleach = reddit.subreddit("eyebleach")   #Creates a new isinstance of eyebleach subreddit
    hot = eyebleach.hot(limit=20)               #Fetches 10 posts from its hot section
    posts = []
    print(f"[Reddit]Carregando posts... (Guild ID:{ctx.guild.id})")
    for submission in hot:
        posts.append((submission.title,submission.url,submission.author))
    print(f"[Reddit]Posts carregados! (Guild ID:{ctx.guild.id})")
    resultado = posts[randint(0,len(posts)-1)]
    print(resultado)
    post = Embed(title=resultado[0],colour=Colour.teal())
    post.set_image(url=resultado[1])
    post.set_footer(text=f'From user {resultado[2]} @ Reddit')
    await ctx.send(embed=post)

@bot.command(name='chonk',help='Uma imagem fresquinha de um gato gordo',brief='Gatos gordos')
async def gordos(ctx):
    chonkers = reddit.subreddit("chonkers")    #Creates a new isinstance of eyebleach subreddit
    hot = chonkers.hot(limit=20)               #Fetches 10 posts from its hot section
    posts = []
    print(f"[Reddit]Carregando posts... (Guild ID:{ctx.guild.id})")
    for submission in hot:
        posts.append((submission.title,submission.url,submission.author))
    print(f"[Reddit]Posts carregados! (Guild ID:{ctx.guild.id})")
    resultado = posts[randint(0,len(posts)-1)]
    print(resultado)
    post = Embed(title=resultado[0],colour=Colour.teal())
    post.set_image(url=resultado[1])
    post.set_footer(text=f'From user {resultado[2]} @ Reddit')
    await ctx.send(embed=post)

@bot.command(name='8ball',help='Tem uma decisão difícil a ser tomada?Pergunte à gloriosa 8ball',brief='Pergunte à 8ball')
async def ball(ctx):
    resposta = bola[randint(0,len(bola)-1)]
    await ctx.send(f":8ball: {resposta}")

@bot.command(name='maisteco',help="Digite o comando + o link direto para a imagem a ser adicionada às imagens do teco teco e peteleco",brief="Adiciona imagens ao teco teco")
async def imagem(ctx, link:str):
    nome = "teco/" + link.split('/')[-1]
    urllib.request.urlretrieve(link,nome)

@bot.command(name='tecoteco',help='ganhe uma amostra grátis das belas fantasias da turma do teco teco e peteleco',brief='Imagem do Teco Teco')
async def teco(ctx):
    diretorio = os.listdir("teco")
    print(diretorio)
    resultado = "teco/" + diretorio[randint(0,len(diretorio)-1)]
    print(resultado)
    arquivo = File(resultado)
    await ctx.send(arquivo)

@bot.command(name='clear',help="Limpa todas as mensagens do canal")
async def clear(ctx):
    await ctx.message.channel.purge()

bot.run(TOKEN)
