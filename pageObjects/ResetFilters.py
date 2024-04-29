from selenium.webdriver.common.by import By


class ResestFilterDashboard():
    def __init__(self,driver):
        self.driver = driver
        self.clicksettings = "//body/div[@id='root']/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/div[3]/span[1]/span[1]/div[1]/button[1]"
        self.clickreserfilters ="//button[contains(text(),'Reset filters')]"
        self.clickapplyfilter="//button[contains(text(),'Apply filters')]"
    def click_settings(self):
        self.driver.find_element(By.XPATH,self.clicksettings).click()
    def click_resetfilter(self):
        self.driver.find_element(By.XPATH,self.clickreserfilters).click()

    def click_applyfilters(self):
        self.driver.find_element(By.XPATH,self.clickapplyfilter).click()

