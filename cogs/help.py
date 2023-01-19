import platform
import random

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import json

from helpers import checks


class General(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="help",
        description="command information",
    )
    @checks.not_blacklisted()
    async def inventory(self, context: Context, page: int=1) -> None:
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Command List"
        )
        if page == 1:
            embed.add_field(
                name="Page 1/3",
                value="",
                inline=False
            )
            embed.add_field(
                name="$new",
                value="Refresh your profile",
                inline=False
            )
            embed.add_field(
                name="$raid (dungeon) (difficulty) (mode)",
                value="Dungeon Codes: DT, WO, PI, KC, UW, SP, TC, GH, SS,\nBR1-BR30, OO, VC, AT, EF, NL, GS\n\nDifficulty Codes: Easy (1), Medium (2), \nHard (3), Insane (4), Nightmare (5)\n\nMode Codes: Non-Hardcore (NHC), Hardcore (HC), or Waves (WVS).\n",
                inline=False
            )
            embed.add_field(
                name="$inventory (page #)",
                value="Displays player inventory",
                inline=False
            )
            embed.add_field(
                name="$viewinv (userid) (page#)",
                value="Displays another player's inventory",
                inline=False
            )
        elif page == 2:
            embed.add_field(
                name="Page 2/3",
                value="",
                inline=False
            )
            embed.add_field(
                name="$clearinv (tag)",
                value="Clears player inventory - leave blank to clear entire inventory, use the tag 'trash' to exclude t3 and legendaries, user the tag 'moretrash' to exclude purple t3 and legendaries",
                inline=False
            )
            embed.add_field(
                name="$equip (item #)",
                value="Equips an item to the player",
                inline=False
            )
            embed.add_field(
                name="$equipped",
                value="Shows equipped items",
                inline=False
            )
            embed.add_field(
                name="$damage",
                value="Shows the damage the user deals",
                inline=False
            )
        elif page == 3:
            embed.add_field(
                name="Page 3/3",
                value="",
                inline=False
            )
            embed.add_field(
                name="$skillpoints",
                value="Shows the user's skillpoint distribution",
                inline=False
            )
            embed.add_field(
                name="$assignsp (war) (mage) (health)",
                value="Distributes skillpoints",
                inline=False
            )
            embed.add_field(
                name="$trade (userid) (giving) (receiving)",
                value="Sends a trade request to another user",
                inline=False
            )
            embed.add_field(
                name="$leaderboard",
                value="Shows the leaderboard",
                inline=False
            )
        else:
            embed.add_field(
                name="Invalid Page",
                value="?/3",
                inline=False
            )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)


    @commands.hybrid_command(
        name="new",
        description="command information",
    )
    @checks.not_blacklisted()
    async def new(self, context: Context) -> None:
        with open('userinv.json') as json_file:
            userinv = json.load(json_file)
        str[context.message.author.id] = {}
        with open('userinv.json', 'w') as fp:
            json.dump(userinv, fp)
        with open('userstats.json') as json_file:
            userstats = json.load(json_file)
        userstats[str(context.message.author.id)] = {}
        userstats[str(context.message.author.id)]["level"] = 1
        userstats[str(context.message.author.id)]["exp"] = 1
        userstats[str(context.message.author.id)]["gold"] = 1
        userstats[str(context.message.author.id)]["war"] = 0
        userstats[str(context.message.author.id)]["mage"] = 0
        userstats[str(context.message.author.id)]["health"] = 0
        userstats[str(context.message.author.id)]["free"] = 0
        with open('userequips.json') as json_file:
            equips = json.load(json_file)
        with open('userstats.json', 'w') as fp:
            json.dump(userstats, fp)
        equips[str(context.message.author.id)] = {}
        equips[str(context.message.author.id)]["helmname"] = "Empty"
        equips[str(context.message.author.id)]["armorname"] = "Empty"
        equips[str(context.message.author.id)]["weapname"] = "Empty"
        equips[str(context.message.author.id)]["helmstats"] = "Empty"
        equips[str(context.message.author.id)]["armorstats"] = "Empty"
        equips[str(context.message.author.id)]["weapstats"] = "Empty"
        equips[str(context.message.author.id)]["spellname"] = "Empty"
        equips[str(context.message.author.id)]["spellstats"] = "Empty"
        with open('userequips.json', 'w') as fp:
            json.dump(equips, fp)
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Profile Creation"
        )
        embed.add_field(
            name="Success",
            value="Your profile has been refreshed",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))