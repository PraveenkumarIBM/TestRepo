from selenium.webdriver.common.by import By

class line_section():
    def __init__(self,driver):
        self.driver = driver
        self.searchinvoice ="//input[@role='searchbox']"
        self.addtoconsolidate="//button[contains(text(),'Add to consolidated table')]"
        self.clickpreviewconsolidate = "//span[contains(text(),'Preview Consolidated table')]"
        self.consolidateok="//button[contains(text(),'OK')]"
        self.clicksubmit = "//button[contains(text(),'Submit')]"
        self.clickcontinue = "//button[contains(text(),'Continue')]"
        self.clickOk = "//button[contains(text(),'Ok')]"
        self.clickdashboard = "//a[contains(text(),'Dashboard')]"
        self.clickreset = "//a[contains(text(),'Reset filter')]"
        self.uncheckshowallpending = "//span[contains(text(),'Show all pending documents')]"
        self.clickdatarange = "//span[contains(text(),'Date range')]"
        self.fromdate = "//input[@id='scan-date-start']"
        self.todate = "//input[@id='scan-date-finish']"
        self.applyfilter = "//button[contains(text(),'Apply filter')]"

    def search_invoice(self,searchinvoice):
        self.driver.find_element(By.XPATH,self.searchinvoice).send_keys(searchinvoice)
    def add_to_consolidate(self):
        self.driver.find_element(By.XPATH,self.addtoconsolidate).click()

    def click_preview_consolidate(self):
        self.driver.find_element(By.XPATH,self.clickpreviewconsolidate).click()

    def click_consolidate_ok(self):
        self.driver.find_element(By.XPATH,self.consolidateok).click()

    def click_submit(self):
        self.driver.find_element(By.XPATH,self.clicksubmit).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.clickcontinue).click()

    def click_Ok(self):
        self.driver.find_element(By.XPATH,self.clickOk).click()

    def click_dashboard(self):
        self.driver.find_element(By.XPATH,self.clickdashboard).click()

    def click_reset(self):
        btn=self.driver.find_element(By.XPATH,self.clickreset)
        self.driver.execute_script("arguments[0].click()", btn)

    def uncheck_showallpending(self):
        btn=self.driver.find_element(By.XPATH,self.uncheckshowallpending)
        self.driver.execute_script("arguments[0].click()", btn)

    def click_daterange(self):
        btn=self.driver.find_element(By.XPATH,self.clickdatarange)
        self.driver.execute_script("arguments[0].click()", btn)

    def clear_fromdate(self):
        self.driver.find_element(By.XPATH,self.fromdate).clear()

    def clear_todate(self):
        self.driver.find_element(By.XPATH,self.todate).clear()
    def enter_fromdate(self,fromdate):
        self.driver.find_element(By.XPATH,self.fromdate).send_keys(fromdate)

    def enter_todate(self,todate):
        self.driver.find_element(By.XPATH,self.todate).send_keys(todate)

    def click_applyfilter(self):
        btn=self.driver.find_element(By.XPATH,self.applyfilter)
        self.driver.execute_script("arguments[0].click()", btn)








