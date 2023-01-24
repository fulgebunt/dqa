import math
import random
from utilities import shorten
from utilities import lengthen
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
import json
import lists
from utilities import get_database
from helpers import checks
from utilities import get_adminlist


class General(commands.Cog, name="dungeon"):

    #Items
    with open('itemValues.json') as json_file:
        data = json.load(json_file)
    with open('raidValues.json') as json_file:
        brdata = json.load(json_file)
    adminlist = get_adminlist()
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
        userdata["stats"]["exp"] = lengthen(str(userdata["stats"]["exp"]))

        error = False
        dungeon = "N/A"
        dung = dung.lower()
        mode = mode.upper()
        t3chance = 40
        color_dict = lists.get_color_dict()
        leg_dict = lists.get_leg_dict()
        ult_dict = lists.get_ult_dict()
        t3_dict = lists.get_t3_dict()
        t3_guard_dict = lists.get_t3_guard_dict()
        exp_dict = lists.get_exp_dict()
        gold_dict = lists.get_gold_dict()
        lvl_dict = lists.get_lvl_dict()
        level_dict = lists.get_level_dict()
        damage_gates = lists.get_damage_gates()
        raids_dict = lists.get_raids_dict()
        raids_leg_dict = lists.get_raids_leg_dict()
        ult_dungeons = lists.get_ult_dungeons()
        leg_dungeons = lists.get_leg_dungeons()
        with open('spells.json') as json_file:
            spell_dict = json.load(json_file)

        # Dungeon Handler
        if True:
            dungeon_dictionary = lists.get_dungeon_dictionary()
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
        elif lvl_dict[dung][str(diff)] > userdata["stats"]["level"]:
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
                pot = random.randint(int(self.brdata[str(tier)][classname][rarity]["minpot"]),int(self.brdata[str(tier)][classname][rarity]["maxpot"]))
                dropstats += "\nPot: " + str(pot)
                if classname == "Armor":
                    health = random.randint(int(self.brdata[str(tier)][classname][rarity]["minhp"]),int(self.brdata[str(tier)][classname][rarity]["maxhp"]))
                    dropstats += "\nHealth: " + str(health)
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
                pot = random.randint(int(self.brdata[str(tier)][classname][rarity]["minpot"]),int(self.brdata[str(tier)][classname][rarity]["maxpot"]))
                dropstats += "\nPot: " + str(pot)
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

            # Buff armor chances
            if random.randint(1,6) == 1:
                if dung != "dt" and dung != "wo":
                    if diff == 5:
                        while ((int(lvlrq) % 10 < 4) or (int(lvlrq) % 10 > 7) or classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict)):
                            dropname = random.choice(list(self.data[dung]))
                            classname = self.data[dung][dropname]["class"]
                            lvlrq = self.data[dung][dropname]["lvlrq"]
                    elif diff == 4:
                        while (((int(lvlrq) % 10 > 3) and (int(lvlrq) % 10 < 8) or classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict))):
                            dropname = random.choice(list(self.data[dung]))
                            classname = self.data[dung][dropname]["class"]
                            lvlrq = self.data[dung][dropname]["lvlrq"]
                    dropstats = ""
                    classname = self.data[dung][dropname]["class"]

            # Get type of weapon
            type = "Gray"
            if classname != "Guardian" and classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict):
                rand = random.randint(1,2000)
                if rand <= 4:
                    if dung in leg_dungeons:
                        if diff == 5:
                            type = "Legendary"
                            if dung in ult_dungeons:
                                if random.randint(1,4) == 1:
                                    type = "Ultimate"
                if rand <= 20:
                    if rand <= 4:
                        if dung in leg_dungeons:
                            if diff == 5:
                                pass
                    else:
                        if dung in leg_dungeons:
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
            if classname != "Guardian" and classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict):

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
                classname = "Spell"
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
            classname2 = self.data[dung][dropname2]["class"]
            lvlrq2 = self.data[dung][dropname2]["lvlrq"]
            if dung != "dt" and dung != "wo":
                if diff == 5:
                    while (("Legendary" in self.data[dung][dropname2]) or ("Ultimate" in self.data[dung][dropname2]) or (
                            dropname2 in t3_dict.values()) or (dropname2 in t3_guard_dict.values()) or (
                                   int(lvlrq2) % 10 < 4) or (int(lvlrq2) % 10 > 7)):
                        dropname2 = random.choice(list(self.data[dung]))
                        lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                elif diff == 4:
                    while (("Legendary" in self.data[dung][dropname2]) or ("Ultimate" in self.data[dung][dropname2]) or (
                            dropname2 in t3_dict.values()) or (dropname2 in t3_guard_dict.values()) or (
                                   (int(lvlrq2) % 10 > 3) and (int(lvlrq2) % 10 < 8))):
                        dropname2 = random.choice(list(self.data[dung]))
                        lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = ""
                classname2 = self.data[dung][dropname2]["class"]
            else:
                while (dropname2 == "Desert Fury") or (dropname2 == "Crystalised Greatsword"):
                    dropname2 = random.choice(list(self.data[dung]))
                    lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = ""
                classname2 = self.data[dung][dropname2]["class"]
            # Buff Armor Chances
            if random.randint(1, 6) == 1:
                if dung != "dt" and dung != "wo":
                    if diff == 5:
                        while ((int(lvlrq2) % 10 < 4) or (int(lvlrq2) % 10 > 7) or classname2 != "DPS Armor" or (dropname2 in t3_dict) or (dropname2 in t3_guard_dict)):
                            dropname2 = random.choice(list(self.data[dung]))
                            classname2 = self.data[dung][dropname2]["class"]
                            lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                    elif diff == 4:
                        while (((int(lvlrq2) % 10 > 3) and (int(lvlrq2) % 10 < 8) or classname2 != "DPS Armor" or (dropname2 in t3_dict) or (dropname2 in t3_guard_dict))):
                            dropname2 = random.choice(list(self.data[dung]))
                            classname2 = self.data[dung][dropname2]["class"]
                            lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                    dropstats2 = ""
                    classname2 = self.data[dung][dropname2]["class"]

            # Get type of weapon
            type2 = "Gray"
            if classname2 != "Guardian" and classname2 != "DPS Armor" or (dropname2 in t3_dict) or (dropname2 in t3_guard_dict):
                rand = random.randint(1, 4)

                if rand <= 4:
                    if dung in leg_dungeons:
                        if diff == 5:
                            type2 = "Legendary"
                            if dung in ult_dungeons:
                                if random.randint(1, 1) == 1:
                                    type2 = "Ultimate"
                if rand <= 20:
                    if rand <= 4:
                        if dung in leg_dungeons:
                            if diff == 5:
                                pass
                    else:
                        if dung in leg_dungeons:
                            pass
                        else:
                            if diff == 5:
                                type2 = "Legendary"
                if rand <= 100:
                    if rand <= 20:
                        if diff == 5:
                            pass
                    else:
                        type2 = "Purple"
                elif rand <= 250:
                    type2 = "Blue"
                elif rand <= 750:
                    type2 = "Green"
                else:
                    type2 = "Gray"
            # Get pot of weapon
            if classname2 != "Guardian" and classname2 != "DPS Armor" or (dropname2 in t3_dict) or (dropname2 in t3_guard_dict):

                # Legendary Catch Code
                if type2 == "Legendary":
                    dropname2 = leg_dict[dung][classname2]
                if type2 == "Ultimate":
                    dropname2 = ult_dict[dung][classname2]
                min_pot = self.data[dung][dropname2][type2]["minpot"]
                max_pot = self.data[dung][dropname2][type2]["maxpot"]
                pot2 = random.randint(int(min_pot), int(max_pot))
                lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = "Class: " + classname2 + "\nPot: " + str(pot2) + "\nLvl Req: " + str(lvlrq2) + "\nRarity: " + type2
            # Get type of guard
            if classname2 == "Guardian":
                rand = random.randint(1, t3chance)
                if rand == 1:
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                           dropname2 = t3_guard_dict[dung]
                rand = random.randint(1,2000)
                if rand <= 100:
                    type2 = "Purple"
                elif rand <= 250:
                    type2 = "Blue"
                elif rand <= 750:
                    type2 = "Green"
                else:
                    type2 = "Gray"
            # Get pot of guard
            if classname2 == "Guardian":
                rand = random.randint(1, 2)
                if rand == 1:
                    classname2 = "Guardian Helm"
                if rand == 2:
                    classname2 = "Guardian Chest"
                min_pot = self.data[dung][dropname2][type2]["minpot"]
                max_pot = self.data[dung][dropname2][type2]["maxpot"]
                pot2 = random.randint(int(min_pot), int(max_pot))
                lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                dropstats2 = "Class: " + classname2 + "\nPot: " + str(pot2) + "\nLvl Req: " + str(lvlrq2) + "\nRarity: " + type2
            # Get type of armor
            if classname2 == "DPS Armor":
                rand = random.randint(1, t3chance)
                if rand == 1:
                    if dung != "dt" and dung != "wo":
                        if diff == 5:
                            dropname2 = t3_dict[dung]
                rand = random.randint(1,2000)
                if rand <= 100:
                    type2 = "Purple"
                elif rand <= 250:
                    type2 = "Blue"
                elif rand <= 750:
                    type2 = "Green"
                else:
                    type2 = "Gray"
            # Get pot of armor
            if classname2 == "DPS Armor":
                rand = random.randint(1,4)
                if rand == 1:
                    classname2 = "War Helm"
                if rand == 2:
                    classname2 = "Mage Helm"
                if rand == 3:
                    classname2 = "War Chest"
                if rand == 4:
                    classname2 = "Mage Chest"
                min_pot = self.data[dung][dropname2][type2]["minpot"]
                max_pot = self.data[dung][dropname2][type2]["maxpot"]
                pot2 = random.randint(int(min_pot), int(max_pot))
                lvlrq2 = self.data[dung][dropname2]["lvlrq"]
                min_pot = self.data[dung][dropname2][type2]["minhp"]
                max_pot = self.data[dung][dropname2][type2]["maxhp"]
                health2 = random.randint(int(min_pot), int(max_pot))
                dropstats2 = "Class: " + classname2 + "\nPot: " + str(pot2) + "\nHealth: " + str(health2) + "\nLvl Req: " + str(lvlrq2) + "\nRarity: " + type2
            # Spell Handling
            rand = random.randint(1, 5)
            if rand == 1:
                rand = random.choice(spell_dict[dung][str(diff)])
                classname2 = "Spell"
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

        #Calculate damage and see if player reaches damage threshold
        with open('spellData.json') as json_file:
            spells = json.load(json_file)
        highest = userdata["stats"]["war"]
        stat = "War"
        if userdata["stats"]["mage"] > highest:
            highest = userdata["stats"]["mage"]
            stat = "Mage"
        skill = highest
        if "Boss Raids" not in dungeon:
            if (userdata["equipped"]["helmstats"] != "Empty") and stat in userdata["equipped"]["helmstats"]:
                helmstats = userdata["equipped"]["helmstats"].split("\n")
                helm = int(helmstats[1][5:])

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
            if damage >= damage_gates[dung][str(diff)]["max"]:
                cleared = True
            elif damage < damage_gates[dung][str(diff)]["min"]:
                cleared = False
                percent = 0
            else:
                percent = math.floor(((damage - damage_gates[dung][str(diff)]["min"]) / (
                        damage_gates[dung][str(diff)]["max"] - damage_gates[dung][str(diff)]["min"])) * 100)
                roll = random.randint(0,100)
                if roll <= percent:
                    cleared = True
                else:
                    cleared = False
        else:
            dmgdung = "br"
            dmgdiff = "1"
            if (userdata["equipped"]["helmstats"] != "Empty") and stat in userdata["equipped"]["helmstats"]:
                helmstats = userdata["equipped"]["helmstats"].split("\n")
                helm = int(helmstats[1][5:])
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
            if damage >= damage_gates[dmgdung][str(dmgdiff)]["max"]:
                cleared = True
            elif damage < damage_gates[dmgdung][str(dmgdiff)]["min"]:
                cleared = False
                percent = 0
            else:
                percent = math.floor(((damage - damage_gates[dmgdung][str(dmgdiff)]["min"]) / (
                            damage_gates[dmgdung][str(dmgdiff)]["max"] - damage_gates[dmgdung][str(dmgdiff)]["min"]))*100)
                roll = random.randint(0,100)
                if roll <= percent:
                    cleared = True
                else:
                    cleared = False
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
        elif "Boss Raids" in dungeon and cleared == True:

            embed = discord.Embed(
                description="You raided " + dungeon,
                color=0x454B1B
            )
            embed.set_author(
                name="Raid Information"
            )
            length = len(userdata["inventory"])
            length2 = length + 1
            length = str(length)
            length2 = str(length2)
            userdata["inventory"][length] = {}
            userdata["inventory"][length]["name"] = dropname
            userdata["inventory"][length]["stats"] = dropstats
            dropstats = 0
            dropstats = "Class: " + classname
            dropstats += "\nPot: " + str(shorten(pot))
            if classname == "Armor":
                dropstats += "\nHealth: " + str(shorten(health))

            dropstats += "\nLvl Req: 130"
            dropstats += "\nRarity: " + rarity
            dropstats += "\nTier: " + str(tier)
            embed.add_field(
                name=dropname,
                value=dropstats,
                inline=False
            )
            embed.add_field(
                name="Other Loot",
                value="Gold: " + str(shorten(((tier-1)*666666) + 14000000)) + "\nExp: 130m",
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
            collection.drop()


            embed.add_field(
                name="Exp",
                value="Level: " + str(userdata["stats"]["level"]) + "\nExp: " + str(
                    shorten(userdata["stats"]["exp"])) + " / " + str(
                    shorten(level_dict[str(userdata["stats"]["level"])]))
            )
            if userdata["stats"]["exp"] > 9000000000000000000:
                userdata["stats"]["exp"] = shorten(userdata["stats"]["exp"])
            collection.insert_one(userdata)
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)
        elif cleared == True:
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
            if "Spell" in classname:
                pass
            elif ("Helm" in classname or "Chest" in classname) and "Guardian" not in classname:
                dropstats = "Class: " + classname + "\nPot: " + str(shorten(pot)) + "\nHealth: " + str(
                    shorten(health)) + "\nLvl Req: " + str(lvlrq) + "\nRarity: " + type
            else:
                dropstats = "Class: " + classname + "\nPot: " + str(shorten(pot)) + "\nLvl Req: " + str(
                    lvlrq) + "\nRarity: " + type

            embed.add_field(
                name=dropname,
                value=dropstats,
                inline=True
            )
            if mode == "Hardcore":

                if "Spell" in classname2:
                    pass
                elif ("Helm" in classname2 or "Chest" in classname2) and "Guardian" not in classname2:
                    dropstats2 = "Class: " + classname2 + "\nPot: " + str(shorten(pot2)) + "\nHealth: " + str(
                        shorten(health2)) + "\nLvl Req: " + str(lvlrq2) + "\nRarity: " + type2
                else:
                    dropstats2 = "Class: " + classname2 + "\nPot: " + str(shorten(pot2)) + "\nLvl Req: " + str(lvlrq2) + "\nRarity: " + type2
                embed.add_field(
                    name=dropname2,
                    value=dropstats2,
                    inline=True
                )
            embed.add_field(
                name="Other Loot",
                value="Gold: " + str(shorten(gold_dict[dung][str(diff)])) + "\nExp: " + str(shorten(exp_dict[dung][str(diff)]))
            )

            userdata["stats"]["gold"] += gold_dict[dung][str(diff)]
            print(userdata["stats"])
            userdata["stats"]["exp"] += exp_dict[dung][str(diff)]
            while userdata["stats"]["exp"] >= level_dict[str(userdata["stats"]["level"])] :
                userdata["stats"]["exp"] -= level_dict[str(userdata["stats"]["level"])]
                userdata["stats"]["level"] += 1
                userdata["stats"]["free"] += 1


            embed.add_field(
                name="Exp",
                value="Level: " + str(userdata["stats"]["level"]) + "\nExp: " + str(shorten(userdata["stats"]["exp"])) + " / " + str(shorten(level_dict[str(userdata["stats"]["level"])]))
            )
            collection.drop()
            if userdata["stats"]["exp"] > 9000000000000000000:
                userdata["stats"]["exp"] = shorten(userdata["stats"]["exp"])
            collection.insert_one(userdata)
            embed.set_footer(
                text=f"Requested by {context.author}"
            )
            await context.send(embed=embed)
        else:
            if "Boss Raids" in dungeon:
                embed = discord.Embed(
                    description="You failed " + dungeon,
                    color=0x454B1B
                )
                embed.set_author(
                    name="Raid Information"
                )

                embed.set_footer(
                    text=f"Requested by {context.author}"
                )
                await context.send(embed=embed)
            else:
                embed = discord.Embed(
                    description="You failed " + dungeon + " on " + difficulty + " difficulty, in " + mode,
                    color=color_dict[dung]
                )
                embed.set_author(
                    name="Raid Information"
                )
                userdata["stats"]["exp"] += math.floor(exp_dict[dung][str(diff)]*percent/100)
                while userdata["stats"]["exp"] >= level_dict[str(userdata["stats"]["level"])]:
                    userdata["stats"]["exp"] -= level_dict[str(userdata["stats"]["level"])]
                    userdata["stats"]["level"] += 1
                    userdata["stats"]["free"] += 1

                embed.add_field(
                    name="Exp",
                    value="Level: " + str(userdata["stats"]["level"]) + "\nExp: " + str(
                        shorten(userdata["stats"]["exp"])) + " / " + str(shorten(level_dict[str(userdata["stats"]["level"])]))
                )
                collection.drop()
                if userdata["stats"]["exp"] > 9000000000000000000:
                    userdata["stats"]["exp"] = shorten(userdata["stats"]["exp"])
                collection.insert_one(userdata)
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
        leg_dict = lists.get_leg_dict()
        t3_dict = lists.get_t3_dict()
        t3_guard_dict = lists.get_t3_guard_dict()
        raids_dict = lists.get_raids_dict()
        raids_leg_dict = lists.get_raids_leg_dict()
        ult_dungeons = lists.get_ult_dungeons()
        leg_dungeons = lists.get_leg_dungeons()
        t3chance = 40
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
                    #Buff armor chances
                    if random.randint(1, 6) == 1:
                        if dung != "dt" and dung != "wo":
                            if diff == 5:
                                while ((int(lvlrq) % 10 < 4) or (int(lvlrq) % 10 > 7) or classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict)):
                                    dropname = random.choice(list(self.data[dung]))
                                    classname = self.data[dung][dropname]["class"]
                                    lvlrq = self.data[dung][dropname]["lvlrq"]
                            elif diff == 4:
                                while (((int(lvlrq) % 10 > 3) and (int(lvlrq) % 10 < 8) or classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict))):
                                    dropname = random.choice(list(self.data[dung]))
                                    classname = self.data[dung][dropname]["class"]
                                    lvlrq = self.data[dung][dropname]["lvlrq"]
                            dropstats = ""
                            classname = self.data[dung][dropname]["class"]

                    # Get type of weapon
                    type = "Gray"
                    if classname != "Guardian" and classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict):
                        rand = random.randint(1, 2000)
                        if rand <= 4:
                            if dung in leg_dungeons:
                                if diff == 5:
                                    type = "Legendary"
                                    if dung in ult_dungeons:
                                        if random.randint(1, 4) == 1:
                                            type = "Ultimate"
                        if rand <= 20:
                            if rand <= 4:
                                if dung in leg_dungeons:
                                    if diff == 5:
                                        pass
                            else:
                                if dung in leg_dungeons:
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

                    if classname != "Guardian" and classname != "DPS Armor" or (dropname in t3_dict) or (dropname in t3_guard_dict):

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
        userdata["stats"]["exp"] = lengthen(str(userdata["stats"]["exp"]))
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
            if userdata["stats"]["exp"] > 9000000000000000000:
                userdata["stats"]["exp"] = shorten(userdata["stats"]["exp"])
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
        userdata["stats"]["exp"] = lengthen(str(userdata["stats"]["exp"]))
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
            if userdata["stats"]["exp"] > 9000000000000000000:
                userdata["stats"]["exp"] = shorten(userdata["stats"]["exp"])
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
