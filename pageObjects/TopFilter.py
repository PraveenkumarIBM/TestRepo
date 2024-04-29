from selenium.webdriver.common.by import By


class TopFilter():
    def __init__(self,driver):
        self.driver = driver
        self.getallcount = "//body/div[@id='root']/div[2]/div[3]/div[1]/div[1]/div[1]/a[1]/div[2]"
        self.getallcountinside ="//body/div[@id='modal']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]"
        self.clickpopup="//button[@aria-label='Close']"
    def get_all_count(self):
        self.driver.find_element(By.XPATH,self.getallcount).click()
    def get_all_count_inside(self):
        self.driver.find_element(By.XPATH,self.getallcountinside)
    def click_popup(self):
        self.driver.find_element(By.XPATH,self.clickpopup).click()

