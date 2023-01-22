import json
import math
import random
import lists

with open('spells.json') as json_file:
    spells = json.load(json_file)
with open('spellData.json') as json_file:
    spelldata = json.load(json_file)
with open('itemValues.json') as json_file:
    items = json.load(json_file)


dunglist = lists.t3_dungeons



#Exp Dict
if True:
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
    exp = 115500000000
    dunglist = lists.t3_dungeons
    i = 0
    for dung in dunglist:
        if i > 11:
            exp *= 1.8
            exp_dict[dung] = {}
            exp_dict[dung][4] = int(exp)
            exp *= 1.8
            exp_dict[dung][5] = int(exp)
        i += 1
    with open("exp_dict.json", "w") as outfile:
        json.dump(exp_dict, outfile)
#Gold Dict
if True:
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
    gold = 410000000
    dunglist = lists.t3_dungeons
    i = 0
    for dung in dunglist:
        if i > 11:
            gold += 150000000
            gold_dict[dung] = {}
            gold_dict[dung][4] = gold
            gold += 150000000
            gold_dict[dung][5] = gold
        i += 1
    with open("gold_dict.json", "w") as outfile:
        json.dump(gold_dict, outfile)
#Ult Dict
if True:
    dunglist = lists.get_ult_dungeons()
    ult_dict = {}
    for dung in dunglist:
        ult_dict[dung]={}
        ult_dict[dung]["War"] = ""
        ult_dict[dung]["Mage"] = ""
        itemslist = items[dung].keys()
        for key in itemslist:
            if "Ultimate" in items[dung][key]["class"]:
                if "War" in items[dung][key]["class"]:
                    ult_dict[dung]["War"] = key
                if "Mage" in items[dung][key]["class"]:
                    ult_dict[dung]["Mage"] = key
    with open("ult_dict.json", "w") as outfile:
        json.dump(ult_dict, outfile)
#Leg Dict
if True:
    dunglist = lists.t3_dungeons
    leg_dict = {
        "dt": {
            "War": "Desert Fury",
            "Mage": "Desert Fury"
        },
        "wo": {
            "War": "Crystalised Greatsword",
            "Mage": "Crystalised Greatsword"
        }
    }
    for dung in dunglist:
        leg_dict[dung]={}
        leg_dict[dung]["War"] = ""
        leg_dict[dung]["Mage"] = ""
        itemslist = items[dung].keys()
        for key in itemslist:
            if "Legend" in items[dung][key]["class"]:
                if "War" in items[dung][key]["class"]:
                    leg_dict[dung]["War"] = key
                if "Mage" in items[dung][key]["class"]:
                    leg_dict[dung]["Mage"] = key
    with open("leg_dict.json", "w") as outfile:
        json.dump(leg_dict, outfile)
#Leg List
if True:
    dunglist = lists.t3_dungeons
    leg_list = ["Desert Fury", "Crystalised Greatsword"]
    for dung in dunglist:
        leg_list.append(leg_dict[dung]["War"])
        leg_list.append(leg_dict[dung]["Mage"])
    for dung in lists.get_ult_dungeons():
        leg_list.append(ult_dict[dung]["War"])
        leg_list.append(ult_dict[dung]["Mage"])
    with open('leg_list.txt', 'w') as writer:
        writer.write(str(leg_list))
#Lvl Dict
if True:
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
    level = 195
    dunglist = lists.t3_dungeons
    i = 0
    for dung in dunglist:
        if i > 11:
            level += 5
            lvl_dict[dung] = {}
            lvl_dict[dung][4] = int(level)
            level += 5
            lvl_dict[dung][5] = int(level)
        i += 1
    with open("lvl_dict.json", "w") as outfile:
        json.dump(lvl_dict, outfile)
#Damage Gates
if True:
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
        }
    }
    t3_dict = lists.get_t3_dict()
    leg_list = lists.get_leg_list()
    t3_guard_dict = lists.get_t3_guard_dict()
    lvl_dict = lists.get_lvl_dict()
    dunglist = lists.t3_dungeons

    ins_dict = lists.get_ins_dict()
    ins_weap_dict = lists.get_ins_weap_dict()
    for dung in dunglist:
        damage_gates[dung]={}
        damage_gates[dung][4] = {}
        damage_gates[dung][5] = {}

    for dung in dunglist:
        skill = lvl_dict[dung]["5"]
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
        skill = lvl_dict[dung]["5"]
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
        skill = lvl_dict[dung]["4"]
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
        damage_gates[dung][5]["min"] = damage
    for dung in dunglist:
        skill = lvl_dict[dung]["4"]
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

    with open("damage_gates.json", "w") as outfile:
        json.dump(damage_gates, outfile)
