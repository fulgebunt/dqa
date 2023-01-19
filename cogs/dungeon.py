import platform
import random

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import json
from utilities import get_database
from helpers import checks


class General(commands.Cog, name="dungeon"):

    #Items
    with open('itemValues.json') as json_file:
        data = json.load(json_file)
    with open('raidValues.json') as json_file:
        brdata = json.load(json_file)
    adminlist = [421086209431961600,383710782686232597,426402208515620864]
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="raid",
        description="Raid a Dungeon",
    )
    @checks.not_blacklisted()
    @app_commands.describe(dung="The dungeon to raid (DT, WO, PI, KC, UW, SP, TC, GH, SS, BR1-BR30, OO, VC, AT, EF, NL, GS)", diffi="Easy (1), Medium (2), Hard (3), Insane (4), Nightmare (5)", mode="Non-Hardcore (NHC), Hardcore (HC), or Waves (WVS).")
    async def raid(self, context: Context,  dung: str = "Desert Temple",  diffi: str = "5", mode: str = "HC") -> None:
        #Temp
        # Fetching user userdata
        db = get_database()
        collection = db[str(context.message.author.id)]
        userdata = collection.find_one()

        error = False
        dungeon = "N/A"
        dung = dung.lower()
        mode = mode.upper()
        t3chance = 5
        color_dict = {
            'dt': 0xFFFF00,
            'wo': 0xFFFFFF,
            'pi': 0x23272A,
            'kc': 0xF1C40F,
            'uw': 0xED4245,
            'sp': 0xE91E63,
            'tc': 0x979C9F,
            'gh': 0x11806A,
            'ss': 0xC27C0E,
            'oo': 0x3498DB,
            'vc': 0xE67E22,
            'at': 0x1ABC9C,
            'ef': 0xAD1457,
            'nl': 0x95A5A6,
            'gs': 0xFFBF00,
        }
        leg_list = ["Desert Fury","Crystalised Greatsword","Soulstealer Greatsword","Staff of the Gods",
                    "Beast Master War Scythe","Beast Master Spell Scythe","Dual Phoenix Daggers","Phoenix Greatstaff",
                    "Sakura Katana","Sakura Greatstaff","Overlords Rageblade","Overlords Manablade","Kraken Slayer",
                    "Sea Serpent Wings","Inventors Greatsword","Inventors Spellblade","Galactic Dual Blades",
                    "Galactic Pike","Lava Kings Warscythe","Lava Kings Spell Daggers","Sea Kings Greatstaff",
                    "Sea Kings Trident","Eldenbark Greatsword","Eldenbark Greatstaff","Mjolnir","Gungnir","Hofund",
                    "Laevateinn","Gildenscale Oath and Aegis","Daybreak and Gildensong"]
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
        ult_dict = {
            "nl": {
                "War": "Hofund",
                "Mage": "Laevateinn"
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
        exp_dict = {
            "dt": {
                1: 232,
                2: 354,
                3: 680,
                4: 1118,
                5: 2253

            },
            "wo": {
                1: 6564,
                2: 9180,
                3: 16140,
                4: 27840,
                5: 46180,
            },
            "pi": {
                4: 51150,
                5: 82200
            },
            "kc": {
                4: 135900,
                5: 271800
            },
            "uw": {
                4: 546000,
                5: 924000
            },
            "sp": {
                4: 1934000,
                5: 3500000
            },
            "tc": {
                4: 4594000,
                5: 8005000
            },
            "gh": {
                4: 12840000,
                5: 24160000
            },
            "ss": {
                4: 35700000,
                5: 59600000
            },
            "oo": {
                4: 329000000,
                5: 506500000
            },
            "vc": {
                4: 755000000,
                5: 1225000000
            },
            "at": {
                4: 2034000000,
                5: 3564000000
            },
            "ef": {
                4: 6900000000,
                5: 11280000000
            },
            "nl": {
                4: 21820000000,
                5: 36600000000
            },
            "gs": {
                4: 63500000000,
                5: 115500000000
            }
        }
        gold_dict = {
            "dt": {
                1: 600,
                2: 1200,
                3: 2400,
                4: 4800,
                5: 9600

            },
            "wo": {
                1: 18000,
                2: 48000,
                3: 80000,
                4: 125000,
                5: 200000,
            },
            "pi": {
                4: 240000,
                5: 325000
            },
            "kc": {
                4: 550000,
                5: 750000
            },
            "uw": {
                4: 1250000,
                5: 1500000
            },
            "sp": {
                4: 2400000,
                5: 3625000
            },
            "tc": {
                4: 4875000,
                5: 6125000
            },
            "gh": {
                4: 8500000,
                5: 11750000
            },
            "ss": {
                4: 21000000,
                5: 27500000
            },
            "oo": {
                4: 50000000,
                5: 60000000
            },
            "vc": {
                4: 90000000,
                5: 100000000
            },
            "at": {
                4: 110000000,
                5: 120000000
            },
            "ef": {
                4: 150000000,
                5: 170000000
            },
            "nl": {
                4: 200000000,
                5: 225000000
            },
            "gs": {
                4: 300000000,
                5: 410000000
            }
        }
        lvl_dict = {
            "dt": {
                1: 1,
                2: 6,
                3: 12,
                4: 20,
                5: 27

            },
            "wo": {
                1: 33,
                2: 40,
                3: 45,
                4: 50,
                5: 55,
            },
            "pi": {
                4: 60,
                5: 65
            },
            "kc": {
                4: 70,
                5: 75
            },
            "uw": {
                4: 80,
                5: 85
            },
            "sp": {
                4: 90,
                5: 95
            },
            "tc": {
                4: 100,
                5: 105
            },
            "gh": {
                4: 110,
                5: 115
            },
            "ss": {
                4: 120,
                5: 125
            },
            "oo": {
                4: 140,
                5: 145
            },
            "vc": {
                4: 150,
                5: 155
            },
            "at": {
                4: 160,
                5: 165
            },
            "ef": {
                4: 170,
                5: 175
            },
            "nl": {
                4: 180,
                5: 185
            },
            "gs": {
                4: 190,
                5: 195
            }
        }
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
        damage_gates = {
            "dt":{
                1: {
                    "min": 1,
                    "max": 1
                },
                2: {
                    "min": 1,
                    "max": 1
                },
                3: {
                    "min": 1,
                    "max": 1
                },
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                }
            },
            "wo":{
                1: {
                    "min": 1,
                    "max": 1
                },
                2: {
                    "min": 1,
                    "max": 1
                },
                3: {
                    "min": 1,
                    "max": 1
                },
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                }
            },
            "pi": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "kc": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "uw": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "sp": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "tc": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "gh": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "ss": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "oo": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "vc": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "at": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "ef": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
            "nl": {
                4: {
                    "min": 1,
                    "max": 1
                },
                5: {
                    "min": 1,
                    "max": 1
                },
            },
        }
        with open('spells.json') as json_file:
            spell_dict = json.load(json_file)
        raids_dict = {
            "inventor":["Bioforged Quickblade","Sunken Blade","Bioforged Cog Spellblade","Fusion Magic Keyblade"],
            "heavenly":["Banished Greatsword","Dual Sinister Blades","Dual Nature Vines","Nature Spellblade"],
            "nature":["Ancient Ruins Greatsword","Earth Maul","Blessed Lightpost","Earth Staff"]
        }
        raids_leg_dict = {
            "inventor":{
                "War":"Dual Bioforged Drills",
                "Mage":"Hextech Overloaded Staff"
            },
            "heavenly": {
                "War": "Dual Godforged Blades",
                "Mage": "Godforged Greastaff"
            },
            "nature": {
                "War": "Twisted Wood Greatsword",
                "Mage": "Twisted Wood Greatstaff"
            }
        }

        # Dungeon Handler
        if True:
            dungeon_dictionary = {
                'dt': 'Desert Temple',
                'wo': 'Winter Outpost',
                'pi': 'Pirate Island',
                'kc': 'Kings Castle',
                'uw': 'The Underworld',
                'sp': 'Samurai Palace',
                'tc': 'The Canals',
                'gh': 'Ghastly Harbor',
                'ss': 'Steampunk Sewers',
                'br1': 'Boss Raids(1)',
                'br2': 'Boss Raids(2)',
                'br3': 'Boss Raids(3)',
                'br4': 'Boss Raids(4)',
                'br5': 'Boss Raids(5)',
                'br6': 'Boss Raids(6)',
                'br7': 'Boss Raids(7)',
                'br8': 'Boss Raids(8)',
                'br9': 'Boss Raids(9)',
                'br10': 'Boss Raids(10)',
                'br11': 'Boss Raids(11)',
                'br12': 'Boss Raids(12)',
                'br13': 'Boss Raids(13)',
                'br14': 'Boss Raids(14)',
                'br15': 'Boss Raids(15)',
                'br16': 'Boss Raids(16)',
                'br17': 'Boss Raids(17)',
                'br18': 'Boss Raids(18)',
                'br19': 'Boss Raids(19)',
                'br20': 'Boss Raids(20)',
                'br21': 'Boss Raids(21)',
                'br22': 'Boss Raids(22)',
                'br23': 'Boss Raids(23)',
                'br24': 'Boss Raids(24)',
                'br25': 'Boss Raids(25)',
                'br26': 'Boss Raids(26)',
                'br27': 'Boss Raids(27)',
                'br28': 'Boss Raids(28)',
                'br29': 'Boss Raids(29)',
                'br30': 'Boss Raids(30)',
                'oo': 'Orbital Outpost',
                'vc': 'Volcanic Chambers',
                'at': 'Aquatic Temple',
                'ef': 'Enchanted Forest',
                'nl': 'Northern Lands',
                'gs': 'Gilded Skies',
            }
            if dung in dungeon_dictionary:
                dungeon = dungeon_dictionary[dung]
            else:
                error = True
                errorType = "Dungeon does not exist"


        # Difficulty Handler
        diffi_dictionary = {
            "easy": 1,
            "medium": 2,
            "hard": 3,
            "insane": 4,
            "nightmare": 5,
            "med": 2,
            "ins": 4,
            "nm": 5,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5
        }
        if diffi in diffi_dictionary:
            diff = diffi_dictionary[diffi.lower()]
        else:
            diff = 5
        if True:
            difficulty_dictionary = {
                0: "Raids",
                1: "Easy",
                2: "Medium",
                3: "Hard",
                4: "Insane",
                5: "Nightmare"
            }
            if diff in difficulty_dictionary:
                difficulty = difficulty_dictionary[diff]
            else:
                error = True
                errorType = "Invalid Difficulty"
            #Dungeons above Desert & Winter don't have the first 3 Difficulties
            if dungeon != "Desert Temple" and dungeon != "Winter Outpost" and not ("Boss Raids" in dungeon):
                if diff == 1 or diff == 2 or diff == 3:
                    error = True
                    errorType = "Invalid Difficulty for this Dungeon"
            if diff < 1 or diff > 5:
                error = True
                errorType = "Invalid Difficulty"

        # Mode Handler
        if True:
            mode_dictionary = {
                "NHC": "Non-Hardcore",
                "HC": "Hardcore",
                "WVS": "Waves"
            }
            mode = mode_dictionary[mode]

        if "br" in dung:
            if 130 > userdata["stats"]["level"]:
                error = True
                errorType = "Your level is not high enough for this dungeon"
        elif lvl_dict[dung][diff] > userdata["stats"]["level"]:
            error = True
            errorType = "Your level is not high enough for this dungeon"

        # Drop Setup
        if error:
            pass
        elif "Boss Raids" in dungeon:
            tier = int(dung[2:])
            if tier < 7:
                map = "inventor"
            elif tier < 13:
                if random.randint(1,2) == 1:
                    map = "inventor"
                else:
                    map = "heavenly"
            else:
                rand = random.randint(1,3)
                if rand == 1:
                    map = "inventor"
                if rand == 2:
                    map = "heavenly"
                if rand == 3:
                    map = "nature"

            rand = random.randint(1,5)
            if rand == 1:
                rand = random.randint(1, 3)
                if rand == 1:
                    classname = "Guardian"
                elif rand == 2:
                    classname = "War"
                elif rand == 3:
                    classname = "Mage"
                if random.randint(1,2) == 1:
                    type = "Helm"
                else:
                    type = "Chest"
                if map == "inventor":
                    dropname = "Inventors " + classname + " " + type
                if map == "heavenly":
                    dropname = "Heavenly " + classname + " " + type
                if map == "nature":
                    dropname = "Nature " + classname + " " + type
                rand = random.randint(1,2000)
                if rand < 100:
                    rarity = "Purple"
                elif rand < 250:
                    rarity = "Blue"
                elif rand < 750:
                    rarity = "Green"
                else:
                    rarity = "Gray"
                dropstats = "Class: " + classname
                if classname == "War" or classname == "Mage":
                    classname = "Armor"
                dropstats += "\nPot: " + str(random.randint(int(self.brdata[str(tier)][classname][rarity]["minpot"]),int(self.brdata[str(tier)][classname][rarity]["maxpot"])))
                if classname == "Armor":
                    dropstats += "\nHealth: " + str(random.randint(int(self.brdata[str(tier)][classname][rarity]["minhp"]),int(self.brdata[str(tier)][classname][rarity]["maxhp"])))
                dropstats += "\nLvl Req: 130"
                dropstats += "\nRarity: " + rarity
                dropstats += "\nTier: " + str(tier)
            elif rand == 2:
                type = "Spell"
                rand = random.choice(spell_dict["br"][map])
                dropname = rand["name"]
                dropstats = "Class: " + rand["class"] + "Spell"
            else:
                classname = "Weapon"
                rand = random.randint(1, 2000)
                if rand < 20:
                    rarity = "Legendary"
                if rand < 100:
                    rarity = "Purple"
                elif rand < 250:
                    rarity = "Blue"
                elif rand < 750:
                    rarity = "Green"
                else:
                    rarity = "Gray"
                if rarity == "Legendary":
                    if random.randint(1,2) == 1:
                        type = "War"
                    else:
                        type = "Mage"
                    dropname = random.choice(raids_leg_dict[map][type])
                else:
                    dropname = random.choice(raids_dict[map])
                dropstats = "Class: " + classname
                dropstats += "\nPot: " + str(random.randint(int(self.brdata[str(tier)][classname][rarity]["minpot"]),
                                                            int(self.brdata[str(tier)][classname][rarity]["maxpot"])))
                dropstats += "\nLvl Req: 130"
                dropstats += "\nRarity: " + rarity
                dropstats += "\nTier: " + str(tier)
        else:
            # Get Drops
            dropname = random.choice(list(self.data[dung]))
            classname = self.data[dung][dropname]["class"]
            lvlrq = self.data[dung][dropname]["lvlrq"]
            if dung != "dt" and dung != "wo":
                if diff == 5:
                    while (("Legendary" in self.data[dung][dropname]) or ("Ultimate" in self.data[dung][dropname]) or (dropname in t3_dict.values()) or (dropname in t3_guard_dict.values()) or (int(lvlrq) % 10 < 4) or (int(lvlrq) % 10 > 7)):
                        dropname = random.choice(list(self.data[dung]))
                        lvlrq = self.data[dung][dropname]["lvlrq"]
                elif diff == 4:
                    while (("Legendary" in self.data[dung][dropname]) or ("Ultimate" in self.data[dung][dropname]) or (dropname in t3_dict.values()) or (dropname in t3_guard_dict.values()) or ((int(lvlrq) % 10 > 3) and (int(lvlrq) % 10 < 8))):
                        dropname = random.choice(list(self.data[dung]))
                        lvlrq = self.data[dung][dropname]["lvlrq"]
                dropstats = ""
                classname = self.data[dung][dropname]["class"]
            else:
                while (dropname == "Desert Fury") or (dropname == "Crystalised Greatsword"):
                    dropname = random.choice(list(self.data[dung]))
                    lvlrq = self.data[dung][dropname]["lvlrq"]
                dropstats = ""
                classname = self.data[dung][dropname]["class"]
            # Get type of weapon
            if classname != "Guardian" and classname != "DPS Armor":
                rand = random.randint(1,2000)
                if rand <= 4:
                    if dung == "gs" or dung == "nl" or dung == "ef" or dung == "at":
                        if diff == 5:
                            type = "Legendary"
                            if dung == "nl":
                                if random.randint(1,4) == 1:
                                    type = "Ultimate"
                if rand <= 20:
                    if rand <= 4:
                        if dung == "gs" or dung == "nl" or dung == "ef" or dung == "at":
                            if diff == 5:
                                pass
                    else:
                        if diff == 5:
                            type = "Legendary"
                if rand <= 100:
                    if rand <= 20:
                        if diff == 5:
                            pass
                    else:
                        type = "Purple"
                elif rand <= 250:
                    type = "Blue"
                elif rand <= 750:
                    type = "Green"
                else:
                    type = "Gray"
            # Get pot of weapon
            if classname != "Guardian" and classname != "DPS Armor":

                #Legendary Catch Code
                if type == "Legendary":
                    dropname = leg_dict[dung][classname]
                if type == "Ultimate":
                    dropname = ult_dict[dung][classname]
                min_pot = self.data[dung][dropname][type]["minpot"]
                max_pot = self.data[dung][dropname][type]["maxpot"]
                pot = random.randint(int(min_pot), int(max_pot))
                lvlrq = self.data[dung][dropname]["lvlrq"]
                dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            # Get type of guard
            if classname == "Guardian":
                rand = random.randint(1, t3chance)
                if rand == 1:
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                            dropname = t3_guard_dict[dung]
                rand = random.randint(1,2000)
                if rand <= 100:
                    type = "Purple"
                elif rand <= 250:
                    type = "Blue"
                elif rand <= 750:
                    type = "Green"
                else:
                    type = "Gray"
            # Get pot of guard
            if classname == "Guardian":
                rand = random.randint(1, 2)
                if rand == 1:
                    classname = "Guardian Helm"
                if rand == 2:
                    classname = "Guardian Chest"
                min_pot = self.data[dung][dropname][type]["minpot"]
                max_pot = self.data[dung][dropname][type]["maxpot"]
                pot = random.randint(int(min_pot), int(max_pot))
                lvlrq = self.data[dung][dropname]["lvlrq"]
                dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            # Get pot of armor
            if classname == "DPS Armor":
                rand = random.randint(1,t3chance)
                if rand == 1:
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                            dropname = t3_dict[dung]
                rand = random.randint(1,2000)
                if rand <= 100:
                    type = "Purple"
                elif rand <= 250:
                    type = "Blue"
                elif rand <= 750:
                    type = "Green"
                else:
                    type = "Gray"
            # Get pot of armor
            if classname == "DPS Armor":
                rand = random.randint(1, 4)
                if rand == 1:
                    classname = "War Helm"
                if rand == 2:
                    classname = "Mage Helm"
                if rand == 3:
                    classname = "War Chest"
                if rand == 4:
                    classname = "Mage Chest"
                min_pot = self.data[dung][dropname][type]["minpot"]
                max_pot = self.data[dung][dropname][type]["maxpot"]
                pot = random.randint(int(min_pot), int(max_pot))
                lvlrq = self.data[dung][dropname]["lvlrq"]
                min_pot = self.data[dung][dropname][type]["minhp"]
                max_pot = self.data[dung][dropname][type]["maxhp"]
                health = random.randint(int(min_pot), int(max_pot))
                dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nHealth: " + str(health) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            # Spell Handling
            rand = random.randint(1,5)
            if rand == 1:
                rand = random.choice(spell_dict[dung][str(diff)])
                dropname = rand["name"]
                dropstats = "Class: " + rand["class"] + " Spell"
                if dung == "vc" or dung == "at" or dung == "ef" or dung == "nl":
                    rand = random.randint(1, 2000)
                    if rand == 1:
                        rand = random.randint(1,2)
                        if rand == 1:
                            dropname = "Enhanced Inner Focus"
                            dropstats = "Class: Mage Spell"
                        elif rand == 2:
                            dropname = "Enhanced Inner Rage"
                            dropstats = "Class: War spell"


            #Drop 2
            dropname2 = random.choice(list(self.data[dung]))
            classname = self.data[dung][dropname2]["class"]
            lvlrq = self.data[dung][dropname2]["lvlrq"]
            if dung != "dt" and dung != "wo":
                if diff == 5:
                    while (("Legendary" in self.data[dung][dropname2]) or ("Ultimate" in self.data[dung][dropname2]) or (
                            dropname2 in t3_dict.values()) or (dropname2 in t3_guard_dict.values()) or (
                                   int(lvlrq) % 10 < 4) or (int(lvlrq) % 10 > 7)):
                        dropname2 = random.choice(list(self.data[dung]))
                        lvlrq = self.data[dung][dropname2]["lvlrq"]
                elif diff == 4:
                    while (("Legendary" in self.data[dung][dropname2]) or ("Ultimate" in self.data[dung][dropname2]) or (
                            dropname2 in t3_dict.values()) or (dropname2 in t3_guard_dict.values()) or (
                                   (int(lvlrq) % 10 > 3) and (int(lvlrq) % 10 < 8))):
                        dropname2 = random.choice(list(self.data[dung]))
                        lvlrq = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = ""
                classname = self.data[dung][dropname2]["class"]
            else:
                while (dropname2 == "Desert Fury") or (dropname2 == "Crystalised Greatsword"):
                    dropname2 = random.choice(list(self.data[dung]))
                    lvlrq = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = ""
                classname = self.data[dung][dropname2]["class"]
            # Get type of weapon
            if classname != "Guardian" and classname != "DPS Armor":
                rand = random.randint(1, 2000)

                if rand <= 4:
                    if dung == "gs" or dung == "nl" or dung == "ef" or dung == "at":
                        if diff == 5:
                            type = "Legendary"
                            if dung == "nl":
                                if random.randint(1, 4) == 1:
                                    type = "Ultimate"
                if rand <= 20:
                    if rand <= 4:
                        if dung == "gs" or dung == "nl" or dung == "ef" or dung == "at":
                            if diff == 5:
                                pass
                    else:
                        if diff == 5:
                            type = "Legendary"
                if rand <= 100:
                    if rand <= 20:
                        if diff == 5:
                            pass
                    else:
                        type = "Purple"
                elif rand <= 250:
                    type = "Blue"
                elif rand <= 750:
                    type = "Green"
                else:
                    type = "Gray"
            # Get pot of weapon
            if classname != "Guardian" and classname != "DPS Armor":

                # Legendary Catch Code
                if type == "Legendary":
                    dropname2 = leg_dict[dung][classname]
                if type == "Ultimate":
                    dropname2 = ult_dict[dung][classname]
                min_pot = self.data[dung][dropname2][type]["minpot"]
                max_pot = self.data[dung][dropname2][type]["maxpot"]
                pot = random.randint(int(min_pot), int(max_pot))
                lvlrq = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            # Get type of guard
            if classname == "Guardian":
                rand = random.randint(1, t3chance)
                if rand == 1:
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                           dropname2 = t3_guard_dict[dung]
                rand = random.randint(1,2000)
                if rand <= 100:
                    type = "Purple"
                elif rand <= 250:
                    type = "Blue"
                elif rand <= 750:
                    type = "Green"
                else:
                    type = "Gray"
            # Get pot of guard
            if classname == "Guardian":
                rand = random.randint(1, 2)
                if rand == 1:
                    classname = "Guardian Helm"
                if rand == 2:
                    classname = "Guardian Chest"
                min_pot = self.data[dung][dropname2][type]["minpot"]
                max_pot = self.data[dung][dropname2][type]["maxpot"]
                pot = random.randint(int(min_pot), int(max_pot))
                lvlrq = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            # Get type of armor
            if classname == "DPS Armor":
                rand = random.randint(1, t3chance)
                if rand == 1:
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                            dropname2 = t3_dict[dung]
                rand = random.randint(1,2000)
                if rand <= 100:
                    type = "Purple"
                elif rand <= 250:
                    type = "Blue"
                elif rand <= 750:
                    type = "Green"
                else:
                    type = "Gray"
            # Get pot of armor
            if classname == "DPS Armor":
                rand = random.randint(1,4)
                if rand == 1:
                    classname = "War Helm"
                if rand == 2:
                    classname = "Mage Helm"
                if rand == 3:
                    classname = "War Chest"
                if rand == 4:
                    classname = "Mage Chest"
                min_pot = self.data[dung][dropname2][type]["minpot"]
                max_pot = self.data[dung][dropname2][type]["maxpot"]
                pot = random.randint(int(min_pot), int(max_pot))
                lvlrq = self.data[dung][dropname2]["lvlrq"]
                min_pot = self.data[dung][dropname2][type]["minhp"]
                max_pot = self.data[dung][dropname2][type]["maxhp"]
                health = random.randint(int(min_pot), int(max_pot))
                dropstats2 = "Class: " + classname + "\nPot: " + str(pot) + "\nHealth: " + str(health) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            # Spell Handling
            rand = random.randint(1, 5)
            if rand == 1:
                rand = random.choice(spell_dict[dung][str(diff)])
                dropname2 = rand["name"]
                dropstats2 = "Class: " + rand["class"] + " Spell"
                if dung == "vc" or dung == "at" or dung == "ef" or dung == "nl":
                    rand = random.randint(1, 2000)
                    if rand == 1:
                        rand = random.randint(1,2)
                        if rand == 1:
                            dropname2 = "Enhanced Inner Focus"
                            dropstats2 = "Class: Mage Spell"
                        elif rand == 2:
                            dropname2 = "Enhanced Inner Rage"
                            dropstats2 = "Class: War Spell"
        if len(userdata["inventory"]) >= 200:
            error = True
            errorType = "Your inventory is full, please clear it: " + str(len(userdata["inventory"])) + "/" + "200"

        #Send Raid Message
        if error:
            embed = discord.Embed(
                description=errorType,
                color=0x992D22
            )
            embed.set_author(
                name="Error"
            )
            await context.send(embed=embed)
        elif "Boss Raids" in dungeon:

            embed = discord.Embed(
                description="You raided " + dungeon,
                color=0x454B1B
            )
            embed.set_author(
                name="Raid Information"
            )
            embed.add_field(
                name=dropname,
                value=dropstats,
                inline=False
            )

            length = len(userdata["inventory"])
            length2 = length + 1
            length = str(length)
            length2 = str(length2)
            userdata["inventory"][length] = {}
            userdata["inventory"][length]["name"] = dropname
            userdata["inventory"][length]["stats"] = dropstats

            embed.add_field(
                name="Other Loot",
                value="Gold: " + str(((tier-1)*666666) + 14000000) + "\nExp: 130000000",
                inline=False
            )

            userdata["stats"]["gold"] += ((tier-1)*666666) + 14000000
            userdata["stats"]["exp"] += 130000000
            while userdata["stats"]["exp"] >= level_dict[
                str(userdata["stats"]["level"])]:
                userdata["stats"]["exp"] -= level_dict[
                    str(userdata["stats"]["level"])]
                userdata["stats"]["level"] += 1
                userdata["stats"]["free"] += 1

            embed.add_field(
                name="Exp",
                value="Level: " + str(userdata["stats"]["level"]) + "\nExp: " + str(
                    userdata["stats"]["exp"]) + " / " + str(
                    level_dict[str(userdata["stats"]["level"])])
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)
        else:
            dbname = get_database()
            collection_name = dbname["userinv"]
            userinv = collection_name.find()
            length = len(userdata["inventory"])
            length2 = length+1
            length = str(length)
            length2 = str(length2)
            userdata["inventory"][length] = {}
            userdata["inventory"][length]["name"] = dropname
            userdata["inventory"][length]["stats"] = dropstats
            if mode == "Hardcore":
                userdata["inventory"][length2] = {}
                userdata["inventory"][length2]["name"] = dropname2
                userdata["inventory"][length2]["stats"] = dropstats2

            embed = discord.Embed(
                description="You raided " + dungeon + " on " + difficulty + " difficulty, in " + mode,
                color=color_dict[dung]
            )
            embed.set_author(
                name="Raid Information"
            )
            embed.add_field(
                name=dropname,
                value=dropstats,
                inline=True
            )
            if mode == "Hardcore":
                embed.add_field(
                    name=dropname2,
                    value=dropstats2,
                    inline=True
                )
            embed.add_field(
                name="Other Loot",
                value="Gold: " + str(gold_dict[dung][diff]) + "\nExp: " + str(exp_dict[dung][diff])
            )

            userdata["stats"]["gold"] += gold_dict[dung][diff]
            userdata["stats"]["exp"] += exp_dict[dung][diff]
            while userdata["stats"]["exp"] >= level_dict[str(userdata["stats"]["level"])] :
                userdata["stats"]["exp"] -= level_dict[str(userdata["stats"]["level"])]
                userdata["stats"]["level"] += 1
                userdata["stats"]["free"] += 1

            collection.drop()
            collection.insert_one(userdata)
            embed.add_field(
                name="Exp",
                value="Level: " + str(userdata["stats"]["level"]) + "\nExp: " + str(userdata["stats"]["exp"]) + " / " + str(level_dict[str(userdata["stats"]["level"])])
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="drop",
        description="drop items",
    )
    @checks.not_blacklisted()
    @app_commands.describe(
        dung="dungeon",
        diff="diff",
        mode="mode",
        quantity="quantity"
    )
    async def drop(self, context: Context, dung: str = "dt", diff: int = 1, mode: str = "NHC", quantity: int = 1) -> None:
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
        ult_dict = {
            "nl": {
                "War": "Hofund",
                "Mage": "Laevateinn"
            }
        }
        raids_dict = {
            "inventor": ["Bioforged Quickblade", "Sunken Blade", "Bioforged Cog Spellblade", "Fusion Magic Keyblade"],
            "heavenly": ["Banished Greatsword", "Dual Sinister Blades", "Dual Nature Vines", "Nature Spellblade"],
            "nature": ["Ancient Ruins Greatsword", "Earth Maul", "Blessed Lightpost", "Earth Staff"]
        }
        raids_leg_dict = {
            "inventor": {
                "War": "Dual Bioforged Drills",
                "Mage": "Hextech Overloaded Staff"
            },
            "heavenly": {
                "War": "Dual Godforged Blades",
                "Mage": "Godforged Greastaff"
            },
            "nature": {
                "War": "Twisted Wood Greatsword",
                "Mage": "Twisted Wood Greatstaff"
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
        t3chance = 5
        with open('spells.json') as json_file:
            spell_dict = json.load(json_file)


        if context.message.author.id in self.adminlist:
            embed = discord.Embed(
                description="drops from " + dung,
            )
            embed.set_author(
                name="drop debug"
            )
            for i in range(quantity):
                if "br" in dung:
                    tier = int(dung[2:])
                    if tier < 7:
                        map = "inventor"
                    elif tier < 13:
                        if random.randint(1, 2) == 1:
                            map = "inventor"
                        else:
                            map = "heavenly"
                    else:
                        rand = random.randint(1, 3)
                        if rand == 1:
                            map = "inventor"
                        if rand == 2:
                            map = "heavenly"
                        if rand == 3:
                            map = "nature"

                    rand = random.randint(1, 5)
                    if rand == 1:
                        rand = random.randint(1, 3)
                        if rand == 1:
                            classname = "Guardian"
                        elif rand == 2:
                            classname = "War"
                        elif rand == 3:
                            classname = "Mage"
                        if random.randint(1, 2) == 1:
                            type = "Helm"
                        else:
                            type = "Chest"
                        if map == "inventor":
                            dropname = "Inventors " + classname + " " + type
                        if map == "heavenly":
                            dropname = "Heavenly " + classname + " " + type
                        if map == "nature":
                            dropname = "Nature " + classname + " " + type
                        rand = random.randint(1, 2000)
                        if rand < 100:
                            rarity = "Purple"
                        elif rand < 250:
                            rarity = "Blue"
                        elif rand < 750:
                            rarity = "Green"
                        else:
                            rarity = "Gray"
                        dropstats = "Class: " + classname
                        if classname == "War" or classname == "Mage":
                            classname = "Armor"
                        dropstats += "\nPot: " + str(
                            random.randint(int(self.brdata[str(tier)][classname][rarity]["minpot"]),
                                           int(self.brdata[str(tier)][classname][rarity]["maxpot"])))
                        if classname == "Armor":
                            dropstats += "\nHealth: " + str(
                                random.randint(int(self.brdata[str(tier)][classname][rarity]["minhp"]),
                                               int(self.brdata[str(tier)][classname][rarity]["maxhp"])))
                        dropstats += "\nLvl Req: 130"
                        dropstats += "\nRarity: " + rarity
                        dropstats += "\nTier: " + str(tier)
                    elif rand == 2:
                        type = "Spell"
                        rand = random.choice(spell_dict["br"][map])
                        dropname = rand["name"]
                        dropstats = "Class: " + rand["class"] + "Spell"
                    else:
                        classname = "Weapon"
                        rand = random.randint(1, 2000)
                        if rand < 20:
                            rarity = "Legendary"
                        if rand < 100:
                            rarity = "Purple"
                        elif rand < 250:
                            rarity = "Blue"
                        elif rand < 750:
                            rarity = "Green"
                        else:
                            rarity = "Gray"
                        if rarity == "Legendary":
                            if random.randint(1, 2) == 1:
                                type = "War"
                            else:
                                type = "Mage"
                            dropname = random.choice(raids_leg_dict[map][type])
                        else:
                            dropname = random.choice(raids_dict[map])
                        dropstats = "Class: " + classname
                        dropstats += "\nPot: " + str(
                            random.randint(int(self.brdata[str(tier)][classname][rarity]["minpot"]),
                                           int(self.brdata[str(tier)][classname][rarity]["maxpot"])))
                        dropstats += "\nLvl Req: 130"
                        dropstats += "\nRarity: " + rarity
                        dropstats += "\nTier: " + str(tier)
                    embed.add_field(
                        name=dropname,
                        value=dropstats,
                        inline=False
                    )
                else:
                    # Get Drops
                    dropname = random.choice(list(self.data[dung]))
                    classname = self.data[dung][dropname]["class"]
                    lvlrq = self.data[dung][dropname]["lvlrq"]
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                            while (("Legendary" in self.data[dung][dropname]) or (
                                    "Ultimate" in self.data[dung][dropname]) or (dropname in t3_dict.values()) or (
                                           dropname in t3_guard_dict.values()) or (int(lvlrq) % 10 < 4) or (
                                           int(lvlrq) % 10 > 7)):
                                dropname = random.choice(list(self.data[dung]))
                                lvlrq = self.data[dung][dropname]["lvlrq"]
                        elif diff == 4:
                            while (("Legendary" in self.data[dung][dropname]) or (
                                    "Ultimate" in self.data[dung][dropname]) or (dropname in t3_dict.values()) or (
                                           dropname in t3_guard_dict.values()) or (
                                           (int(lvlrq) % 10 > 3) and (int(lvlrq) % 10 < 8))):
                                dropname = random.choice(list(self.data[dung]))
                                lvlrq = self.data[dung][dropname]["lvlrq"]
                        dropstats = ""
                        classname = self.data[dung][dropname]["class"]
                    else:
                        while (dropname == "Desert Fury") or (dropname == "Crystalised Greatsword"):
                            dropname = random.choice(list(self.data[dung]))
                            lvlrq = self.data[dung][dropname]["lvlrq"]
                        dropstats = ""
                        classname = self.data[dung][dropname]["class"]
                    # Get type of weapon
                    if classname != "Guardian" and classname != "DPS Armor":
                        rand = random.randint(1, 2000)
                        if rand <= 4:
                            if dung == "gs" or dung == "nl" or dung == "ef" or dung == "at":
                                if diff == 5:
                                    type = "Legendary"
                                    if dung == "gs":
                                        if random.randint(1, 4) == 1:
                                            type = "Ultimate"
                        if rand <= 20:
                            if rand <= 4:
                                if dung == "gs" or dung == "nl" or dung == "ef" or dung == "at":
                                    if diff == 5:
                                        pass
                            else:
                                if diff == 5:
                                    type = "Legendary"
                        if rand <= 100:
                            if rand <= 20:
                                if diff == 5:
                                    pass
                            else:
                                type = "Purple"
                        elif rand <= 250:
                            type = "Blue"
                        elif rand <= 750:
                            type = "Green"
                        else:
                            type = "Gray"
                    # Get pot of weapon
                    if classname != "Guardian" and classname != "DPS Armor":

                        # Legendary Catch Code
                        if type == "Legendary" or type == "Ultimate":
                            dropname = leg_dict[dung][classname]
                        min_pot = self.data[dung][dropname][type]["minpot"]
                        max_pot = self.data[dung][dropname][type]["maxpot"]
                        pot = random.randint(int(min_pot), int(max_pot))
                        lvlrq = self.data[dung][dropname]["lvlrq"]
                        dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(
                            lvlrq) + "\nRarity: " + type
                    # Get type of guard
                    if classname == "Guardian":
                        rand = random.randint(1, t3chance)
                        if rand == 1:
                            if dung != "dt" and dung != "wo":
                                if diff == 5:
                                    dropname = t3_guard_dict[dung]
                        rand = random.randint(1, 2000)
                        if rand <= 100:
                            type = "Purple"
                        elif rand <= 250:
                            type = "Blue"
                        elif rand <= 750:
                            type = "Green"
                        else:
                            type = "Gray"
                    # Get pot of guard
                    if classname == "Guardian":
                        rand = random.randint(1, 2)
                        if rand == 1:
                            classname = "Guardian Helm"
                        if rand == 2:
                            classname = "Guardian Chest"
                        min_pot = self.data[dung][dropname][type]["minpot"]
                        max_pot = self.data[dung][dropname][type]["maxpot"]
                        pot = random.randint(int(min_pot), int(max_pot))
                        lvlrq = self.data[dung][dropname]["lvlrq"]
                        dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(
                            lvlrq) + "\nRarity: " + type
                    # Get pot of armor
                    if classname == "DPS Armor":
                        rand = random.randint(1, t3chance)
                        if rand == 1:
                            if dung != "dt" and dung != "wo":
                                if diff == 5:
                                    dropname = t3_dict[dung]
                        rand = random.randint(1, 2000)
                        if rand <= 100:
                            type = "Purple"
                        elif rand <= 250:
                            type = "Blue"
                        elif rand <= 750:
                            type = "Green"
                        else:
                            type = "Gray"
                    # Get pot of armor
                    if classname == "DPS Armor":
                        rand = random.randint(1, 4)
                        if rand == 1:
                            classname = "War Helm"
                        if rand == 2:
                            classname = "Mage Helm"
                        if rand == 3:
                            classname = "War Chest"
                        if rand == 4:
                            classname = "Mage Chest"
                        min_pot = self.data[dung][dropname][type]["minpot"]
                        max_pot = self.data[dung][dropname][type]["maxpot"]
                        pot = random.randint(int(min_pot), int(max_pot))
                        lvlrq = self.data[dung][dropname]["lvlrq"]
                        min_pot = self.data[dung][dropname][type]["minhp"]
                        max_pot = self.data[dung][dropname][type]["maxhp"]
                        health = random.randint(int(min_pot), int(max_pot))
                        dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nHealth: " + str(
                            health) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type

                    embed.add_field(
                        name=dropname,
                        value=dropstats,
                        inline=False
                    )
        else:
            embed = discord.Embed(
            )
            embed.set_author(
                name="You do not have permission to use this command"
            )

        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="generate",
        description="generate item admin command",
    )
    @checks.not_blacklisted()
    async def generate(self, context: Context, dung: str=None, item: str=None, type: str=None, target: int=0) -> None:

        if target == 0:
            target = context.message.author.id
        db = get_database()
        collection = db[str(target)]
        userdata = collection.find_one()
        if context.message.author.id in self.adminlist:
            dropname = item
            classname = self.data[dung][dropname]["class"]
            if classname == "DPS Armor":
                if (random.randint(1,2) == 1):
                    if (random.randint(1, 2) == 1):
                        classname = "War Helm"
                    else:
                        classname = "War Chest"
                else:
                    if (random.randint(1, 2) == 1):
                        classname = "Mage Helm"
                    else:
                        classname = "Mage Chest"
            min_pot = self.data[dung][dropname][type]["minpot"]
            max_pot = self.data[dung][dropname][type]["maxpot"]
            pot = random.randint(int(min_pot), int(max_pot))
            lvlrq = self.data[dung][dropname]["lvlrq"]
            min_pot = self.data[dung][dropname][type]["minhp"]
            max_pot = self.data[dung][dropname][type]["maxhp"]
            health = random.randint(int(min_pot), int(max_pot))
            dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nHealth: " + str(health) + "\nLvl Req: " + str(
                lvlrq) + "\nRarity: " + type

            length = len(userdata["inventory"])
            length2 = length + 1
            length = str(length)
            length2 = str(length2)
            userdata["inventory"][length] = {}
            userdata["inventory"][length]["name"] = dropname
            userdata["inventory"][length]["stats"] = dropstats
            collection.drop()
            collection.insert_one(userdata)
            embed = discord.Embed(
                description="debug item gen",
            )
            embed.set_author(
                name="debug"
            )
            embed.add_field(
                name=dropname,
                value=dropstats,
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="give",
        description="give item admin command",
    )
    @checks.not_blacklisted()
    async def give(self, context: Context, item: str="None", itemclass: str="None", pot: int=0, health: int=0, lvlreq: int=0, rarity: str="None",target: int=0) -> None:
        if target == 0:
            target = context.message.author.id
        db = get_database()
        collection = db[str(target)]
        userdata = collection.find_one()
        if context.message.author.id in self.adminlist:
            dropname = item
            classname = itemclass
            if health == 0:
                dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nLvl Req: " + str(
                    lvlreq) + "\nRarity: " + rarity
            else:
                dropstats = "Class: " + classname + "\nPot: " + str(pot) + "\nHealth: " + str(
                    health) + "\nLvl Req: " + str(
                    lvlreq) + "\nRarity: " + rarity
            dbname = get_database()
            collection_name = dbname["userinv"]
            userinv = collection_name.find()
            length = len(userdata["inventory"])
            length2 = length + 1
            length = str(length)
            length2 = str(length2)
            userdata["inventory"][length] = {}
            userdata["inventory"][length]["name"] = dropname
            userdata["inventory"][length]["stats"] = dropstats
            collection.drop()
            collection.insert_one(userdata)
            embed = discord.Embed(
                description="debug item giver",
            )
            embed.set_author(
                name="debug"
            )
            embed.add_field(
                name=dropname,
                value=dropstats,
                inline=True
            )
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
