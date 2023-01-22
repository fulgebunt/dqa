from utilities import get_database
import discord
from discord.ext import commands
from discord.ext.commands import Context
import lists

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
        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()
        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Profile"
        )
        embed.add_field(
            name="Skill Point Distribution",
            value="War SP: " + str(userdata["stats"]["war"]) + "\nMage SP: " + str(userdata["stats"]["mage"]) +
            "\nHealth SP: " + str(userdata["stats"]["health"]) + "\nFree SP: " + str(userdata["stats"]["free"]),
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
        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()
        if (war + mage + health) >= int(userdata["stats"]["level"]):
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
            userdata["stats"]["war"] = war
            userdata["stats"]["mage"] = mage
            userdata["stats"]["health"] = health
            userdata["stats"]["free"] = userdata["stats"]["level"] - (war + mage + health) - 1
            collection.drop()
            collection.insert_one(userdata)
            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="Succesfully Distributed"
            )
            embed.add_field(
                name="Skill Point Distribution",
                value="War SP: " + str(userdata["stats"]["war"]) + "\nMage SP: " + str(
                    userdata["stats"]["mage"]) +
                      "\nHealth SP: " + str(userdata["stats"]["health"]) + "\nFree SP: " + str(
                    userdata["stats"]["free"]),
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))