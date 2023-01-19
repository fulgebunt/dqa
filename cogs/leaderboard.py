import math
import platform
import random
import aiohttp
import discord
from discord import app_commands, client
from discord.ext import commands
from discord.ext.commands import Context
import json

from helpers import checks


class General(commands.Cog, name="inventory"):


    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="leaderboard",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(type="leaderboard type")
    async def leaderboard(self, context: Context, type: str = "lvl") -> None:
        rankedlist = {}
        with open('userstats.json') as json_file:
            userstats = json.load(json_file)
        users = userstats.keys()
        for i in users:
            temp = userstats[i]["level"]
            if temp in rankedlist:
                rankedlist[temp].append(i)
            else:
                rankedlist[temp] = [i]
        levellist = rankedlist.keys()
        levels = list(levellist)
        levels.sort(reverse=True)
        usercount = 0
        breaking = False
        numlevels = 0
        for i in range(len(levels)):
            usercount += len(rankedlist[levels[i]])
            #full userlist
            #if usercount >= len(users):
            #    breaking = True
            if usercount > 5:
                breaking = True
            if breaking:
                numlevels = i
                break


        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Leaderboard"
        )
        for i in range(numlevels):
            for j in range(len(rankedlist[levels[i]])):
                embed.add_field(
                    name=str(await context.bot.fetch_user(int(rankedlist[levels[i]][j]))),
                    value=str(levels[i]),
                    inline=False
                )

        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)
async def setup(bot):
    await bot.add_cog(General(bot))