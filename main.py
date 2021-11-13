import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from lib.selenium import Selenium
from lib.utils import writeFile
from constants import *

selenium = Selenium()
driver = selenium.get_driver()

def get_data(url):
    try :
        driver.get(url)
        time.sleep(3)
        name = driver.find_element(By.XPATH, '//h1')
        price = driver.find_element_by_xpath(f"//h4[@itemprop='price']")
        data = {
            'name': name.text,
            'price': price.text,
            'url': url
        }
        return data
    except Exception as e:
        print(e)
        return str(e)
    
def main():
    result = list(map(get_data, URLS))
    data_str = json.dumps(result)
    writeFile(file_path='data.txt', data=data_str)
    driver.quit()

main()