from selenium.webdriver.common.by import By

class Result_Pending():
    def __init__(self,driver):
        self.driver=driver

        self.click_pending="//*[contains(text(),'Pending')]"
        self.result_in_pending="//*[contains(@class,'_result_count_')]"
        self.filter_table="//*[@placeholder='Filter table']"
    
    
    def Click_Pending(self):
        self.driver.find_element(By.XPATH, self.click_pending).click()
    def ResultIn_Pending(self):
        self.driver.find_element(By.XPATH, self.result_in_pending).text
    def Filter_Table(self,tbinput):
        self.driver.find_element(By.XPATH, self.filter_table).send_keys(tbinput)
    

      