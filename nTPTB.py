from discord.ext import commands
import json
import os
from lib2to3.pgen2.tokenize import tokenize
import translators as translate

if os.path.exists(os.getcwd() + "/config.json"):
    with open(".\config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"token": ""}
    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate,f)

bot = commands.Bot(command_prefix='$', help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot

    @commands.command(name='hello')
    async def test(self,ctx):
        return await ctx.send("Hello, world!")

    @commands.command(name='echo')
    async def echo(self, ctx, *, message):
        return await ctx.send(message)
   
    @commands.command(name='translate', aliases = ['tl', 'Tl', 'tL', 'TL'])
    async def translate(self, ctx, from_language, to_language, *, message):
        translated_message = translate.google(message, str(from_language), str(to_language))
        return await ctx.send(translated_message)

    @commands.command(name = 'TranslateTTs', aliases = ['tltts'])
    async def translateTTS(self,ctx, from_language, to_language, *, message):
         translated_message = translate.google(message, str(from_language), str(to_language))
         return await ctx.send(translated_message, tts=True)

    @commands.command(name = 'countryGuide', aliases = ['cg', 'cG', 'Cg'])
    async def countryGuide(self, ctx):
        file = open("countries.txt", 'r')
        await ctx.send(file.read())
        file.close()

    @commands.command(name = 'help', aliases = ['h', '?'])
    async def helper(self, ctx, to_language='en'):
        help_message = 'help message'
        translated_help_message = translate.google(help_message, 'en', str(to_language))
        return await ctx.send(translated_help_message)


token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)
