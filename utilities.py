import math

from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://aurelianus:16201Dd!@dungeonquest.1g1dj.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['dqa']

def get_adminlist():
    return [421086209431961600, 383710782686232597, 426402208515620864]

def shorten(num: int = 0):
    digits = len(str(num))
    num = str(num)
    if digits == 0:
        return num
    if digits == 1:
        return num
    if digits == 2:
        return num
    if digits == 3:
        return num
    if digits == 4:
        shortened = num[0:1] + "." + num[1:2] + "k"
        return shortened
    if digits == 5:
        shortened = num[0:2] + "." + num[2:3] + "k"
        return shortened
    if digits == 6:
        shortened = num[0:3] + "." + num[3:4] + "k"
        return shortened
    if digits == 7:
        shortened = num[0:1] + "." + num[1:2] + "m"
        return shortened
    if digits == 8:
        shortened = num[0:2] + "." + num[2:3] + "m"
        return shortened
    if digits == 9:
        shortened = num[0:3] + "." + num[3:4] + "m"
        return shortened
    if digits == 10:
        shortened = num[0:1] + "." + num[1:2] + "b"
        return shortened
    if digits == 11:
        shortened = num[0:2] + "." + num[2:3] + "b"
        return shortened
    if digits == 12:
        shortened = num[0:3] + "." + num[3:4] + "b"
        return shortened
    if digits == 13:
        shortened = num[0:1] + "." + num[1:2] + "t"
        return shortened
    if digits == 14:
        shortened = num[0:2] + "." + num[2:3] + "t"
        return shortened
    if digits == 15:
        shortened = num[0:3] + "." + num[3:4] + "t"
        return shortened
    if digits == 16:
        shortened = num[0:1] + "." + num[1:2] + "qa"
        return shortened
    if digits == 17:
        shortened = num[0:2] + "." + num[2:3] + "qa"
        return shortened
    if digits == 18:
        shortened = num[0:3] + "." + num[3:4] + "qa"
        return shortened
    if digits == 19:
        shortened = num[0:1] + "." + num[1:2] + "qi"
        return shortened
    if digits == 20:
        shortened = num[0:2] + "." + num[2:3] + "qi"
        return shortened
    if digits == 21:
        shortened = num[0:3] + "." + num[3:4] + "qi"
        return shortened
    if digits == 22:
        shortened = num[0:1] + "." + num[1:2] + "sx"
        return shortened
    if digits == 23:
        shortened = num[0:2] + "." + num[2:3] + "sx"
        return shortened
    if digits == 24:
        shortened = num[0:3] + "." + num[3:4] + "sx"
        return shortened
    if digits == 25:
        shortened = num[0:1] + "." + num[1:2] + "sp"
        return shortened
    if digits == 26:
        shortened = num[0:2] + "." + num[2:3] + "sp"
        return shortened
    if digits == 27:
        shortened = num[0:3] + "." + num[3:4] + "sp"
        return int(shortened)

def lengthen(num: str = "0"):
    if "k" in num:
        num = num[:-1]
        num = num.replace('.','')
        return int(num)*100
    if "m" in num:
        num = num[:-1]
        num = num.replace('.','')
        return int(num)*100000
    if "b" in num:
        num = num[:-1]
        num = num.replace('.','')
        return int(num)*100000000
    if "t" in num:
        num = num[:-1]
        num = num.replace('.','')
        return int(num)*100000000000
    if "qa" in num:
        num = num[:-2]
        num = num.replace('.','')
        return int(num)*100000000000000
    if "qi" in num:
        num = num[:-2]
        num = num.replace('.','')
        return int(num)*100000000000000000
    if "sx" in num:
        num = num[:-2]
        num = num.replace('.','')
        return int(num)*100000000000000000000
    if "sp" in num:
        num = num[:-2]
        num = num.replace('.','')
        return int(num)*100000000000000000000
    else:
        return int(num)

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()

#write to file
#collection.drop()
#collection.insert_one(userdata)
#db = get_database()
#collection = db[str(userid)]
#userdata = collection.find_one()
