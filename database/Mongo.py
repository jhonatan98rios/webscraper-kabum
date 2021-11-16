from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")  

mongo_key = config["MONGO_KEY"]
class Database:
    def __init__(self) -> None:
        self.client = MongoClient(mongo_key)
        self.db = self.client['SmartGadget']
        self.collection = self.db['KabumScrape']
        
        print(self.collection)

    def saveProduct(self, _id, product_name, price):
        try:
            res = self.collection.insert({
                "id": _id,
                "name": product_name,
                "price": price
            }).inserted_id
            return res

        except Exception as err:
            print(err)