import math
import platform
import random
import aiohttp
from utilities import get_database
from utilities import get_adminlist
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import json

from helpers import checks


class General(commands.Cog, name="trading"):

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="trade",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def trade(self, context: Context, userid: int=0, giving: int=0, receiving: int=0) -> None:
        if context.message.author.id in get_adminlist():
            db = get_database()
            collection = db[str(userid)]
            destination = collection.find_one()
            db = get_database()
            collection2 = db[str(context.message.author.id)]
            origin = collection2.find_one()
            print(len(origin['inventory']))
            print(giving)
            print(len(destination['inventory']))
            print(receiving)
            if len(origin['inventory']) >= giving:
                if len(destination['inventory']) >= receiving:
                    authorlen = str(len(origin['trades']))
                    otherlen = str(len(destination['trades']))
                    origin['trades'][authorlen] = {}
                    origin['trades'][authorlen]["userid"] = str(userid)
                    origin['trades'][authorlen]["giving"] = giving
                    origin['trades'][authorlen]["receiving"] = receiving
                    origin['trades'][authorlen]["initiated"] = True
                    destination['trades'][otherlen] = {}
                    destination['trades'][otherlen]["userid"] = str(context.message.author.id)
                    destination['trades'][otherlen]["giving"] = receiving
                    destination['trades'][otherlen]["receiving"] = giving
                    destination['trades'][otherlen]["initiated"] = False
                    collection.drop()
                    collection.insert_one(destination)
                    collection2.drop()
                    collection2.insert_one(origin)

                    embed = discord.Embed(
                        color=0x9C84EF
                    )
                    embed.set_author(
                        name="Trade Sent"
                    )
                    embed.add_field(
                        name="Offering",
                        value=origin['inventory'][str(giving-1)]["name"] + "\n" + origin['inventory'][str(giving-1)]["stats"],
                        inline=False
                    )
                    embed.add_field(
                        name="Receiving",
                        value=destination['inventory'][str(receiving-1)]["name"] + "\n" +
                              destination['inventory'][str(receiving-1)]["stats"],
                        inline=False
                    )
                    embed.set_footer(
                        text=f"Requested by {context.author}"
                    )
                    await context.send(embed=embed)
            else:
                embed = discord.Embed(
                    description="Invalid item ID",
                    color=0x9C84EF
                )
                embed.set_author(
                    name="Error"
                )
                embed.set_footer(
                    text=f"Requested by {context.author}"
                )
                await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))