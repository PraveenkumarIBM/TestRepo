from selenium.webdriver.common.by import By

class Upload_Document():
    def __init__(self, driver):
        self.driver = driver
        self.upload_Document = "//*[contains(text(),'Upload Document')]"
        self.browsefile = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
        self.clusterid = "//*[contains(@id,'clusterId')]"
        self.click_ud_Windows = "//*[contains(text(),'UPLOAD DOCUMENT')]"
        self.countryid = "//*[contains(@id,'countryId')]"
        self.companyid = "//*[contains(@id,'companyId')]"
        self.clickSubmit = "//button[contains(text(),'SUBMIT')]"
        self.closebutton = "//*[@aria-label='Close']"
        self.clickok ="//button[contains(text(),'Ok')]"

    def upload_document(self):
        btn=self.driver.find_element(By.XPATH, self.upload_Document)
        self.driver.execute_script("arguments[0].click()", btn)

    def browse_File(self):
        btn=self.driver.find_element(By.XPATH, self.browsefile)
        btn.send_keys()
        #btn.send_keys("C:\Users\PraveenKumar187\Documents\S2P\Automation\Content Intelligence\pythonProject\features\INVPO(10).pdf")
        #self.driver.execute_script("arguments[0].click()", btn)

    def Cluster_ID(self, clid):
        self.driver.find_element(By.XPATH, self.clusterid).send_keys(clid)

    def Enter_clusterId(self, clEnter):
        self.driver.find_element(By.XPATH, self.clusterid).send_keys(clEnter)

    def Click_UD_windows(self):
        btn=self.driver.find_element(By.XPATH, self.click_ud_Windows)
        self.driver.execute_script("arguments[0].click()", btn)

    def CountryID(self, country):
        self.driver.find_element(By.XPATH, self.countryid).send_keys(country)

    def Enter_CountryID(self, countryEnter):
        self.driver.find_element(By.XPATH, self.countryid).send_keys(countryEnter)

    def CompanyId(self, cid):
        self.driver.find_element(By.XPATH, self.companyid).send_keys(cid)

    def Enter_CompanyID(self, companyEnter):
        self.driver.find_element(By.XPATH, self.companyid).send_keys(companyEnter)

    def Click_Submit(self):
        btn=self.driver.find_element(By.XPATH, self.clickSubmit)
        self.driver.execute_script("arguments[0].click()", btn)

    def Close_Button(self):
        btn=self.driver.find_element(By.XPATH, self.closebutton)
        self.driver.execute_script("arguments[0].click()", btn)

    def click_ok(self):
        btn=self.driver.find_element(By.XPATH,self.clickok)
        self.driver.execute_script("arguments[0].click()", btn)


