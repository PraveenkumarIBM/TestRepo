from selenium.webdriver.common.by import By

class Select_Cluster():
    def __init__(self,driver):
        self.driver=driver  

        self.click_Cluster= "(//label[contains(text(),'Cluster')]/following::button)[1]"
        self.input_Cluster= "//input[@id='search_input' and @placeholder='Cluster']"
        self.result_Count="//*[contains(@class,'_result_count_')]"


    def Click_Cluster(self):

         self.driver.find_element(By.XPATH, self.click_Cluster).click()
 
    def Input_Cluster(self,clst):
        self.driver.find_element(By.XPATH, self.input_Cluster).send_keys(clst)
    
    def Hit_Enter(self,enter):
        self.driver.find_element(By.XPATH, self.input_Cluster).send_keys(enter)
    
    def Result_Count(self):
        self.driver.find_element(By.XPATH, self.result_Count).click()
        
    