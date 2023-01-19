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
    "gs": "Dracani"
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
    "gs": "Dracani Royal Glaive"
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
dunglistbackup = dunglist
dunglist = dunglist[:-1]


for dung in dunglist:
    skill = lvl_dict[dung][5]
    wep = leg_dict[dung]["War"]
    arm = t3_dict[dung]
    wep = int(items[dung][wep]["Legendary"]["minpot"])
    arm = int(items[dung][arm]["Green"]["minpot"])
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
    wep = int(items[dung][wep]["Gray"]["minpot"])
    arm = int(items[dung][arm]["Gray"]["minpot"])
    helm = arm
    spell = random.choice(spells[dung]["5"])
    while spell["class"] != "Mage":
        spell = random.choice(spells[dung]["5"])
    SPELL_MULT = int(spelldata[spell["name"]]["Damage"])/100

    damage = math.floor((wep * (0.6597 + 0.013202 * skill) * ((arm + helm) * 0.0028)) * SPELL_MULT)

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


