from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Selenium():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(
            chrome_options=self.chrome_options, 
            service=Service(ChromeDriverManager().install())
        )
    

    def query(self, xpath):
        try:
            data = self.driver.find_element_by_xpath(xpath)
            return data
        except Exception as e:
            return None
