from selenium.webdriver.common.by import By

class Upload_Document():
    def __init__(self,driver):
        self.driver=driver

        self.upload_Document="//*[contains(text(),'Upload Document')]"
        self.browse_file="//button[contains(text(),'Browse File')]"
        self.clusterid="//*[contains(@id,'clusterId')]"
        self.click_ud_Windows="//*[contains(text(),'UPLOAD DOCUMENT')]"
        self.countryid="//*[contains(@id,'countryId')]"
        self.companyid="//*[contains(@id,'companyId')]"
        self.clickSubmit="//button[contains(text(),'SUBMIT')]"
        self.closebutton="//*[@aria-label='Close']"
    
    def upload_document(self):
        self.driver.find_element(By.XPATH, self.upload_Document ).click()

    def browse_File(self):
        self.driver.find_element(By.XPATH, self.browse_file).click()
    
    def Cluster_ID(self,clid):
        self.driver.find_element(By.XPATH, self.clusterid).send_keys(clid)

    def Enter_clusterId(self,clEnter):
        self.driver.find_element(By.XPATH, self.clusterid).send_keys(clEnter)

    def Click_UD_windows(self):
         self.driver.find_element(By.XPATH, self.click_ud_Windows ).click()

    def CountryID(self,country):
        self.driver.find_element(By.XPATH, self.countryid).send_keys(country)

    def Enter_CountryID(self,countryEnter):
        self.driver.find_element(By.XPATH, self.countryid).send_keys(countryEnter)

    def CompanyId(self,cid):
        self.driver.find_element(By.XPATH, self.companyid).send_keys(cid)

    def Enter_CompanyID(self,companyEnter):
        self.driver.find_element(By.XPATH, self.companyid).send_keys(companyEnter)
    
    def Click_Submit(self):
        self.driver.find_element(By.XPATH, self.clickSubmit).click()
   
    def Close_Button(self):
        self.driver.find_element(By.XPATH, self.closebutton).click()
   
   
   