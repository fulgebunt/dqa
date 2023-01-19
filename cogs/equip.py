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
    async def damage(self, context: Context, dung: str="dt") -> None:
        damage_gates = {
  "dt": {
    "1": {
      "min": 1,
      "max": 1
    },
    "2": {
      "min": 1,
      "max": 1
    },
    "3": {
      "min": 1,
      "max": 1
    },
    "4": {
      "min": 1,
      "max": 1
    },
    "5": {
      "min": 1,
      "max": 1
    }
  },
  "wo": {
    "1": {
      "min": 1,
      "max": 1
    },
    "2": {
      "min": 1,
      "max": 1
    },
    "3": {
      "min": 1,
      "max": 1
    },
    "4": {
      "min": 1,
      "max": 1
    },
    "5": {
      "min": 1,
      "max": 1
    }
  },
  "pi": {
    "4": {
      "min": 1,
      "max": 162916
    },
    "5": {
      "min": 162916,
      "max": 738487
    }
  },
  "kc": {
    "4": {
      "min": 482232,
      "max": 1654379
    },
    "5": {
      "min": 1654379,
      "max": 8676735
    }
  },
  "uw": {
    "4": {
      "min": 5963503,
      "max": 14573049
    },
    "5": {
      "min": 14573049,
      "max": 36958863
    }
  },
  "sp": {
    "4": {
      "min": 29567090,
      "max": 61558932
    },
    "5": {
      "min": 61558932,
      "max": 181983567
    }
  },
  "tc": {
    "4": {
      "min": 144180217,
      "max": 419825999
    },
    "5": {
      "min": 419825999,
      "max": 893671521
    }
  },
  "gh": {
    "4": {
      "min": 763592104,
      "max": 1738592292
    },
    "5": {
      "min": 1738592292,
      "max": 5580019482
    }
  },
  "ss": {
    "4": {
      "min": 4391896029,
      "max": 10270841120
    },
    "5": {
      "min": 10270841120,
      "max": 30571979892
    }
  },
  "oo": {
    "4": {
      "min": 22514248758,
      "max": 443050348144
    },
    "5": {
      "min": 443050348144,
      "max": 1401043912623
    }
  },
  "vc": {
    "4": {
      "min": 916580376537,
      "max": 2511647524847
    },
    "5": {
      "min": 2511647524847,
      "max": 7628358177706
    }
  },
  "at": {
    "4": {
      "min": 0,
      "max": 12606801168245
    },
    "5": {
      "min": 12606801168245,
      "max": 37088616556535
    }
  },
  "ef": {
    "4": {
      "min": 30899994418565,
      "max": 63859672403788
    },
    "5": {
      "min": 63859672403788,
      "max": 188668177076686
    }
  },
  "nl": {
    "4": {
      "min": 157108787154550,
      "max": 312611214558692
    },
    "5": {
      "min": 312611214558692,
      "max": 904717196044072
    }
  },
  "gs": {
    "4": {
      "min": 760489176934816,
      "max": 1512304433113689
    },
    "5": {
      "min": 1512304433113689,
      "max": 4495306129317689
    }
  },
  "om": {
    "4": {
      "min": 3719325425193000,
      "max": 7047476787972479
    },
    "5": {
      "min": 7047476787972479,
      "max": 20634397774821292
    }
  },
  "wt": {
    "4": {
      "min": 17509964108529648,
      "max": 34376434213563368
    },
    "5": {
      "min": 34376434213563368,
      "max": 99472216092176352
    }
  },
  "ec": {
    "4": {
      "min": 83539188234517840,
      "max": 174070594276045376
    },
    "5": {
      "min": 174070594276045376,
      "max": 499207900505063296
    }
  }
}
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
        if damage < 1:
            damage = 1
        diff = 4
        if damage >= damage_gates[dung][str(diff)]["max"]:
            cleared = True
            percent = 100
        elif damage < damage_gates[dung][str(diff)]["min"]:
            cleared = False
            percent = 0
        else:
            percent = math.floor(((damage - damage_gates[dung][str(diff)]["min"]) / (
                    damage_gates[dung][str(diff)]["max"] - damage_gates[dung][str(diff)]["min"])) * 100)
            roll = random.randint(0, 100)
            if roll <= percent:
                cleared = True

        embed.add_field(
            name="Your total damage is",
            value=damage,
            inline=True
        )
        embed.add_field(
            name="Your clear chance of " + dung + " insane is:",
            value=str(percent) + "%",
            inline=True
        )

        diff = 5
        if damage >= damage_gates[dung][str(diff)]["max"]:
            percent = 100
            cleared = True
        elif damage < damage_gates[dung][str(diff)]["min"]:
            cleared = False
            percent = 0
        else:
            print((damage - damage_gates[dung][str(diff)]["min"]))
            print(damage_gates[dung][str(diff)]["max"] - damage_gates[dung][str(diff)]["min"])
            percent = math.floor(((damage - damage_gates[dung][str(diff)]["min"]) / (
                    damage_gates[dung][str(diff)]["max"] - damage_gates[dung][str(diff)]["min"]))*100)
            roll = random.randint(0, 100)
            if roll <= percent:
                cleared = True
        embed.add_field(
            name="Your clear chance of " + dung + " nightmare is:",
            value=str(percent) + "%",
            inline=True
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)
async def setup(bot):
    await bot.add_cog(General(bot))