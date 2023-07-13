import os

import discord


def fetch(accounts: str) -> str:
    with open("data/" + accounts + '.txt', 'r') as filein:
        data = filein.read().splitlines(True)
    with open("data/" + accounts + '.txt', 'w') as fileout:
        line = data[:1][0]
        fileout.writelines(data[1:])
        return line


async def fetchstock(ctx):
    embed = discord.Embed(title="Account Stock", colour=discord.Colour.teal(), description="")
    for file in os.listdir("data"):
        # if file == __file__ or file == ".git" or file == ".idea":
        if not file.endswith(".txt"):
            continue

        with open(f"data/{file}", "r") as filein:
            embed.description += f"**{file.capitalize().replace('.txt', '')}**: {len(filein.readlines())}\n"

    await ctx.reply(embed=embed)
