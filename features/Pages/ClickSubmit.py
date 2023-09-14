from selenium.webdriver.common.by import By

class hit_Submit_Button():
    def __init__(self,driver):
        self.driver=driver

        self.Login_Button="//button[@id='login-button']"
        self.Id_Button="//input[@id='idSIButton9']"  


    def login_button(self):
        self.driver.find_element(By.XPATH, self.Login_Button).click()


    def id_button(self):
         self.driver.find_element(By.XPATH, self.Id_Button).click()