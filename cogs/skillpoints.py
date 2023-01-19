import math
import platform
import random

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import json

from helpers import checks


class General(commands.Cog, name="skillpoints"):


    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="skillpoints",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def skillpoints(self, context: Context) -> None:
        with open('userstats.json') as json_file:
            userstats = json.load(json_file)
        if str(context.message.author.id) in userstats:
            pass
        else:
            userstats[str(context.message.author.id)] = {}
            userstats[str(context.message.author.id)]["level"] = 1
            userstats[str(context.message.author.id)]["exp"] = 1
            userstats[str(context.message.author.id)]["gold"] = 1
            userstats[str(context.message.author.id)]["war"] = 0
            userstats[str(context.message.author.id)]["mage"] = 0
            userstats[str(context.message.author.id)]["health"] = 0
            userstats[str(context.message.author.id)]["free"] = 0
            with open('userstats.json', 'w') as fp:
                json.dump(userstats, fp)
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Profile"
        )
        embed.add_field(
            name="Skill Point Distribution",
            value="War SP: " + str(userstats[str(context.message.author.id)]["war"]) + "\nMage SP: " + str(userstats[str(context.message.author.id)]["mage"]) +
            "\nHealth SP: " + str(userstats[str(context.message.author.id)]["health"]) + "\nFree SP: " + str(userstats[str(context.message.author.id)]["free"]),
            inline=True
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="assignsp",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def assignsp(self, context: Context, war: int=0, mage: int=0, health: int=0) -> None:
        with open('userstats.json') as json_file:
            userstats = json.load(json_file)
        if str(context.message.author.id) in userstats:
            pass
        else:
            userstats[str(context.message.author.id)] = {}
            userstats[str(context.message.author.id)]["level"] = 1
            userstats[str(context.message.author.id)]["exp"] = 1
            userstats[str(context.message.author.id)]["gold"] = 1
            userstats[str(context.message.author.id)]["war"] = 0
            userstats[str(context.message.author.id)]["mage"] = 0
            userstats[str(context.message.author.id)]["health"] = 0
            userstats[str(context.message.author.id)]["free"] = 0
            with open('userstats.json', 'w') as fp:
                json.dump(userstats, fp)
        if (war + mage + health) >= int(userstats[str(context.message.author.id)]["level"]):
            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="Error"
            )
            embed.add_field(
                name="You tried to distribute more points than you had",
                value="SP Distrubution Failed",
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)
        elif (war < 0) or (mage < 0) or (health < 0):
            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="Error"
            )
            embed.add_field(
                name="You tried to distribute negative points",
                value="SP Distrubution Failed",
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)
        else:
            userstats[str(context.message.author.id)]["war"] = war
            userstats[str(context.message.author.id)]["mage"] = mage
            userstats[str(context.message.author.id)]["health"] = health
            userstats[str(context.message.author.id)]["free"] = userstats[str(context.message.author.id)]["level"] - (war + mage + health)
            with open('userstats.json', 'w') as fp:
                json.dump(userstats, fp)
            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="Succesfully Distributed"
            )
            embed.add_field(
                name="Skill Point Distribution",
                value="War SP: " + str(userstats[str(context.message.author.id)]["war"]) + "\nMage SP: " + str(
                    userstats[str(context.message.author.id)]["mage"]) +
                      "\nHealth SP: " + str(userstats[str(context.message.author.id)]["health"]) + "\nFree SP: " + str(
                    userstats[str(context.message.author.id)]["free"]),
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))