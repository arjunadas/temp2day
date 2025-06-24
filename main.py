from flask import Flask
import pymongo
app = Flask(__name__)

host = "localhost"
port = 27017
user = "admin"
password = "qwerty11"
db_name = "testdb"

def mongodb_connect(mongo_collection_name):
    mongo_client = pymongo.MongoClient(
        f"mongodb://{user}:{password}@{host}:{port}/{db_name}"
    )
    mongo_db = mongo_client[db_name]
    mongo_collection = mongo_db[mongo_collection_name]
    return mongo_collection

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
