from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f'Pong! Latency: {round(self.bot.latency * 1000)} ms')

    @commands.command()
    async def cope(self, ctx):
        await ctx.reply('https://tenor.com/view/skill-issue-ratio-cancelled-twitter-cringe-gif-23133228')

def setup(bot):
    bot.add_cog(Fun(bot))