from discord.ext import commands
from data import *


class Gen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stock(self, ctx):
        await fetchstock(ctx)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)  # 60 seconds = 1 min
    async def get(self, ctx, accounts):
        await ctx.author.send(
            embed=discord.Embed(title="Generated an account for you. This message will delete after 60 seconds. **!!LOOKING FOR RESTOCKERS DM synaps#9794!!**",
                                colour=discord.Colour.green(),
                                description=f"```{fetch(accounts.lower())}```"), delete_after=60)

        await ctx.message.add_reaction('✅')


def setup(bot):
    bot.add_cog(Gen(bot))
