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


class General(commands.Cog, name="inv"):
    adminlist = [421086209431961600, 383710782686232597, 426402208515620864]

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="inventory",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(page="The page number")
    async def inventory(self, context: Context, page: int = 1) -> None:
        with open('userinv.json') as json_file:
            data = json.load(json_file)
        if str(context.message.author.id) in data:
            pass
        else:
            data[context.message.author.id] = {}
            with open('userinv.json', 'w') as fp:
                json.dump(data, fp)
        if page < 1:
            page = 1
        if page > math.ceil(len(data[str(context.message.author.id)])/5):
            page = math.ceil(len(data[str(context.message.author.id)])/5)
        embed = discord.Embed(
            description="Page: " + str(page) + "/" + str(math.ceil(len(data[str(context.message.author.id)])/5)),
            color=0x9C84EF
        )
        embed.set_author(
            name="Inventory"
        )
        if page == 0:
            for i in range(len(data[str(context.message.author.id)])):
                embed.add_field(
                    name=str(i + 1) + ". " + data[str(context.message.author.id)][str(i)]["name"],
                    value=data[str(context.message.author.id)][str(i)]["stats"],
                    inline=False
                )
        elif str(context.message.author.id) in data:
            if page > math.floor(len(data[str(context.message.author.id)]) / 5):
                for i in range((page-1) * 5, len(data[str(context.message.author.id)])):
                    embed.add_field(
                        name=str(i + 1) + ". " + data[str(context.message.author.id)][str(i)]["name"],
                        value=data[str(context.message.author.id)][str(i)]["stats"],
                        inline=False
                    )
            else:
                for i in range((page-1)*5, page*5):
                    embed.add_field(
                        name=str(i+1) + ". " + data[str(context.message.author.id)][str(i)]["name"],
                        value=data[str(context.message.author.id)][str(i)]["stats"],
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
    async def inv(self, context: Context, page: int = 1) -> None:
        with open('userinv.json') as json_file:
            data = json.load(json_file)
        if str(context.message.author.id) in data:
            pass
        else:
            data[context.message.author.id] = {}
            with open('userinv.json', 'w') as fp:
                json.dump(data, fp)
        if page < 1:
            page = 1
        if page > math.ceil(len(data[str(context.message.author.id)]) / 5):
            page = math.ceil(len(data[str(context.message.author.id)]) / 5)
        embed = discord.Embed(
            description="Page: " + str(page) + "/" + str(math.ceil(len(data[str(context.message.author.id)]) / 5)),
            color=0x9C84EF
        )
        embed.set_author(
            name="Inventory"
        )
        if page == 0:
            for i in range(len(data[str(context.message.author.id)])):
                embed.add_field(
                    name=str(i + 1) + ". " + data[str(context.message.author.id)][str(i)]["name"],
                    value=data[str(context.message.author.id)][str(i)]["stats"],
                    inline=False
                )
        elif str(context.message.author.id) in data:
            if page > math.floor(len(data[str(context.message.author.id)]) / 5):
                for i in range((page-1) * 5, len(data[str(context.message.author.id)])):
                    embed.add_field(
                        name=str(i + 1) + ". " + data[str(context.message.author.id)][str(i)]["name"],
                        value=data[str(context.message.author.id)][str(i)]["stats"],
                        inline=False
                    )
            else:
                for i in range((page-1)*5, page*5):
                    embed.add_field(
                        name=str(i+1) + ". " + data[str(context.message.author.id)][str(i)]["name"],
                        value=data[str(context.message.author.id)][str(i)]["stats"],
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
    async def clearinv(self, context: Context, tag: str="all") -> None:
        with open('userinv.json') as json_file:
            userinv = json.load(json_file)

        leg_list = ["Desert Fury", "Crystalised Greatsword", "Soulstealer Greatsword", "Staff of the Gods",
                    "Beast Master War Scythe", "Beast Master Spell Scythe", "Dual Phoenix Daggers",
                    "Phoenix Greatstaff",
                    "Sakura Katana", "Sakura Greatstaff", "Overlords Rageblade", "Overlords Manablade", "Kraken Slayer",
                    "Sea Serpent Wings", "Inventors Greatsword", "Inventors Spellblade", "Galactic Dual Blades",
                    "Galactic Pike", "Lava Kings Warscythe", "Lava Kings Spell Daggers", "Sea Kings Greatstaff",
                    "Sea Kings Trident", "Eldenbark Greatsword", "Eldenbark Greatstaff", "Mjolnir", "Gungnir", "Hofund",
                    "Laevateinn", "Gildenscale Oath and Aegis", "Daybreak and Gildensong"]
        leg_dict = {
            "dt": {
                "War": "Desert Fury",
                "Mage": "Desert Fury"
            },
            "wo": {
                "War": "Crystalised Greatsword",
                "Mage": "Crystalised Greatsword"
            },
            "pi": {
                "War": "Soulstealer Greatsword",
                "Mage": "Staff of the Gods"
            },
            "kc": {
                "War": "Beast Master War Scythe",
                "Mage": "Beast Master Spell Scythe"
            },
            "uw": {
                "War": "Dual Phoenix Daggers",
                "Mage": "Phoenix Greatstaff"
            },
            "sp": {
                "War": "Sakura Katana",
                "Mage": "Sakura Greatstaff"
            },
            "tc": {
                "War": "Overlords Rageblade",
                "Mage": "Overlords Manablade"
            },
            "gh": {
                "War": "Kraken Slayer",
                "Mage": "Sea Serpent Wings"
            },
            "ss": {
                "War": "Inventors Greatsword",
                "Mage": "Inventors Spellblade"
            },
            "oo": {
                "War": "Galactic Dual Blades",
                "Mage": "Galactic Pike"
            },
            "vc": {
                "War": "Lava Kings Warscythe",
                "Mage": "Lava Kings Spell Daggers"
            },
            "at": {
                "War": "Sea Kings Trident",
                "Mage": "Sea Kings Greatstaff"
            },
            "ef": {
                "War": "Eldenbark Greatsword",
                "Mage": "Eldenbark Greatstaff"
            },
            "nl": {
                "War": "Mjolnir",
                "Mage": "Gungnir"
            },
            "gs": {
                "War": "Gildenscale Oath and Aegis",
                "Mage": "Daybreak and Gildensong"
            }
        }
        t3_dict = {
            "pi": "Godly",
            "kc": "TitanForged",
            "uw": "Glorious",
            "sp": "Ancestral",
            "tc": "Overlords",
            "gh": "Mythical",
            "ss": "WarForged",
            "oo": "Alien",
            "vc": "Lava Kings",
            "at": "Triton",
            "ef": "Eldenbark",
            "nl": "Valhalla",
            "gs": "Gildenscale"
        }
        t3_guard_dict = {
            "pi": "Godly Guardian",
            "kc": "TitanForged Guardian",
            "uw": "Glorious Guardian",
            "sp": "Ancestral Guardian",
            "tc": "Overlords Guardian",
            "gh": "Mythical Guardian",
            "ss": "WarForged Guardian",
            "oo": "Alien Guardian",
            "vc": "Lava Kings Guardian",
            "at": "Triton Guardian",
            "ef": "Eldenbark Guardian",
            "nl": "Valhalla Guardian",
            "gs": "Gildenscale Guardian"
        }
        t3_list = list(t3_dict.values())
        t3_guard_list = list(t3_guard_dict.values())
        embed = discord.Embed(
            color=0x9C84EF
        )
        if tag == "all":
            if str(context.message.author.id) in userinv:
                userinv[str(context.message.author.id)] = {}
                embed.set_author(
                    name="Inventory Cleared"
                )
        elif tag == "trash":
            keeplist = {}
            itemnum = 0
            if str(context.message.author.id) in userinv:
                for i in range(len(userinv[str(context.message.author.id)])):
                    if userinv[str(context.message.author.id)][str(i)]["name"] in leg_list or userinv[str(context.message.author.id)][str(i)]["name"] in t3_list or userinv[str(context.message.author.id)][str(i)]["name"] in t3_guard_list:
                        keeplist[str(itemnum)] = userinv[str(context.message.author.id)][str(i)]
                        itemnum += 1
                userinv[str(context.message.author.id)] = keeplist
                embed.set_author(
                    name="Inventory Cleared of Trash"
                )
        elif tag == "moretrash":
            keeplist = {}
            itemnum = 0
            if str(context.message.author.id) in userinv:
                for i in range(len(userinv[str(context.message.author.id)])):
                    if userinv[str(context.message.author.id)][str(i)]["name"] in leg_list or \
                            userinv[str(context.message.author.id)][str(i)]["name"] in t3_list or \
                            userinv[str(context.message.author.id)][str(i)]["name"] in t3_guard_list:
                        if "Rarity: Gray" in userinv[str(context.message.author.id)][str(i)]["stats"] or \
                        "Rarity: Green" in userinv[str(context.message.author.id)][str(i)]["stats"] or \
                        "Rarity: Blue" in userinv[str(context.message.author.id)][str(i)]["stats"]:
                            pass
                        else:
                            keeplist[str(itemnum)] = userinv[str(context.message.author.id)][str(i)]
                            itemnum += 1
                userinv[str(context.message.author.id)] = keeplist
                embed.set_author(
                    name="Inventory Cleared of Trash"
                )
        else:
            embed.set_author(
                name="Invalid Tag"
            )
        with open('userinv.json', 'w') as fp:
            json.dump(userinv, fp)


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
        with open('userinv.json') as json_file:
            data = json.load(json_file)
        if page < 1:
            page = 1

        print(userid)
        if str(userid) not in data:
            data[userid] = {}
            with open('userinv.json', 'w') as fp:
                json.dump(data, fp)
        print(page)


        if page > math.ceil(len(data[str(userid)]) / 5):
            page = math.ceil(len(data[str(userid)])/ 5)
        print(page)
        embed = discord.Embed(
            description="Page: " + str(page) + "/" + str(math.ceil(len(data[str(userid)]) / 5)),
            color=0x9C84EF
        )
        embed.set_author(
            name="Inventory"
        )

        if page == 0:
            for i in range(len(data[str(userid)])):
                embed.add_field(
                    name=str(i + 1) + ". " + data[str(userid)][str(i)]["name"],
                    value=data[str(userid)][str(i)]["stats"],
                    inline=False
                )
        elif str(context.message.author.id) in data:
            if page > math.floor(len(data[str(userid)]) / 5):
                for i in range((page-1) * 5, len(data[str(userid)])):
                    embed.add_field(
                        name=str(i + 1) + ". " + data[str(userid)][str(i)]["name"],
                        value=data[str(userid)][str(i)]["stats"],
                        inline=False
                    )
            else:
                for i in range((page-1)*5, page*5):
                    embed.add_field(
                        name=str(i+1) + ". " + data[str(userid)][str(i)]["name"],
                        value=data[str(userid)][str(i)]["stats"],
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
        with open('userstats.json') as json_file:
            userstats = json.load(json_file)
        level_dict = {
            "1": 84,
            "2": 94,
            "3": 107,
            "4": 121,
            "5": 136,
            "6": 154,
            "7": 174,
            "8": 197,
            "9": 223,
            "10": 252,
            "11": 285,
            "12": 322,
            "13": 364,
            "14": 411,
            "15": 464,
            "16": 525,
            "17": 593,
            "18": 670,
            "19": 758,
            "20": 856,
            "21": 967,
            "22": 1093,
            "23": 1235,
            "24": 1396,
            "25": 1578,
            "26": 1783,
            "27": 2015,
            "28": 2277,
            "29": 2573,
            "30": 2907,
            "31": 3285,
            "32": 3712,
            "33": 4195,
            "34": 4740,
            "35": 5357,
            "36": 6053,
            "37": 6840,
            "38": 7730,
            "39": 8734,
            "40": 9870,
            "41": 11153,
            "42": 12603,
            "43": 14242,
            "44": 16093,
            "45": 18185,
            "46": 20549,
            "47": 23221,
            "48": 26240,
            "49": 29651,
            "50": 33506,
            "51": 37861,
            "52": 42783,
            "53": 48345,
            "54": 54630,
            "55": 61732,
            "56": 69757,
            "57": 78826,
            "58": 89073,
            "59": 100653,
            "60": 113738,
            "61": 128524,
            "62": 145232,
            "63": 164112,
            "64": 185447,
            "65": 209555,
            "66": 236798,
            "67": 267581,
            "68": 302367,
            "69": 341675,
            "70": 386092,
            "71": 436285,
            "72": 493002,
            "73": 557092,
            "74": 629514,
            "75": 711351,
            "76": 803826,
            "77": 908324,
            "78": 1026406,
            "79": 1159839,
            "80": 1310618,
            "81": 1480998,
            "82": 1673528,
            "83": 1891087,
            "84": 2136929,
            "85": 2414729,
            "86": 2728644,
            "87": 3083368,
            "88": 3484206,
            "89": 3937153,
            "90": 4448983,
            "91": 5027350,
            "92": 5680906,
            "93": 6419424,
            "94": 7253949,
            "95": 8196962,
            "96": 9262568,
            "97": 10466702,
            "98": 11827373,
            "99": 13364931,
            "100": 15102372,
            "101": 17065681,
            "102": 19284220,
            "103": 21791168,
            "104": 24624020,
            "105": 27825143,
            "106": 31442411,
            "107": 35529925,
            "108": 40148815,
            "109": 45368161,
            "110": 51266022,
            "111": 57930605,
            "112": 65461584,
            "113": 73971590,
            "114": 83587897,
            "115": 94454323,
            "116": 106733385,
            "117": 120608726,
            "118": 136287860,
            "119": 154005282,
            "120": 174025968,
            "121": 196649344,
            "122": 222213759,
            "123": 251101548,
            "124": 283744749,
            "125": 320631567,
            "126": 362313671,
            "127": 409414448,
            "128": 462638326,
            "129": 522781309,
            "130": 590742879,
            "131": 667539453,
            "132": 754319582,
            "133": 852381128,
            "134": 963190674,
            "135": 1088405462,
            "136": 1229898172,
            "137": 1389784935,
            "138": 1570456976,
            "139": 1774616383,
            "140": 2005316513,
            "141": 2266007660,
            "142": 2560588656,
            "143": 2893465181,
            "144": 3269615655,
            "145": 3694665690,
            "146": 4174972230,
            "147": 4717718620,
            "148": 5331022041,
            "149": 6024054906,
            "150": 6807182044,
            "151": 7692115710,
            "152": 8692090752,
            "153": 9822062550,
            "154": 11098930681,
            "155": 12541791670,
            "156": 14172224587,
            "157": 16014613784,
            "158": 18096513575,
            "159": 20449060340,
            "160": 23107438185,
            "161": 26111405149,
            "162": 29505887818,
            "163": 33341653234,
            "164": 37676068155,
            "165": 42573957015,
            "166": 48108571427,
            "167": 54362685713,
            "168": 61429834856,
            "169": 69415713387,
            "170": 78439756127,
            "171": 88636924424,
            "172": 100159724599,
            "173": 113180488797,
            "174": 127893952341,
            "175": 144520166145,
            "176": 163307787744,
            "177": 184537800151,
            "178": 208527714170,
            "179": 235636317013,
            "180": 266269038224,
            "181": 300884013194,
            "182": 339998934909,
            "183": 384198796447,
            "184": 434144639985,
            "185": 490583443184,
            "186": 554359290797,
            "187": 626425998601,
            "188": 707861378419,
            "189": 799883357614,
            "190": 903868194104,
            "191": 1021371059337,
            "192": 1154149297051,
            "193": 1304188705668,
            "194": 1473733237405,
            "195": 1665318558268,
            "196": 1881809970843,
            "197": 2126445267052,
            "198": 2402883151769,
            "199": 2715257961499,
            "200": 3068241496494,
            "201": 3467112891038,
            "202": 3917837566873,
            "203": 4427156450567,
            "204": 5002686789141,
            "205": 5653036071729,
            "206": 6387930761054,
            "207": 7218361759991,
            "208": 8156748788790,
            "209": 9217126131333,
            "210": 10415352528406,
            "211": 11769348357099,
            "212": 13299363643522,
            "213": 15028280917180,
            "214": 16981957436413,
            "215": 19189611903147,
            "216": 21684261450556,
            "217": 24503215439128,
            "218": 27688633446215,
            "219": 31288155794223,
            "220": 35355616047472,
            "221": 39951846133644,
            "222": 45145586131017,
            "223": 51014512328050,
            "224": 57646398930696,
            "225": 65140430791687,
            "226": 73608686794606,
            "227": 83177816077905,
            "228": 93990932168033,
            "229": 106209753349877,
            "230": 120017021285361,
            "231": 135619234052458,
            "232": 153249734479278,
            "233": 173172199961584,
            "234": 195684585956590,
            "235": 221123582130947,
            "236": 249869647807970,
            "237": 282352702023006,
            "238": 319058553285997,
            "239": 360536165213176,
            "240": 407405866690889,
            "241": 460368629360705,
            "242": 520216551177596,
            "243": 587844702830684,
            "244": 664264514198673,
            "245": 750618901044500,
            "246": 848199358180285,
            "247": 958465274743722,
            "248": 1083065760460406,
            "249": 1223864309320259,
            "250": 1382966669531892,
            "251": 1562752336571038,
            "252": 1765910140325273,
            "253": 1995478458567558,
            "254": 2254890658181341,
            "255": 2548026443744915,
            "256": 2879269881431754,
            "257": 3253574966017882,
            "258": 3676539711600205,
            "259": 4154489874108232,
            "260": 4694573557742302,
            "261": 5304868120248800,
            "262": 5994500975881144,
            "263": 6773786102745693,
            "264": 7654378296102631,
            "265": 8649447474595973,
            "266": 9773875646293448,
            "267": 11044479480311594,
            "268": 12480261812752102,
            "269": 14102695848409872,
            "270": 15936046308703156,
            "271": 18007732328834564,
            "272": 20348737531583056,
            "273": 22994073410688848,
            "274": 25983302954078400,
            "275": 29361132338108588,
            "276": 33178079542062700,
            "277": 37491229882530848,
            "278": 42365089767259856,
            "279": 47872551437003632,
            "280": 54095983123814096,
            "281": 61128460929909920,
            "282": 69075160850798200,
            "283": 78054931761401968,
            "284": 88202072890384208,
            "285": 99668342366134160,
            "286": 112625226873731584,
            "287": 127266506367316672,
            "288": 143811152195067840,
            "289": 162506601980426624,
            "290": 183632460237882080,
            "291": 207504680068806752,
            "292": 234480288477751584,
            "293": 264962725979859264,
            "294": 299407880357240960,
            "295": 338330904803682240,
            "296": 382313922428160896,
            "297": 432014732343821760,
            "298": 488176647548518592,
            "299": 551639611729825920
        }
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
            name="Stats",
            value="Level: " + str(userstats[str(context.message.author.id)]["level"]) + "\nExp: " + str(userstats[str(context.message.author.id)]["exp"]) + " / " + str(level_dict[str(userstats[str(context.message.author.id)]["level"])]) +
            "\nGold: " + str(userstats[str(context.message.author.id)]["gold"]),
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
    async def setlevel(self, context: Context, userid: int=0, level: int=0) -> None:
        if context.message.author.id in self.adminlist:
            with open('userstats.json') as json_file:
                userstats = json.load(json_file)
            userstats[str(userid)]["level"] = level
            with open('userstats.json', 'w') as fp:
                json.dump(userstats, fp)

            embed = discord.Embed(
                color=0x9C84EF
            )
            embed.set_author(
                name="debug setlevel"
            )
            embed.add_field(
                name="level set",
                value="Level: " + str(userstats[str(userid)]["level"]),
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