import time

from selenium.webdriver.common.by import By
from pageObjects.TopFilter import TopFilter
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains


class TopFilterFunctionality():
    def __init__(self,driver):
        self.driver = driver
    def top_filter(self):
        for i in range(1,7,1):
            topfilter = TopFilter(self.driver)
            self.driver.execute_script("document.body.style.zoom='100%'")
            time.sleep(3)
            outsidecount = self.driver.find_element(By.XPATH,'//body/div[@id="root"]/div[2]/div[3]/div[1]/div[1]/div['+str(i)+']/a[1]/div[2]').text
            #outsidecount='12'
            print(outsidecount)
            time.sleep(3)
            #topfilter.get_all_count()
            self.driver.find_element(By.XPATH, '//body/div[@id="root"]/div[2]/div[3]/div[1]/div[1]/div[' + str(i) + ']/a[1]/div[2]').click()
            time.sleep(3)
            action = ActionChains(self.driver)
            textinside = self.driver.find_element(By.XPATH,'//body/div[@id="modal"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]')
            action.move_to_element(textinside).perform()
            time.sleep(2)
            textinside = self.driver.find_element(By.XPATH, '//body/div[@id="modal"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]').text
            print(textinside)
            op = textinside.split()
            list = op[2]
            print(list)
            time.sleep(3)
            if outsidecount == list:
                print("count is matching")
                assert_that(outsidecount, equal_to(list))
                time.sleep(2)
                topfilter.click_popup()
            elif outsidecount !=list:
                removezero=outsidecount.lstrip('0')
                print(removezero)
                assert_that(removezero, equal_to(list))
                print("Count is matching")
                time.sleep(2)
                topfilter.click_popup()








