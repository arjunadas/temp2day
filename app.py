import pymongo

MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_PORT = int(os.getenv("MONGODB_PORT"))
MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")

def mongodb_connect(mongo_collection_name: str) -> pymongo.collection.Collection:
    mongo_client = pymongo.MongoClient(f'mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DB_NAME}')
    mongo_db = mongo_client[MONGODB_DB_NAME]
    mongo_collection = mongo_db[mongo_collection_name]
    return mongo_collection
