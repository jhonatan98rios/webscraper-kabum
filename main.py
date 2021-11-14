import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from lib.selenium import Selenium
from lib.utils import writeFile
from constants import *


from database.Mongo import Database

selenium = Selenium()
driver = selenium.driver

def get_data(products):
    try :
        driver.get(products['url'])
        time.sleep(3)
        data = {}

        name = selenium.query(f"//h1[@itemprop='name']")
        price = selenium.query(f"//h4[@itemprop='price']")

        if name.text != None:
            data['name'] = name.text
        else:
            data['name'] = 'Indisponível'

        if price.text != None:
            data['price'] = price.text
        else:
            data['price'] = 'Indisponível'

        data['id'] = products['id']
        data['url'] = products['url']

        return data
    except Exception as e:
        print('>>>>>>>>>>>>>>>>')
        print(e)

    
def main():
    result = list(map(get_data, PRODUCTS))
    cleaned_data = list(filter(None, result))

    db = Database()

    for prod in cleaned_data:
    
        db.saveProduct(
            _id=prod['id'],
            product_name=prod['name'],
            price=prod['price']
        )

    driver.quit()

main()