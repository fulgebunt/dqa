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
