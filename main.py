import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    # Cog loading

    for cog in os.listdir("cogs"):
        if not cog.endswith(".py"):
            continue
        bot.load_extension(f"cogs.{cog.replace('.py', '')}")

    print(f"HydroGen Bot is online")


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("https://media.discordapp.net/attachments/865333823041962024/902831647429361704/caption.gif")

    if isinstance(error, commands.CommandNotFound):
        pass


bot.run("ODAyNDE4MTY0Mjg5ODk2NDQ4.YAu8Jg.kmuVRkU4hu6mx6vjtfKeSeOFINM")
