import math
from utilities import get_adminlist
from utilities import get_database
from utilities import shorten
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import lists
from helpers import checks


class General(commands.Cog, name="inv"):
    adminlist = get_adminlist()

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="inventory",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(page="The page number")
    #Command to get user inventory
    async def inventory(self, context: Context, page: int = 1, userid: int = 0) -> None:
        #Setup
        if userid == 0:
            userid = context.message.author.id
        #Fetching user userdata
        db = get_database()
        collection = db[str(userid)]
        userdata = collection.find_one()

        #Printing user userdata
        if page < 1:
            page = 1
        if page > math.ceil(len(userdata['inventory'])/5):
            page = math.ceil(len(userdata['inventory'])/5)
        embed = discord.Embed(
            description="Page: " + str(page) + "/" + str(math.ceil(len(userdata['inventory'])/5)),
            color=0x9C84EF
        )
        embed.set_author(
            name="Inventory"
        )
        if page == 0:
            for i in range(len(userdata['inventory'])):
                embed.add_field(
                    name=str(i + 1) + ". " + userdata['inventory'][str(i)]["name"],
                    value=userdata['inventory'][str(i)]["stats"],
                    inline=False
                )
        elif len(userdata['inventory']) > 0:
            if page > math.floor(len(userdata['inventory']) / 5):
                for i in range((page-1) * 5, len(userdata['inventory'])):
                    embed.add_field(
                        name=str(i + 1) + ". " + userdata['inventory'][str(i)]["name"],
                        value=userdata['inventory'][str(i)]["stats"],
                        inline=False
                    )
            else:
                for i in range((page-1)*5, page*5):
                    embed.add_field(
                        name=str(i+1) + ". " + userdata['inventory'][str(i)]["name"],
                        value=userdata['inventory'][str(i)]["stats"],
                        inline=False
                    )

        else:
            embed.add_field(
                name="EMPTY",
                value="EMPTY",
                inline=True
            )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="inv",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(page="The page number")
    async def inv(self, context: Context, page: int = 1, userid: int =0) -> None:

        if userid == 0:
            userid = context.message.author.id
        # Fetching user userdata
        db = get_database()
        collection = db[str(userid)]
        userdata = collection.find_one()

        if page < 1:
            page = 1
        if page > math.ceil(len(userdata['inventory']) / 5):
            page = math.ceil(len(userdata['inventory']) / 5)
        embed = discord.Embed(
            description="Page: " + str(page) + "/" + str(math.ceil(len(userdata['inventory']) / 5)),
            color=0x9C84EF
        )
        embed.set_author(
            name="Inventory"
        )
        if page == 0:
            for i in range(len(userdata['inventory'])):
                embed.add_field(
                    name=str(i + 1) + ". " + userdata['inventory'][str(i)]["name"],
                    value=userdata['inventory'][str(i)]["stats"],
                    inline=False
                )
        elif len(userdata['inventory']) > 0:
            if page > math.floor(len(userdata['inventory']) / 5):
                for i in range((page-1) * 5, len(userdata['inventory'])):
                    embed.add_field(
                        name=str(i + 1) + ". " + userdata['inventory'][str(i)]["name"],
                        value=userdata['inventory'][str(i)]["stats"],
                        inline=False
                    )
            else:
                for i in range((page-1)*5, page*5):
                    embed.add_field(
                        name=str(i+1) + ". " + userdata['inventory'][str(i)]["name"],
                        value=userdata['inventory'][str(i)]["stats"],
                        inline=False
                    )
        else:
            embed.add_field(
                name="EMPTY",
                value="EMPTY",
                inline=True
            )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="clearinv",
        description="clear inventory",
    )
    @checks.not_blacklisted()
    async def clearinv(self, context: Context, tag: str="all", userid: int = 0) -> None:
        if context.message.author.id not in get_adminlist():
            userid = context.message.author.id
        elif userid == 0:
            userid = context.message.author.id
        # Fetching user userdata
        db = get_database()
        collection = db[str(userid)]
        userdata = collection.find_one()
        leg_list = lists.get_leg_list()
        t3_dict = lists.get_t3_dict()
        t3_guard_dict = lists.get_t3_guard_dict()
        t3_list = list(t3_dict.values())
        t3_guard_list = list(t3_guard_dict.values())
        embed = discord.Embed(
            color=0x9C84EF
        )
        if tag == "all":
            userdata['inventory'] = {}
            embed.set_author(
                name="Inventory Cleared"
            )
        elif tag == "trash":
            keeplist = {}
            itemnum = 0
            for i in range(len(userdata['inventory'])):
                if userdata['inventory'][str(i)]["name"] in leg_list or userdata['inventory'][str(i)]["name"] in t3_list or userdata['inventory'][str(i)]["name"] in t3_guard_list:
                    keeplist[str(itemnum)] = userdata['inventory'][str(i)]
                    itemnum += 1
            userdata['inventory'] = keeplist
            embed.set_author(
                name="Inventory Cleared of Trash"
            )
        elif tag == "moretrash":
            keeplist = {}
            itemnum = 0
            for i in range(len(userdata['inventory'])):
                if userdata['inventory'][str(i)]["name"] in leg_list or \
                        userdata['inventory'][str(i)]["name"] in t3_list or \
                        userdata['inventory'][str(i)]["name"] in t3_guard_list:
                    if "Rarity: Gray" in userdata['inventory'][str(i)]["stats"] or \
                    "Rarity: Green" in userdata['inventory'][str(i)]["stats"] or \
                    "Rarity: Blue" in userdata['inventory'][str(i)]["stats"]:
                        pass
                    else:
                        keeplist[str(itemnum)] = userdata['inventory'][str(i)]
                        itemnum += 1
            userdata['inventory'] = keeplist
            embed.set_author(
                name="Inventory Cleared of Trash"
            )
        else:
            embed.set_author(
                name="Invalid Tag"
            )
        collection.drop()
        collection.insert_one(userdata)
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="viewinv",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(userid="The user's id",page="The page number")
    async def viewinv(self, context: Context, userid: int = 0, page: int = 1) -> None:
        if page < 1:
            page = 1

        # Fetching user userdata
        db = get_database()
        collection = db[str(userid)]
        userdata = collection.find_one()

        if page > math.ceil(len(userdata['inventory']) / 5):
            page = math.ceil(len(userdata['inventory'])/ 5)
        print(page)
        embed = discord.Embed(
            description="Page: " + str(page) + "/" + str(math.ceil(len(userdata['inventory']) / 5)),
            color=0x9C84EF
        )
        embed.set_author(
            name="Inventory"
        )

        if page == 0:
            for i in range(len(userdata['inventory'])):
                embed.add_field(
                    name=str(i + 1) + ". " + userdata['inventory'][str(i)]["name"],
                    value=userdata['inventory'][str(i)]["stats"],
                    inline=False
                )
        elif str(context.message.author.id) in userdata:
            if page > math.floor(len(userdata['inventory']) / 5):
                for i in range((page-1) * 5, len(userdata['inventory'])):
                    embed.add_field(
                        name=str(i + 1) + ". " + userdata['inventory'][str(i)]["name"],
                        value=userdata['inventory'][str(i)]["stats"],
                        inline=False
                    )
            else:
                for i in range((page-1)*5, page*5):
                    embed.add_field(
                        name=str(i+1) + ". " + userdata['inventory'][str(i)]["name"],
                        value=userdata['inventory'][str(i)]["stats"],
                        inline=False
                    )
        else:
            embed.add_field(
                name="EMPTY",
                value="EMPTY",
                inline=True
            )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="profile",
        description="view user profile",
    )
    @checks.not_blacklisted()
    async def profile(self, context: Context) -> None:
        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()
        level_dict = lists.get_level_dict()

        embed = discord.Embed(
            color=0x9C84EF
        )
        embed.set_author(
            name="Profile"
        )
        embed.add_field(
            name="Stats",
            value="Level: " + str(shorten(userdata["stats"]["level"])) + "\nExp: " + str(shorten(userdata["stats"]["exp"])) + " / " + str(shorten(level_dict[str(userdata["stats"]["level"])])) +
            "\nGold: " + str(shorten(userdata["stats"]["gold"])),
            inline=True
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="setlevel",
        description="set a user's level",
    )
    @checks.not_blacklisted()
    async def setlevel(self, context: Context, level: int=0, userid: int=0,) -> None:
        if userid == 0:
            userid = context.message.author.id
        if context.message.author.id in self.adminlist:
            db = get_database()
            collection = db[str(userid)]
            userdata = collection.find_one()
            userdata["stats"]["level"] = level
            collection.drop()
            collection.insert_one(userdata)

            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="debug setlevel"
            )
            embed.add_field(
                name="level set",
                value="Level: " + str(level),
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="Invalid"
            )
            embed.add_field(
                name="Invalid",
                value="You do not have permission to use this command",
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
