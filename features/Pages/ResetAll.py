from selenium.webdriver.common.by import By

class Reset_All():
    def __init__(self,driver):
        self.driver=driver

        self.reset_all="//a[contains(text(),'Reset All Filter')]"
    
    def reset_All(self):
        self.driver.find_element(By.XPATH, self.reset_all).click()
         
        