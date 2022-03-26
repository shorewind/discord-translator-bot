from lib2to3.pgen2.tokenize import tokenize
import discord
from discord.ext import commands
import nltk 
import json
import os
import translators as ts


if os.path.exists(os.getcwd() + "/config.json"):
    with open(".\config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"token": ""}
    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate,f)


bot = commands.Bot(command_prefix='$')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot
 
    @commands.command(name= "test")
    async def test(self,ctx,*,message):
        puncts = nltk.tokenize.wordpunct_tokenize(message)  
        return await ctx.send(puncts)

    @commands.command(name='translate', alias = 'tl')
    async def translate(self,ctx,*,message):
        puncts = nltk.tokenize.wordpunct_tokenize(message)  
        eng = []
        outString = ""
        eng.append(ts.google(str(puncts)))
        for word in eng:
            outString +=  " " + word
        return await ctx.send(str(outString))
            



token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)