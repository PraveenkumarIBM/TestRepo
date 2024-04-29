import time

from selenium.webdriver.common.by import By
from pageObjects.SearchFunctionality import SearchFunctionality
from utilities.customlogger import LogGen
logger = LogGen.loggen()


class SearchFunctionalityverification():
    def __init__(self, driver):
        self.driver = driver

    def search_functionality(self):
        search=SearchFunctionality(self.driver)
        time.sleep(1)
        search.search_invoice("20240117_CI00000052")
        time.sleep(1)
        invoiceispresent = self.driver.find_element(By.XPATH, "//span[contains(text(),'INV_CSV')]")
        abc = invoiceispresent.is_displayed()
        print(abc)
        time.sleep(1)
        self.driver.close()







