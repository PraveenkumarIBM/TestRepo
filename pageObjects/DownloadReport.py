from selenium.webdriver.common.by import By


class DownloadReport():
    def __init__(self, driver):
        self.driver = driver
        self.clickdownload = "//body/div[@id='root']/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/div[4]/*[1]"

    def click_download(self):
        self.driver.find_element(By.XPATH,self.clickdownload).click()
