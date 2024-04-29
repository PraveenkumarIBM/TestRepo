from selenium.webdriver.common.by import By


class SearchFunctionality():
    def __init__(self, driver):
        self.driver = driver
        self.searchinvoice = "//input[@role='searchbox']"

    def search_invoice(self, searchinvoice):
        self.driver.find_element(By.XPATH, self.searchinvoice).send_keys(searchinvoice)
