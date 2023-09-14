from selenium.webdriver.common.by import By

class Check_Document():
    def __init__(self,driver):
        self.driver=driver

        
        self.filter_table="//*[@placeholder='Filter table']"
        self.select_items="//td[contains(@class,'_statusBlock_eslwx_')]/a[1]"
    


    def Filter_Table(self,tbinput):
        self.driver.find_element(By.XPATH, self.filter_table).send_keys(tbinput)
    def Clear_Filter_tble(self):
        self.driver.find_element(By.XPATH, self.filter_table).clear()
    def Select_Items(self):
        self.driver.find_element(By.XPATH,self.select_items).click()

      