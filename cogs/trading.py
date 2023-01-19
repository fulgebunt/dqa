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


class General(commands.Cog, name="trading"):

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="trade",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def trade(self, context: Context, userid: int=0, giving: int=0, receiving: int=0) -> None:
        with open('userinv.json') as json_file:
            inv = json.load(json_file)
        with open('trades.json') as json_file:
            trades = json.load(json_file)
        if str(context.message.author.id) not in trades:
            trades[str(context.message.author.id)] = {}
        if str(userid) not in trades:
            trades[str(userid)] = {}
        print(len(inv[str(context.message.author.id)]))
        print(giving)
        print(len(inv[str(userid)]))
        print(receiving)
        if len(inv[str(context.message.author.id)]) >= giving:
            if len(inv[str(userid)]) >= receiving:
                authorlen = str(len(trades[str(context.message.author.id)]))
                otherlen = str(len(trades[str(userid)]))
                trades[str(context.message.author.id)][authorlen] = {}
                trades[str(context.message.author.id)][authorlen]["userid"] = str(userid)
                trades[str(context.message.author.id)][authorlen]["giving"] = giving
                trades[str(context.message.author.id)][authorlen]["receiving"] = receiving
                trades[str(context.message.author.id)][authorlen]["initiated"] = True
                trades[str(userid)][otherlen] = {}
                trades[str(userid)][otherlen]["userid"] = str(context.message.author.id)
                trades[str(userid)][otherlen]["giving"] = receiving
                trades[str(userid)][otherlen]["receiving"] = giving
                trades[str(userid)][otherlen]["initiated"] = False
                with open('trades.json', 'w') as fp:
                    json.dump(trades, fp)

                embed = discord.Embed(
                    color=0x9C84EF
                )
                embed.set_author(
                    name="Trade Sent"
                )
                embed.add_field(
                    name="Offering",
                    value=inv[str(context.message.author.id)][str(giving-1)]["name"] + "\n" + inv[str(context.message.author.id)][str(giving-1)]["stats"],
                    inline=False
                )
                embed.add_field(
                    name="Receiving",
                    value=inv[str(userid)][str(receiving-1)]["name"] + "\n" +
                          inv[str(userid)][str(receiving-1)]["stats"],
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

    @commands.hybrid_command(
        name="listtrade",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def listtrade(self, context: Context) -> None:
        with open('userinv.json') as json_file:
            inv = json.load(json_file)
        with open('trades.json') as json_file:
            trades = json.load(json_file)
        if str(context.message.author.id) not in trades:
            embed = discord.Embed(
                description="Invalid Trade",
                color=0x9C84EF
            )
            embed.set_author(
                name="No trades exist"
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
                name="List of Trades"
            )
            for i in range(len(trades[str(context.message.author.id)])):
                embed.add_field(
                    name="Trade #" + str(i+1),
                    value="",
                    inline=False
                )
                embed.add_field(
                    name="Offering",
                    value=inv[str(context.message.author.id)][str(trades[str(context.message.author.id)][str(i)]["receiving"]-1)]["name"] + "\n" +
                          inv[str(context.message.author.id)][str(trades[str(context.message.author.id)][str(i)]["receiving"]-1)]["stats"],
                    inline=False
                )
                embed.add_field(
                    name="Receiving",
                    value=inv[str(trades[str(context.message.author.id)][str(i)]["userid"])][str(trades[str(context.message.author.id)][str(i)]["giving"]-1)]["name"] + "\n" +
                          inv[str(trades[str(context.message.author.id)][str(i)]["userid"])][str(trades[str(context.message.author.id)][str(i)]["giving"]-1)]["stats"],
                    inline=False
                )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))