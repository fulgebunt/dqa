import platform
import random
from utilities import get_database
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
                name="$damage (dungeon)",
                value="Shows the damage the user deals, and their clear chance of a dungeon",
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
        new = {
            "inventory": {

            },
            "stats": {
                "level": 1,
                "exp": 0,
                "gold": 0,
                "war": 0,
                "mage": 0,
                "health": 0,
                "free": 0
            },
            "equipped": {
                "helmname": "Empty",
                "armorname": "Empty",
                "weapname": "Empty",
                "helmstats": "Empty",
                "armorstats": "Empty",
                "weapstats": "Empty",
                "spellname": "Empty",
                "spellstats": "Empty"
            },
            "trades": {
            }
        }
        dbname = get_database()
        collection = dbname[str(context.message.author.id)]
        collection.drop()
        collection = dbname[str(context.message.author.id)]
        collection.insert_one(new)

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