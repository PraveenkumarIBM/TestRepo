from selenium.webdriver.common.by import By
class Open_Document():

    def __init__(self,driver):
        self.driver=driver


        self.searchButton="//input[@placeholder='Filter table']"
       
    

    def search_Button(self,scanid):
        self.driver.find_element(By.XPATH, self.searchButton).send_keys(scanid)


    def click_Pop_Document(self,sid):
        def clickpopdocuemnt(sid):
            return "//a[contains(@title,'"+sid+"')]"
        self.driver.find_element(By.XPATH, clickpopdocuemnt()).click()

    
