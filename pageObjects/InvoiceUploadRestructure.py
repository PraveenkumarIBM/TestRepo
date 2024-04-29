import time

from selenium.webdriver.common.by import By
from utilities.customlogger import LogGen

logger = LogGen.loggen()
class Upload_Document_NewUI():
    def __init__(self, driver):
        self.driver = driver
        self.upload_Document = "//button[contains(text(),'Upload document')]"
        self.browsefile = "//span[contains(text(),'Drop file here or click to upload')]"
        self.Continue ="//button[contains(text(),'Continue')]"
        self.region = "//*[contains(@placeholder,'Region')]"
        self.countryid = "//*[contains(@placeholder,'Country')]"
        self.companyid = "//*[contains(@placeholder,'Company Code')]"
        self.clickok = "//button[contains(text(),'Ok')]"
        self.clickerrorpopup ="//body/div[@id='root']/div[2]/div[1]/nav[1]/ol[1]/li[5]/div[1]/span[1]/button[1]/*[1]"


    def upload_document_newUI(self):
        btn=self.driver.find_element(By.XPATH, self.upload_Document)
        self.driver.execute_script("arguments[0].click()", btn)

    def browse_File(self):
        btn=self.driver.find_element(By.XPATH, self.browsefile)
        self.driver.execute_script("arguments[0].click()", btn)

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.Continue).click()

    def region(self, region):
        self.driver.find_element(By.XPATH, self.region).send_keys(region)

    def Enter_region(self, Enter):
        self.driver.find_element(By.XPATH, self.region).send_keys(Enter)

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

    def click_ok(self):
        btn=self.driver.find_element(By.XPATH,self.clickok)
        self.driver.execute_script("arguments[0].click()", btn)

    def click_errorpopup(self):
        btn=self.driver.find_element(By.XPATH,self.clickerrorpopup)
        self.driver.execute_script("arguments[0].click()", btn)



