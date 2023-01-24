import math

bases = {
    "wo": {
        "l": [1092, 1208]
    },
    "pi": {
        "l": [3277, 3626],
        "c": [199, 221]
    },
    "kc": {
        "l": [13300, 14700],
        "c": [655, 725]
    },
    "uw": {
        "l": [22800, 25200],
        "c": [1615, 1785]
    },
    "sp": {
        "l": [53200, 58800],
        "c": [3705, 4095]
    },
    "tc": {
        "l": [115900, 128100],
        "c": [7410, 8190]
    },
    "gh": {
        "l": [228000, 252000],
        "c": [16150, 17850]
    },
    "ss": {
        "l": [460750, 509250],
        "c": [38950, 43050]
    },
    "oo": {
        "l": [2992500, 3307500],
        "c": [209000, 231000]
    },
    "vc": {
        "l": [6412500, 7087500],
        "c": [503500, 556500]
    },
    "at": {
        "l": [14250000, 15750000],
        "c": [1216000, 1344000]
    },
    "ef": {
        "l": [30020000, 33180000],
        "c": [2531750, 2798250]
    },
    "nl": {
        "l": [63270000, 69930000],
        "c": [5510000, 6090000]
    },
    "nlu": {
        "l": [69930000, 75524400]
    },
    "gs": {
        "l": [132525000, 146475000],
        "c": [10735000, 11865000]
    },
    "gsu": {
        "l": [0, 0]
    },
}

ups = {
    "pi": {
        "l": [332, 368],
        "c": [123, 137]
    },
    "kc": {
        "l": [807, 893],
        "c": [285, 315]
    },
    "uw": {
        "l": [1330, 1470],
        "c": [437, 483]
    },
    "sp": {
        "l": [2137, 2363],
        "c": [731, 809]
    },
    "tc": {
        "l": [4180, 4620],
        "c": [1349, 1491]
    },
    "gh": {
        "l": [10450, 11550],
        "c": [2660, 2940]
    },
    "ss": {
        "l": [22800, 25200],
        "c": [4655, 5145]
    },
    "oo": {
        "l": [75525, 83475],
        "c": [20900, 23100]
    },
    "vc": {
        "l": [123500, 136500],
        "c": [34200, 37800]
    },
    "at": {
        "l": [161500, 178500],
        "c": [47025, 51975]
    },
    "ef": {
        "l": [285000, 315000],
        "c": [86925, 96075]
    },
    "nl": {
        "l": [418000, 462000],
        "c": [133000, 147000]
    },
    "nlu": {
        "l": [462000, 498960]
    },
    "gs": {
        "l": [807500, 892500],
        "c": [332500, 367500]
    },
    "gsu": {
        "l": [0, 0]
    },
}


def calculate_probability_for_base(base, MAX_UPS, pot_to_aim, upsRange):
    minimum_ups_for_base = math.ceil((pot_to_aim - base) / 10)
    if minimum_ups_for_base > MAX_UPS:  # Not Possible
        return 0
    else:
        r = max(1, min(MAX_UPS - minimum_ups_for_base + 1, upsRange))  # r for range, clamp it
        return r


def calc_prob(dung, t, pot_to_aim):
    MIN_BASE = bases[dung][t][0]
    MAX_BASE = bases[dung][t][1]
    MIN_UPS = ups[dung][t][0]
    MAX_UPS = ups[dung][t][1]

    pot_to_aim = int(pot_to_aim)

    baseRange = MAX_BASE - MIN_BASE + 1
    upsRange = MAX_UPS - MIN_UPS + 1
    totalRange = baseRange * upsRange

    minimum_base = max(pot_to_aim - MAX_UPS * 10, MIN_BASE)

    prob = 0
    for base in range(minimum_base, MAX_BASE + 1):
        prob += calculate_probability_for_base(base, MAX_UPS, pot_to_aim, upsRange)

    prob /= totalRange
    return prob


while True:
    dungeon = input("Enter dungeon: ")
    if not dungeon in bases:
        print("eeeee???")
        continue

    t = input("Enter type (l/c): ")
    if not (t == "c") and not (t == "l"):
        print("eeeee???")
        continue

    pot = input("Pot: ")

    prob = calc_prob(dungeon, t, pot)
    print("1 in " + str(1 / prob) + " drops")
    if t == "l" and dungeon == "nlu" or t == "l" and dungeon == "gsu":
        print("1 in " + str(1 / prob * 13875 / 7) + " runs\n")
    elif t == "l" and dungeon == "nl" or t == "l" and dungeon == "gs":
        print("1 in " + str(1 / prob * 555) + " runs\n")
    elif t == "l":
        print("1 in " + str(1 / prob * 1000 / 3) + " runs\n")
    elif t == "c":
        print("1 in " + str(1 / prob * 3 / 0.00117 / 2) + " runs\n")