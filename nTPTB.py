from discord.ext import commands
import json
import os
import nltk
from lib2to3.pgen2.tokenize import tokenize
import translators as translate
import re



if os.path.exists(os.getcwd() + "/config.json"):
    with open(".\config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"token": ""}
    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate,f)


bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot

    @commands.command(name= "test")
    async def test(self,ctx,*,message):
        puncts = nltk.tokenize.wordpunct_tokenize(message)  
        return await ctx.send(puncts)

    @commands.command(name='terminate')
    async def terminate(self, ctx):
        await ctx.send('Goodbye')
        await bot.logout()

    @commands.command(name='hello')
    async def test(self,ctx):
        return await ctx.send("Hello, world!")

    @commands.command(name='echo')
    async def echo(self, ctx, *, message):
        return await ctx.send(message)
   
    @commands.command(name='translate', aliases = ['tl', 'Tl', 'tL', 'TL'])
    async def translate(self,ctx,*,message):
        eng =(translate.google(message))
        return await ctx.send(eng)

    @commands.command(name = 'TranslateTTs', aliases = ['tltts'])
    async def translateTTS(self,ctx, *, message):
         eng =(translate.google(message))
         return await ctx.send(eng, tts=True)

    @commands.command(name = 'countryGuide', aliases = ['cg', 'cG', 'Cg'])
    async def countryGuide(self, ctx):
        return await ctx.send("")
token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)