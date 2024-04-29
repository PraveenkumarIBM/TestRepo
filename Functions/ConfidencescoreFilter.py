import time

from hamcrest import assert_that, equal_to
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class ConfidencescoreFilter():
    def __init__(self, driver):
        self.driver = driver

    def confidence_score_filter(self):
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 300);")
        time.sleep(4)
        for i in range(1,4,1):
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/fieldset[1]/div[' + str(i) + ']/label[1]').click()
            time.sleep(2)

        #High Filter
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/fieldset[1]/div[1]/label[1]').click()
        time.sleep(2)
        try:
            records = self.driver.find_element(By.XPATH, '//td[contains(text(),"No Records Found")]').text
            if records == 'No Records Found':
                print("No Records for High invoices")
        except NoSuchElementException:
            action = ActionChains(self.driver)
            high = self.driver.find_element(By.XPATH, '//td//span[contains(text(),"High")]')
            action.move_to_element(high).perform()
            time.sleep(1)
            invoicedisplayed = self.driver.find_element(By.XPATH, '//td//span[contains(text(),"High")]').text
            print(invoicedisplayed)
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/fieldset[1]/div[1]/label[1]').click()

        # #medium Filter
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/fieldset[1]/div[2]/label[1]').click()
        time.sleep(2)
        try:
            records = self.driver.find_element(By.XPATH, '//td[contains(text(),"No Records Found")]').text
            if records == 'No Records Found':
                print("No Records for Medium invoices")
        except NoSuchElementException:
            action = ActionChains(self.driver)
            medium = self.driver.find_element(By.XPATH, '//td//span[contains(text(),"Medium")]')
            action.move_to_element(medium).perform()
            time.sleep(2)
            invoicedisplayed = self.driver.find_element(By.XPATH, '//td//span[contains(text(),"Medium")]').text
            print(invoicedisplayed)
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/fieldset[1]/div[2]/label[1]').click()

        # Low Filter
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//body/div[@id="root"]/div[2]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/fieldset[1]/div[3]/label[1]').click()
        time.sleep(2)
        try:
            records = self.driver.find_element(By.XPATH, '//td[contains(text(),"No Records Found")]').text
            if records == 'No Records Found':
                print("No Records for Low invoices")
        except NoSuchElementException:
            action = ActionChains(self.driver)
            medium = self.driver.find_element(By.XPATH, '//td//span[contains(text(),"Low")]')
            action.move_to_element(medium).perform()
            time.sleep(2)
            invoicedisplayed = self.driver.find_element(By.XPATH, '//td//span[contains(text(),"Low")]').text
            print(invoicedisplayed)
        time.sleep(2)
        self.driver.close()


















