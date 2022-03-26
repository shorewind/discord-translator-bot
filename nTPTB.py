import discord
from discord.ext import commands
import nltk 

client = discord.Client()
bot = commands.Bot(command_prefix='$')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot
    @commands.command(name='test')
    async def test(self,ctx):
        return await ctx.send("Hello, world!")


def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run('OTU3MDkzNTQ3ODM4OTM5MTM2.Yj5w0w.CvtXi2-UfFc8cZ6ckY7Ywd86CdY')