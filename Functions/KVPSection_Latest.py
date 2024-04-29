import time
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.HeaderSection import header_section
from pageObjects.LineSection import line_section
from utilities.customlogger import LogGen
import openpyxl
path = "C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\testData\\Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Header = workbook.get_sheet_by_name('KVP')
control_statements = workbook.get_sheet_by_name('Control Statements')
logger = LogGen.loggen()

FrowInterval = control_statements['A2'].value
LRowInternal = control_statements['B2'].value

FrowAlphabets = control_statements['A5'].value
LRowAlphabets = control_statements['B5'].value




class KvpSection():
    def __init__(self, driver):
        self.driver = driver

    def test_kvp_section(self):
        for i in range(2, 23, 1):
            action = ActionChains(self.driver)
            btn1 = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]')
            action.move_to_element(btn1).click().perform()
            time.sleep(3)
            a = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').get_attribute('value')
            print(a)
            for j in range(FrowInterval,LRowInternal,1):
                if a != Header[chr(FrowAlphabets) + str(j)].value:
                    self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').clear()
                    time.sleep(3)
                    self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').send_keys(Header[chr(FrowAlphabets) + str(j)].value)
                    print('value is not matching..')
                elif a == Header[chr(FrowAlphabets) + str(j)].value:
                    print(a + ' is matching')
                time.sleep(5)
        header = header_section(self.driver)
        header.click_save()
        time.sleep(2)
        header.click_kvp_ok()
        time.sleep(5)

