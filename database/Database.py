import psycopg2
from database.credentials import STRING_CONNECTION


class Database:
    def __init__(self):
        #postgres://apnohjpr:Z119OyefeR0bRnTRfd2YLQEukDQDcFPd@kesavan.db.elephantsql.com/apnohjpr
        self.conn = psycopg2.connect("dbname=apnohjpr user=apnohjpr password=Z119OyefeR0bRnTRfd2YLQEukDQDcFPd host=kesavan.db.elephantsql.com")
        self.db = self.conn.cursor()


    def saveProduct(self, _id, product_name, price):
        try:
            self.db.execute(f"INSERT INTO products (id, product_name, price ) values ( {_id}, {product_name}, {price})")
            
            records = self.db.fetchall()
            print(records)

        except Exception as err:
            print(err)

    def test(self):
        try:
            self.db.execute("INSERT INTO products ( id, product_name, price ) values ( 'aaa', 'note aleatorio', 'R$ 10' )")
            records = self.db.fetchall()
            print(records)

        except Exception as err:
            print(err)

