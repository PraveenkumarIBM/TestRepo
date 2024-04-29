import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.ResetFilters import ResestFilterDashboard


class ResetFilters():
    def __init__(self,driver):
        self.driver = driver
    def reset_filters(self):
        self.driver.execute_script("document.body.style.zoom='100%'")
        reset = ResestFilterDashboard(self.driver)
        reset.click_settings()
        time.sleep(3)
        #Unselect all checkbox and reset
        for i in range(1, 5, 1):
            uncheck=self.driver.find_element(By.XPATH,'//body/div[3]/ul[1]/fieldset[1]/fieldset['+str(i)+']/div[1]/label[1]')
            uncheck.click()
            time.sleep(3)
        time.sleep(2)
        reset.click_resetfilter()
        time.sleep(2)
        #unselect all filter
        for i in range(1, 5, 1):
            uncheck=self.driver.find_element(By.XPATH,'//body/div[3]/ul[1]/fieldset[1]/fieldset['+str(i)+']/div[1]/label[1]')
            uncheck.click()
            time.sleep(3)
        time.sleep(2)
        #Check one by one checkbox and apply filter
        for i in range(1, 5, 1):
            time.sleep(3)
            uncheck=self.driver.find_element(By.XPATH,'//body/div[3]/ul[1]/fieldset[1]/fieldset['+str(i)+']/div[1]/label[1]')
            uncheck.click()
            time.sleep(2)
            text=self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[3]/ul[1]/fieldset[1]/fieldset['+str(i)+']/div[1]/label[1]/span[1]').text
            print(text)
            reset.click_applyfilters()
            time.sleep(2)
            text1=self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/ul[1]/li[1]').text
            print(text1)
            time.sleep(1)
            firstelement = text
            secondelement = text1
            S1=firstelement.split()
            S2 = S1[0]
            if secondelement.__contains__(S2):
                print("yes")
            time.sleep(2)
            uncheck.click()
            time.sleep(2)
        reset.click_resetfilter()




