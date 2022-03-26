import discord
from discord.ext import commands
import nltk 
import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    with open(".\config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"token": ""}
    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate,f)

client = discord.Client()
bot = commands.Bot(command_prefix='$')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot
 
    @commands.command(name='test')
    async def test(self,ctx):
        return await ctx.send("Hello, world!")


token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)