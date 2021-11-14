import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from lib.selenium import Selenium
from lib.utils import writeFile
from constants import *

selenium = Selenium()
driver = selenium.driver

def get_data(url):
    try :
        driver.get(url)
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

        data['url'] = url

        return data
    except Exception as e:
        print('>>>>>>>>>>>>>>>>')
        print(e)

    
def main():
    result = list(map(get_data, URLS))
    cleaned_data = list(filter(None, result))
    data_str = json.dumps(cleaned_data)
    writeFile(file_path='data.json', data=data_str)
    driver.quit()

main()