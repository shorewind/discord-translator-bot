from discord.ext import commands
import json
import os
import translators as translate

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
   
    @commands.command(name='translate')
    async def translate(self, ctx, *, message):
        text_translated = translate.google(message)
        await ctx.send(text_translated)


token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)
