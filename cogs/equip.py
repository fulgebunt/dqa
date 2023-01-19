import math
import platform
import random
import aiohttp
import discord
from utilities import get_database
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import json
from helpers import checks

class General(commands.Cog, name="equip"):

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="equip",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(item="item number to be equipped")
    async def equip(self, context: Context, item: int = 0) -> None:


        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()
        if item <= len(userdata["inventory"]) and item > 0:
            if "Helm" in userdata["inventory"][str(item-1)]["stats"]:
                userdata["equipped"]["helmname"] = userdata["inventory"][str(item-1)]["name"]
                userdata["equipped"]["helmstats"] = userdata["inventory"][str(item-1) ]["stats"]
            elif "Chest" in userdata["inventory"][str(item-1)]["stats"]:
                userdata["equipped"]["armorname"] = userdata["inventory"][str(item-1)]["name"]
                userdata["equipped"]["armorstats"] = userdata["inventory"][str(item-1)]["stats"]
            elif "Spell" in userdata["inventory"][str(item-1)]["stats"]:
                userdata["equipped"]["spellname"] = userdata["inventory"][str(item-1)]["name"]
                userdata["equipped"]["spellstats"] = userdata["inventory"][str(item-1)]["stats"]
            else:
                userdata["equipped"]["weapname"] = userdata["inventory"][str(item-1)]["name"]
                userdata["equipped"]["weapstats"] = userdata["inventory"][str(item-1)]["stats"]

        collection.drop()
        collection.insert_one(userdata)
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Equipped"
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="equipped",
        description="show equipped items",
    )
    @checks.not_blacklisted()
    async def equipped(self, context: Context) -> None:
        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Equipped Items"
        )

        embed.add_field(
            name="Helm",
            value=userdata["equipped"]["helmname"] + "\n" + userdata['equipped']["helmstats"],
            inline=False
        )
        embed.add_field(
            name="Armor",
            value=userdata["equipped"]["armorname"] + "\n" + userdata['equipped']["armorstats"],
            inline=False
        )
        embed.add_field(
            name="Weapon",
            value=userdata["equipped"]["weapname"] + "\n" + userdata['equipped']["weapstats"],
            inline=False
        )
        embed.add_field(
            name="Spell",
            value=userdata["equipped"]["spellname"] + "\n" + userdata['equipped']["spellstats"],
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="damage",
        description="show damage",
    )
    @checks.not_blacklisted()
    async def damage(self, context: Context) -> None:
        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()
        with open('spellData.json') as json_file:
            spells = json.load(json_file)
        highest = userdata["stats"]["war"]
        stat = "War"
        if userdata["stats"]["mage"] > highest:
            highest = userdata["stats"]["mage"]
            stat = "Mage"
        skill = highest
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Damage"
        )
        if (userdata["equipped"]["helmstats"] != "Empty") and stat in userdata["equipped"]["helmstats"]:
            helmstats = userdata["equipped"]["helmstats"].split("\n")
            helm = int(helmstats[1][5:])
            print(helm)
        else:
            helm = 1
        if (userdata["equipped"]["armorstats"] != "Empty") and stat in userdata["equipped"]["armorstats"]:
            armorstats = userdata["equipped"]["armorstats"].split("\n")
            arm = int(armorstats[1][5:])
        else:
            arm = 1
        if (userdata["equipped"]["weapstats"] != "Empty") and stat in userdata["equipped"]["weapstats"]:
            weapstats = userdata["equipped"]["weapstats"].split("\n")
            wep = int(weapstats[1][5:])
        else:
            wep = 1
        if (userdata["equipped"]["spellstats"] != "Empty") and stat in userdata["equipped"]["spellstats"]:
            SPELL_MULT = int(spells[userdata["equipped"]["spellname"]]["Damage"])/100
        else:
            SPELL_MULT = 1
        damage = math.floor((wep * (0.6597 + 0.013202 * skill)*((arm+helm)*0.0028))*SPELL_MULT)
        embed.add_field(
            name="Your total damage is",
            value=damage,
            inline=True
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)
async def setup(bot):
    await bot.add_cog(General(bot))