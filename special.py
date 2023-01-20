import json
import math
import random

damage_gates = {
    "dt": {
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
    "wo": {
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
            "max": 1142389651831
        },
    },
    "vc": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 7628358177706
        },
    },
    "at": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 37088616556535
        },
    },
    "ef": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 188668177076686
        },
    },
    "nl": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 904717196044072
        },
    },
    "gs": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 4495306129317689
        },
    },
    "om": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 4495306129317689
        },
    },
    "wt": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 4495306129317689
        },
    },
    "ec": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 4495306129317689
        },
    },
    "cl": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 4495306129317689
        },
    },
    "mk": {
        4: {
            "min": 1,
            "max": 1
        },
        5: {
            "min": 1,
            "max": 4495306129317689
        },
    }
}
leg_list = ["Desert Fury", "Crystalised Greatsword", "Soulstealer Greatsword", "Staff of the Gods",
            "Beast Master War Scythe", "Beast Master Spell Scythe", "Dual Phoenix Daggers", "Phoenix Greatstaff",
            "Sakura Katana", "Sakura Greatstaff", "Overlords Rageblade", "Overlords Manablade", "Kraken Slayer",
            "Sea Serpent Wings", "Inventors Greatsword", "Inventors Spellblade", "Galactic Dual Blades",
            "Galactic Pike", "Lava Kings Warscythe", "Lava Kings Spell Daggers", "Sea Kings Greatstaff",
            "Sea Kings Trident", "Eldenbark Greatsword", "Eldenbark Greatstaff", "Mjolnir", "Gungnir", "Hofund",
            "Laevateinn", "Gildenscale Oath and Aegis", "Daybreak and Gildensong", "Fulmen", "Fuscina",
            "Shattered Skies", "Stormy Seas", "Ghost Kings Halberd", "Ghost Kings Tome",
            "Gladius Imperialis", "Magicus Imperialis", "Storsvero", "Vigamenn", "Theospathia",
            "Theosevis", "Demonic Sacrificial Dagger", "Demonic Ritual Wand", "Uhenyth", "Shuggoth",
            "Glimmershine Battlesword",
            "Glimmershine Artefact", "Myrimidion", "Myriminion"]
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
    },
    "om": {
        "War": "Fuscina",
        "Mage": "Fulmen"
    },
    "wt": {
        "War": "Ghost Kings Halberd",
        "Mage": "Ghost Kings Tome"
    },
    "ec": {
        "War": "Gladius Imperialis",
        "Mage": "Magicus Imperialis"
    },
    "cl": {
        "War": "Demonic Sacrificial Dagger",
        "Mage": "Demonic Ritual Wand"
    },
    "mk": {
        "War": "Glimmershine Battlesword",
        "Mage": "Glimmershine Artefact"
    }
}
ult_dict = {
    "nl": {
        "War": "Hofund",
        "Mage": "Laevateinn"
    },
    "om": {
        "War": "Stormy Seas",
        "Mage": "Shattered Skies"
    },
    "wt": {
        "War": "Storsvero",
        "Mage": "Vigamenn"
    },
    "ec": {
        "War": "Theospathia",
        "Mage": "Theosevis"
    },
    "cl": {
        "War": "Uhenyth",
        "Mage": "Shuggoth"
    },
    "mk": {
        "War": "Myrimidion",
        "Mage": "Myriminion"
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
    "gs": "Gildenscale",
    "om": "Thunder Gods",
    "wt": "Soulshard",
    "ec": "Gods Chosen",
    "cl": "Demonic Cultists",
    "mk": "Glimmershine"
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
    "gs": "Gildenscale Guardian",
    "om": "Thunder Gods Guardian",
    "wt": "Soulshard Guardian",
    "ec": "Gods Chosen Guardian",
    "cl": "Demonic Cultists Guardian",
    "mk": "Glimmershine Guardian"
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
    },
    "om": {
        4: 207900000000,
        5: 374220000000
    },
    "wt": {
        4: 673596000000,
        5: 1212472800000,
    },
    "ec": {
        4: 2182451040000,
        5: 3928411872000,
    },
    "cl": {
        4: 7071141369600,
        5: 12728054465280,
    },
    "mk": {
        4: 22910498037504,
        5: 41238896467507,
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
    },
    "om": {
        4: 450000000,
        5: 550000000
    },
    "wt": {
        4: 600000000,
        5: 750000000
    },
    "ec": {
        4: 900000000,
        5: 1050000000
    },
    "cl": {
        4: 1200000000,
        5: 1350000000
    },
    "mk": {
        4: 1500000000,
        5: 1650000000
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
    },
    "om": {
        4: 200,
        5: 205
    },
    "wt": {
        4: 210,
        5: 215
    },
    "ec": {
        4: 220,
        5: 225
    },
    "cl": {
        4: 230,
        5: 235
    },
    "mk": {
        4: 240,
        5: 245
    }

}
dunglist = list(t3_dict.keys())
with open('spells.json') as json_file:
    spells = json.load(json_file)
with open('spellData.json') as json_file:
    spelldata = json.load(json_file)
with open('itemValues.json') as json_file:
    items = json.load(json_file)

ins_dict = {
    "pi": "Pirate Kings",
    "kc": "Barbaric",
    "uw": "Tribal",
    "sp": "Samurai",
    "tc": "Rouge",
    "gh": "Raiders",
    "ss": "Titanium",
    "oo": "Space",
    "vc": "Burned",
    "at": "Aquatic",
    "ef": "Fungal",
    "nl": "Midgardian",
    "gs": "Dracani",
    "om": "Olympian",
    "wt": "Skeleton",
    "ec": "Centurion",
    "cl": "Initiates",
    "mk": "Glistening"
}
ins_weap_dict = {
    "pi": "Cultist Blade",
    "kc": "Heavenly Greatsword",
    "uw": "Hopes Triumph",
    "sp": "Amethyst Spelldagger",
    "tc": "Giant Royal Axe",
    "gh": "Dual Ocean Fists",
    "ss": "Hextech Polearm",
    "oo": "Void Spell Blade",
    "vc": "Lava Spellblade",
    "at": "Aquatic Defender",
    "ef": "Enchanted Shard Spell Dagger",
    "nl": "Viking Hatchets",
    "gs": "Dracani Royal Glaive",
    "om": "Heavenly Staff and Tome",
    "wt": "Cracked Greatsword",
    "ec": "Praetorian Godstaff",
    "cl": "Demonstaff",
    "mk": "Scaled Shields"
}

for dung in dunglist:
    skill = lvl_dict[dung][5]
    wep = leg_dict[dung]["War"]
    arm = t3_dict[dung]
    wep = int(items[dung][wep]["Legendary"]["minpot"])
    arm = int(items[dung][arm]["Blue"]["minpot"])
    helm = arm
    spell = random.choice(spells[dung]["5"])
    while spell["class"] != "Mage":
        spell = random.choice(spells[dung]["5"])
    SPELL_MULT = int(spelldata[spell["name"]]["Damage"])/100

    damage = math.floor((wep * (0.6597 + 0.013202 * skill) * ((arm + helm) * 0.0028)) * SPELL_MULT)

    damage_gates[dung][5]["max"] = damage
    print(damage)
dunglistbackup = dunglist
dunglist = dunglist[:-1]


for dung in dunglist:
    skill = lvl_dict[dung][5]
    wep = leg_dict[dung]["War"]
    arm = t3_dict[dung]
    wep = int(items[dung][wep]["Legendary"]["minpot"])
    arm = int(items[dung][arm]["Gray"]["minpot"])
    helm = arm
    spell = random.choice(spells[dung]["4"])
    while spell["class"] != "Mage":
        spell = random.choice(spells[dung]["4"])
    SPELL_MULT = int(spelldata[spell["name"]]["Damage"])/100

    damage = math.floor((wep * (0.6597 + 0.013202 * skill) * ((arm + helm) * 0.0028)) * SPELL_MULT)


    dung = dunglistbackup[dunglist.index(dung)+1]
    damage_gates[dung][4]["min"] = damage

dunglist = dunglistbackup

for dung in dunglist:
    skill = lvl_dict[dung][4]
    wep = ins_weap_dict[dung]
    arm = ins_dict[dung]
    wep = int(items[dung][wep]["Green"]["minpot"])
    arm = int(items[dung][arm]["Green"]["minpot"])
    helm = arm
    spell = random.choice(spells[dung]["5"])
    while spell["class"] != "Mage":
        spell = random.choice(spells[dung]["5"])
    SPELL_MULT = int(spelldata[spell["name"]]["Damage"])/100

    damage = math.floor((wep * (0.6597 + 0.013202 * skill) * ((arm + helm) * 0.0028)) * SPELL_MULT)
    print(damage)
    damage_gates[dung][5]["min"] = damage
for dung in dunglist:
    skill = lvl_dict[dung][4]
    wep = ins_weap_dict[dung]
    arm = ins_dict[dung]
    wep = int(items[dung][wep]["Green"]["minpot"])
    arm = int(items[dung][arm]["Green"]["minpot"])
    helm = arm
    spell = random.choice(spells[dung]["5"])
    while spell["class"] != "Mage":
        spell = random.choice(spells[dung]["5"])
    SPELL_MULT = int(spelldata[spell["name"]]["Damage"])/100

    damage = math.floor((wep * (0.6597 + 0.013202 * skill) * ((arm + helm) * 0.0028)) * SPELL_MULT)

    damage_gates[dung][4]["max"] = damage

with open("temp.json", "w") as outfile:
    json.dump(damage_gates, outfile)
print(damage_gates)


