from selenium.webdriver.common.by import By
class header_section():
    def __init__(self,driver):
        self.driver = driver
        self.save ="//button[contains(text(),'Save')]"
        self.ok = "//button[contains(text(),'Ok')]"
    def click_save(self):
        self.driver.find_element(By.XPATH,self.save).click()
    def click_kvp_ok(self):
        self.driver.find_element(By.XPATH,self.ok).click()
