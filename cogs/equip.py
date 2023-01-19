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

        with open('userinv.json') as json_file:
            inv = json.load(json_file)
        with open('userequips.json') as json_file:
            equips = json.load(json_file)
        if item <= len(inv[str(context.message.author.id)]) and item > 0:
            if str(context.message.author.id) not in equips:
                equips[str(context.message.author.id)] = {}
                equips[str(context.message.author.id)]["helmname"] = "Empty"
                equips[str(context.message.author.id)]["armorname"] = "Empty"
                equips[str(context.message.author.id)]["weapname"] = "Empty"
                equips[str(context.message.author.id)]["helmstats"] = "Empty"
                equips[str(context.message.author.id)]["armorstats"] = "Empty"
                equips[str(context.message.author.id)]["weapstats"] = "Empty"
                equips[str(context.message.author.id)]["spellname"] = "Empty"
                equips[str(context.message.author.id)]["spellstats"] = "Empty"
            if "Helm" in inv[str(context.message.author.id)][str(item-1)]["stats"]:
                equips[str(context.message.author.id)]["helmname"] = inv[str(context.message.author.id)][str(item-1)]["name"]
                equips[str(context.message.author.id)]["helmstats"] = inv[str(context.message.author.id)][str(item-1) ]["stats"]
            elif "Chest" in inv[str(context.message.author.id)][str(item-1)]["stats"]:
                equips[str(context.message.author.id)]["armorname"] = inv[str(context.message.author.id)][str(item-1)]["name"]
                equips[str(context.message.author.id)]["armorstats"] = inv[str(context.message.author.id)][str(item-1)]["stats"]
            elif "Spell" in inv[str(context.message.author.id)][str(item-1)]["stats"]:
                equips[str(context.message.author.id)]["spellname"] = inv[str(context.message.author.id)][str(item-1)]["name"]
                equips[str(context.message.author.id)]["spellstats"] = inv[str(context.message.author.id)][str(item-1)]["stats"]
            else:
                equips[str(context.message.author.id)]["weapname"] = inv[str(context.message.author.id)][str(item-1)]["name"]
                equips[str(context.message.author.id)]["weapstats"] = inv[str(context.message.author.id)][str(item-1)]["stats"]


        with open('userequips.json', 'w') as fp:
            json.dump(equips, fp)
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
        with open('userequips.json') as json_file:
            equips = json.load(json_file)
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Equipped Items"
        )
        if str(context.message.author.id) in equips:
            embed.add_field(
                name="Helm",
                value=equips[str(context.message.author.id)]["helmname"] + "\n" + equips[
                    str(context.message.author.id)]["helmstats"],
                inline=False
            )
            embed.add_field(
                name="Armor",
                value=equips[str(context.message.author.id)]["armorname"] + "\n" + equips[
                    str(context.message.author.id)]["armorstats"],
                inline=False
            )
            embed.add_field(
                name="Weapon",
                value=equips[str(context.message.author.id)]["weapname"] + "\n" + equips[
                    str(context.message.author.id)]["weapstats"],
                inline=False
            )
            embed.add_field(
                name="Spell",
                value=equips[str(context.message.author.id)]["spellname"] + "\n" + equips[
                    str(context.message.author.id)]["spellstats"],
                inline=False
            )
        else:
            embed.add_field(
                name="Empty",
                value="Empty",
                inline=True
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
        with open('userequips.json') as json_file:
            equips = json.load(json_file)
        with open('spellData.json') as json_file:
            spells = json.load(json_file)
        with open('userstats.json') as json_file:
            stats = json.load(json_file)
        highest = stats[str(context.message.author.id)]["war"]
        if stats[str(context.message.author.id)]["mage"] > highest:
            highest = stats[str(context.message.author.id)]["mage"]
        skill = highest
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Damage"
        )
        if str(context.message.author.id) in equips:
            if equips[str(context.message.author.id)]["helmstats"] != "Empty":
                helmstats = equips[str(context.message.author.id)]["helmstats"].split("\n")
                helm = int(helmstats[1][5:])
            else:
                helm = 1
            if equips[str(context.message.author.id)]["armorstats"] != "Empty":
                armorstats = equips[str(context.message.author.id)]["armorstats"].split("\n")
                arm = int(armorstats[1][5:])
            else:
                arm = 1
            if equips[str(context.message.author.id)]["weapstats"] != "Empty":
                weapstats = equips[str(context.message.author.id)]["weapstats"].split("\n")
                wep = int(weapstats[1][5:])
            else:
                wep = 1
            if equips[str(context.message.author.id)]["spellstats"] != "Empty":
                SPELL_MULT = int(spells[equips[str(context.message.author.id)]["spellname"]]["Damage"])/100
            else:
                SPELL_MULT = 1
            print(arm)
            print(helm)
            print(wep)
            print(0.6597 + 0.013202 * skill)
            print((arm+helm)*0.0028)
            print((wep * (0.6597 + 0.013202 * skill)*((arm+helm)*0.0028))*SPELL_MULT)
            damage = math.floor((wep * (0.6597 + 0.013202 * skill)*((arm+helm)*0.0028))*SPELL_MULT)
            embed.add_field(
                name="Your total damage is",
                value=damage,
                inline=True
            )
        else:
            embed.add_field(
                value="N/A",
                name="You have nothing equipped",
                inline=True
            )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)
async def setup(bot):
    await bot.add_cog(General(bot))