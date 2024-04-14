'''
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseMethod:
    '''
    '''
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qproxy.org/auth/login"

    def go_to_site(self):
        '''
        '''
        return self.driver.get(self.base_url)