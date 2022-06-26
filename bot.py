import discord
from discord.ext import commands
import json
import os
import translators as translate

if os.path.exists(os.getcwd() + "/config.json"):
    with open("config.json") as f:
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

@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == '📥':
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        url = message.jump_url
        message = message.content
        translated_message = translate.google(message)
        embed = discord.Embed(title='English translation', description=translated_message)
        embed.add_field(name='original message',value=message + '\n' + url)
        await channel.send(embed=embed)


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
    
    @commands.command(name='translateMessage', aliases=['tm', 'translatemessage'])
    async def reply(self, ctx, to_language): 
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        message = message.content
        translated_message = translate.google(message, 'auto', str(to_language))
        await ctx.send(translated_message)

    @commands.command(name = 'languageGuide', aliases = ['lg', 'languageguide','languages'])
    async def countryGuide(self, ctx):
        file = open("languages.txt", 'r')
        await ctx.send(file.read())
        file.close()

    @commands.command(name = 'languageSearch', aliases = ['ls', 'searchlanguage', 'search', 'abbreviation'])
    async def languageSearch(self,ctx,*,language):
        if language in langDict.values():
            return await ctx.send(list(langDict.keys())[list(langDict.values()).index(language)])
        else:
            return await ctx.send(langDict[language.lower()])

    @commands.command(name = 'help', aliases = ['h', '?', 'Help', 'HELP', 'guide', 'commands', 'info', 'about'])
    async def helper(self, ctx, to_language='en'):
        help_title = '** Command Guide **\n Note: Languages must be in abbreviated form.\n'
        help_tl = '__ Translate __\n$[tl|tr] <source language> <target language> <message>\n'
        help_tltts = '__ Text-to-Speech __\n$tltts <source language> <target language> <message>\n'
        help_lg = '__ Language Guide __\n$lg\n'
        help_ls = '__ Language Abbrevation Search __\n$ls <target language>\n'
        help_tm = '__ Translate Message by Replying__\n$tm <target language>\n'
        help_react = '__Translate to English by Message Reaction__ \n react to message with 📥'
        help_message = help_title + help_tl + help_tltts + help_lg + help_ls+ help_tm + help_react
        translated_help_message = translate.google(help_message, 'en', str(to_language))
        translated_help_message = translated_help_message.lower()
        lines = translated_help_message.splitlines()
        final_message = ''
        for line in lines:
            if line[1] == ' ':
                line = line.replace(line[1], '', 1)
            final_message += line + '\n'
        return await ctx.send(final_message)


token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)
