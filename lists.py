import json

if True:

    #Leg List
    with open('leg_list.txt', 'r') as reader:
        temp_list = reader.readline()
    temp_list = temp_list.split(", ")
    leg_list = []
    for item in temp_list:
        temp = item.replace("'", '')
        temp = temp.replace("[", '')
        temp = temp.replace("]", '')
        leg_list.append(temp)

    #Leg Dict
    with open('leg_dict.json') as json_file:
        leg_dict = json.load(json_file)

    #Ult Dict
    with open('ult_dict.json') as json_file:
        ult_dict = json.load(json_file)

    #Exp Dicts
    with open('exp_dict.json') as json_file:
        exp_dict = json.load(json_file)

    #Gold Dict
    with open('gold_dict.json') as json_file:
        gold_dict = json.load(json_file)

    #Lvl Dict
    with open('lvl_dict.json') as json_file:
        lvl_dict = json.load(json_file)

    #Damage Gates
    with open('damage_gates.json') as json_file:
        damage_gates = json.load(json_file)

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
        "mk": "Glimmershine",
        'td': "Tartarus",
        'cf': "Constellation",
        'bc': "Bloodthirsty",
        'fe': "Deepfrost",
        'ad': "Shadowsteel",
        'pw': "Immortal",
        'ws': "Lichs",
        'sd': "Fortunata"
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
        "mk": "Glimmershine Guardian",
        'td': "Tartarus Guardian",
        'cf': "Constellation Guardian",
        'bc': "Bloodthirsty Guardian",
        'fe': "Deepfrost Guardian",
        'ad': "Shadowsteel Guardian",
        'pw': "Immortal Guardian",
        'ws': "Lichs Guardian",
        'sd': "Fortunata Guardian"
    }
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
        'om': 0xFFFFFF,
        'wt': 0xE8BCF0,
        'ec': 0xA020F0,
        'cl': 0x301934,
        'mk': 0x0096FF,
        'td': 0x880808,
        'cf': 0xD4AF37,
        'bc': 0x1c0000,
        'fe': 0x368BC1,
        'ad': 0x301934,
        'pw': 0x888C8D,
        'ws': 0x023020,
        'sd': 0xFFB6C1
    }
    level_dict = {"1": 84, "2": 94, "3": 107, "4": 121, "5": 136, "6": 154, "7": 174, "8": 197, "9": 223, "10": 252, "11": 285, "12": 322, "13": 364, "14": 411, "15": 464, "16": 525, "17": 593, "18": 670, "19": 758, "20": 856, "21": 967, "22": 1093, "23": 1235, "24": 1396, "25": 1578, "26": 1783, "27": 2015, "28": 2277, "29": 2573, "30": 2907, "31": 3285, "32": 3712, "33": 4195, "34": 4740, "35": 5357, "36": 6053, "37": 6840, "38": 7730, "39": 8734, "40": 9870, "41": 11153, "42": 12603, "43": 14242, "44": 16093, "45": 18185, "46": 20549, "47": 23221, "48": 26240, "49": 29651, "50": 33506, "51": 37861, "52": 42783, "53": 48345, "54": 54630, "55": 61732, "56": 69757, "57": 78826, "58": 89073, "59": 100653, "60": 113738, "61": 128524, "62": 145232, "63": 164112, "64": 185447, "65": 209555, "66": 236798, "67": 267581, "68": 302367, "69": 341675, "70": 386092, "71": 436285, "72": 493002, "73": 557092, "74": 629514, "75": 711351, "76": 803826, "77": 908324, "78": 1026406, "79": 1159839, "80": 1310618, "81": 1480998, "82": 1673528, "83": 1891087, "84": 2136929, "85": 2414729, "86": 2728644, "87": 3083368, "88": 3484206, "89": 3937153, "90": 4448983, "91": 5027350, "92": 5680906, "93": 6419424, "94": 7253949, "95": 8196962, "96": 9262568, "97": 10466702, "98": 11827373, "99": 13364931, "100": 15102372, "101": 17065681, "102": 19284220, "103": 21791168, "104": 24624020, "105": 27825143, "106": 31442411, "107": 35529925, "108": 40148815, "109": 45368161, "110": 51266022, "111": 57930605, "112": 65461584, "113": 73971590, "114": 83587897, "115": 94454323, "116": 106733385, "117": 120608726, "118": 136287860, "119": 154005282, "120": 174025968, "121": 196649344, "122": 222213759, "123": 251101548, "124": 283744749, "125": 320631567, "126": 362313671, "127": 409414448, "128": 462638326, "129": 522781309, "130": 590742879, "131": 667539453, "132": 754319582, "133": 852381128, "134": 963190674, "135": 1088405462, "136": 1229898172, "137": 1389784935, "138": 1570456976, "139": 1774616383, "140": 2005316513, "141": 2266007660, "142": 2560588656, "143": 2893465181, "144": 3269615655, "145": 3694665690, "146": 4174972230, "147": 4717718620, "148": 5331022041, "149": 6024054906, "150": 6807182044, "151": 7692115710, "152": 8692090752, "153": 9822062550, "154": 11098930681, "155": 12541791670, "156": 14172224587, "157": 16014613784, "158": 18096513575, "159": 20449060340, "160": 23107438185, "161": 26111405149, "162": 29505887818, "163": 33341653234, "164": 37676068155, "165": 42573957015, "166": 48108571427, "167": 54362685713, "168": 61429834856, "169": 69415713387, "170": 78439756127, "171": 88636924424, "172": 100159724599, "173": 113180488797, "174": 127893952341, "175": 144520166145, "176": 163307787744, "177": 184537800151, "178": 208527714170, "179": 235636317013, "180": 266269038224, "181": 300884013194, "182": 339998934909, "183": 384198796447, "184": 434144639985, "185": 490583443184, "186": 554359290797, "187": 626425998601, "188": 707861378419, "189": 799883357614, "190": 903868194104, "191": 1021371059337, "192": 1154149297051, "193": 1304188705668, "194": 1473733237405, "195": 1665318558268, "196": 1881809970843, "197": 2126445267052, "198": 2402883151769, "199": 2715257961499, "200": 3068241496494, "201": 3467112891038, "202": 3917837566873, "203": 4427156450567, "204": 5002686789141, "205": 5653036071729, "206": 6387930761054, "207": 7218361759991, "208": 8156748788790, "209": 9217126131333, "210": 10415352528406, "211": 11769348357099, "212": 13299363643522, "213": 15028280917180, "214": 16981957436413, "215": 19189611903147, "216": 21684261450556, "217": 24503215439128, "218": 27688633446215, "219": 31288155794223, "220": 35355616047472, "221": 39951846133644, "222": 45145586131017, "223": 51014512328050, "224": 57646398930696, "225": 65140430791687, "226": 73608686794606, "227": 83177816077905, "228": 93990932168033, "229": 106209753349877, "230": 120017021285361, "231": 135619234052458, "232": 153249734479278, "233": 173172199961584, "234": 195684585956590, "235": 221123582130947, "236": 249869647807970, "237": 282352702023006, "238": 319058553285997, "239": 360536165213176, "240": 407405866690889, "241": 460368629360705, "242": 520216551177596, "243": 587844702830684, "244": 664264514198673, "245": 750618901044500, "246": 848199358180285, "247": 958465274743722, "248": 1083065760460406, "249": 1223864309320259, "250": 1382966669531892, "251": 1562752336571038, "252": 1765910140325273, "253": 1995478458567558, "254": 2254890658181341, "255": 2548026443744915, "256": 2879269881431754, "257": 3253574966017882, "258": 3676539711600205, "259": 4154489874108232, "260": 4694573557742302, "261": 5304868120248800, "262": 5994500975881144, "263": 6773786102745693, "264": 7654378296102631, "265": 8649447474595973, "266": 9773875646293448, "267": 11044479480311594, "268": 12480261812752102, "269": 14102695848409872, "270": 15936046308703156, "271": 18007732328834564, "272": 20348737531583056, "273": 22994073410688848, "274": 25983302954078400, "275": 29361132338108588, "276": 33178079542062700, "277": 37491229882530848, "278": 42365089767259856, "279": 47872551437003632, "280": 54095983123814096, "281": 61128460929909920, "282": 69075160850798200, "283": 78054931761401968, "284": 88202072890384208, "285": 99668342366134160, "286": 112625226873731584, "287": 127266506367316672, "288": 143811152195067840, "289": 162506601980426624, "290": 183632460237882080, "291": 207504680068806752, "292": 234480288477751584, "293": 264962725979859264, "294": 299407880357240960, "295": 338330904803682240, "296": 382313922428160896, "297": 432014732343821760, "298": 488176647548518592, "299": 551639611729825920, "300": 623352761254703232, "301": 704388620217814528, "302": 795959140846130304, "303": 899433829156127104, "304": 1016360226946423680, "305": 1148487056449458560, "306": 1297790373787888128, "307": 1466503122380313600, "308": 1657148528289754112, "309": 1872577836967421696, "310": 2116012955773186560, "311": 2391094640023700480, "312": 2701936943226781184, "313": 3053188745846262784, "314": 3450103282806276608, "315": 3898616709571091968, "316": 4405436881815333376, "317": 4978143676451326976, "318": 5625302354389998592, "319": 6356591660460697600, "320": 7182948576320587776, "321": 8116731891242263552, "322": 9171907037103756288, "323": 10364254951927244800, "324": 11711608095677786112, "325": 13234117148115894272, "326": 14954552377370959872, "327": 16898644186429184000, "328": 19095467930664976384, "329": 21577878761651421184, "330": 24383003000666103808, "331": 27552793390752694272, "332": 31134656531550539776, "333": 35182161880652107776, "334": 39755842925136879616, "335": 44924102505404669952, "336": 50764235831107272704, "337": 57363586489151209472, "338": 64820852732740861952, "339": 73247563587997163520, "340": 82769746854436782080, "341": 93529813945513574400, "342": 105688689758430314496, "343": 119428219427026255872, "344": 134953887952539648000, "345": 152497893386369794048, "346": 172322619526597836800, "347": 194724560065055522816, "348": 220038752873512763392, "349": 248643790747069382656, "350": 280967483544188354560, "351": 317493256404932820992, "352": 358767379737574113280, "353": 405407139103458656256, "354": 458110067186908200960, "355": 517664375921206296576, "356": 584960744790962995200, "357": 661005641613788184576, "358": 746936375023580479488, "359": 844038103776646004736, "360": 953763057267609829376, "361": 1077752254712399003648, "362": 1217860047825010688000, "363": 1376181854042262077440, "364": 1555085495067755937792, "365": 1757246609426564251648, "366": 1985688668652017287168, "367": 2243828195576779112448, "368": 2535525861001760079872, "369": 2865144222931989037056, "370": 3237612971913147580416, "371": 3658502658261855502336, "372": 4134108003835896659968, "373": 4671542044334563000320, "374": 5278842510098055561216, "375": 5965092036410801651712, "376": 6740554001144206065664, "377": 7616826021292950945792, "378": 8607013404061034610688, "379": 9725925146588967075840, "380": 10990295415645534158848, "381": 12419033819679450726400, "382": 14033508216237778272256, "383": 15857864284348688105472, "384": 17919386641314015608832, "385": 20248906904684837470208, "386": 22881264802293862105088, "387": 25855829226592061620224, "388": 29217087026049029505024, "389": 33015308339435395874816, "390": 37307298423561997254656, "391": 42157247218625049264128, "392": 47637689357046302900224, "393": 53830588973462319005696, "394": 60828565540012419973120, "395": 68736279060214026600448, "396": 77671995338041847709696, "397": 87769354731987262242816, "398": 99179370847145612541952, "399": 112072689057274523549696}
    ult_dungeons = ["nl","om","wt","ec","mk","cl","td","cf","bc","fe","ad","pw","ws","sd"]
    leg_dungeons = ["at","ef","nl","gs","om","wt","ec","mk","cl","td","cf","bc","fe","ad","pw","ws","sd"]
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
                'om': 'Olympus Mons',
                'wt': 'Warlords Tomb',
                'ec': 'Emperors Colosseum',
                'cl': 'Cultists Lair',
                'mk': 'Mermaid Kingdom',
                'td': "Tartarus Domain",
                'cf': "Celestial Forge",
                'bc': "Bloodbane Caverns",
                'fe': "Frost Empire",
                'ad': "Abyssal Domain",
                'pw': "Petrified Woods",
                'ws': "Wailing Swamp",
                'sd': "Shattered Dream"
            }
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
        "mk": "Glistening",
        'td': "Hades",
        'cf': "Starry",
        'bc': "Sacrificial",
        'fe': "Frozen",
        'ad': "Darkened",
        'pw': "Mysterious",
        'ws': "Dirty",
        'sd': "Dreamers"
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
        "mk": "Scaled Shields",
        'td': "Atropos Blade",
        'cf': "Caelum",
        'bc': "Sacrificial Greatsword",
        'fe': "Deepsnow Icestaff",
        'ad': "Darksworn Aura",
        'pw': "Solidified Lifestaff",
        'ws': "Ghastly Spellorb",
        'sd': "Tehiny Mpanonofy"
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
    t3_dungeons = ["pi","kc","uw","sp","tc","ss","oo","vc","at","ef","nl","gs","om","wt","ec","mk","cl","td","cf","bc","fe","ad","pw","ws","sd"]


def get_color_dict():
    return color_dict
def get_leg_list():
    return leg_list
def get_leg_dict():
    return leg_dict
def get_ult_dict():
    return ult_dict
def get_t3_dict():
    return t3_dict
def get_t3_guard_dict():
    return t3_guard_dict
def get_exp_dict():
    return exp_dict
def get_gold_dict():
    return gold_dict
def get_lvl_dict():
    return lvl_dict
def get_level_dict():
    return level_dict
def get_damage_gates():
    return damage_gates
def get_raids_dict():
    return raids_dict
def get_raids_leg_dict():
    return raids_leg_dict
def get_ult_dungeons():
    return ult_dungeons
def get_leg_dungeons():
    return leg_dungeons
def get_dungeon_dictionary():
    return dungeon_dictionary
def get_ins_dict():
    return ins_dict
def get_ins_weap_dict():
    return ins_weap_dict