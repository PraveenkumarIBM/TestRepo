import time
import allure
import allure
from allure_commons.types import AttachmentType
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.HeaderSection import header_section
from pageObjects.LineSection import line_section
from utilities.customlogger import LogGen
import openpyxl
path = "./testData/Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Header = workbook.get_sheet_by_name('Header_GB')
logger = LogGen.loggen()

class KvpSection():
    def __init__(self, driver):
        self.driver = driver

    def test_kvp_section(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Invoice Indexing page",attachment_type=AttachmentType.PNG)
        for i in range(2, 17, 1):
            action = ActionChains(self.driver)
            btn1 = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]')
            action.move_to_element(btn1).click().perform()
            time.sleep(3)
            a = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').get_attribute('value')
            print(a)
            if a != Header['B' + str(i)].value:
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').clear()
                time.sleep(3)
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').send_keys(Header['B' + str(i)].value)
                print('value is not matching..')
            elif a == Header['B' + str(i)].value:
                print(a + ' is matching')
            time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="After Entering All KVP Fields",attachment_type=AttachmentType.PNG)
        header = header_section(self.driver)
        header.click_save()
        allure.attach(self.driver.get_screenshot_as_png(), name="After Saving All KVP Fields",attachment_type=AttachmentType.PNG)
        time.sleep(2)
        header.click_kvp_ok()
        allure.attach(self.driver.get_screenshot_as_png(), name="Click Ok for KVP Fields", attachment_type=AttachmentType.PNG)
        time.sleep(5)

