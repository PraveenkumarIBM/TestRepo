from selenium.webdriver.common.by import By

class Click_Less1_Day():
    def __init__(self,driver):
        self.driver=driver

        self.result_Count= "//*[contains(@class,'_result_count_')]"
        self.less_1day="//*[contains(text(),'<= 1 Day')]"


    def Get_Result_Less1Day(self):
     
        self.driver.find_element(By.XPATH, self.result_Count ).text   
    
    def Click_Less_1Day(self):
        self.driver.find_element(By.XPATH, self.less_1day).click()