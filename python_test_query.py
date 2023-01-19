# Get the database using the method we defined in pymongo_test_insert file
from utilities import get_database
import pymongo
dbname = get_database()
collection_name = dbname["392837642036969473"]
userinv = (collection_name.find())
print(list(userinv))
print(dbname.list_collection_names())