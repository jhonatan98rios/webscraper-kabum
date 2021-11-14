from pymongo import MongoClient

class Database:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb://jhonatan98rios:maiarios@cluster0-shard-00-00.t0gwi.gcp.mongodb.net:27017/&ssl=true&ssl_cert_reqs=CERT_NONE")
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