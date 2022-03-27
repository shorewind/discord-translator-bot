import discord
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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='$ commands'))
    print(f'{bot.user} is online!')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot
        global langDict
        self.bot = bot
        file = open('languages.txt','r')
        langDict = {}
        f = file.readlines()
        for line in f:
            words = line.split()
            langDict[words[0].lower()] = words[1]
        file.close()

    @commands.command(name='hello')
    async def test(self,ctx):
        return await ctx.send("Hello, world!")

    @commands.command(name='echo')
    async def echo(self, ctx, *, message):
        return await ctx.send(message)
   
    @commands.command(name='translate', aliases = ['tl', 'tr'])
    async def translate(self, ctx, from_language, to_language, *, message):
        translated_message = translate.google(message, str(from_language), str(to_language))
        return await ctx.send(translated_message)

    @commands.command(name = 'TranslateTTs', aliases = ['tltts', 'translatetts', 'translateTTS', 'translateTTs'])
    async def translateTTS(self,ctx, from_language, to_language, *, message):
         translated_message = translate.google(message, str(from_language), str(to_language))
         return await ctx.send(translated_message, tts=True)

    @commands.command(name = 'languageGuide', aliases = ['lg', 'languageguide','languages'])
    async def countryGuide(self, ctx):
        file = open("languages.txt", 'r')
        await ctx.send(file.read())
        file.close()

    @commands.command(name = 'languageSearch', aliases = ['ls', 'searchlanguage', 'search', 'abbreviation'])
    async def languageSearch(self,ctx,*,language):
        return await ctx.send(langDict[language.lower()])

    @commands.command(name = 'help', aliases = ['h', '?', 'Help', 'HELP', 'guide', 'commands'])
    async def helper(self, ctx, to_language='en'):
        help_title = '**Command Guide**\nNote: Languages must be in abbreviated form.\n'
        help_translate = '__ Translate __\n$tl|tr [from language] [to language] [message]\n'
        help_translatetts = '__ Text-to-Speech __\n$tltts [from language] [to language] [message]\n'
        help_languageguide = '__ Language Guide __\n$lg\n'
        help_languagesearch = '__ Language Abbrevation Search __\n$ls [language]'
        help_message = help_title + help_translate + help_translatetts + help_languageguide + help_languagesearch
        translated_help_message = translate.google(help_message, 'en', str(to_language))
        translated_help_message = translated_help_message.lower()
        return await ctx.send(translated_help_message)


token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)
