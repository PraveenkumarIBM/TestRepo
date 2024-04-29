import time
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pageObjects.HeaderSection import header_section
from pageObjects.LineSection import line_section
from utilities.customlogger import LogGen
import openpyxl
path = "./testData/Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Line = workbook.get_sheet_by_name('Line_GB')
logger = LogGen.loggen()

class LineSection():
    def __init__(self, driver):
        self.driver = driver

    def test_line_section(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Entering into Line Section",attachment_type=AttachmentType.PNG)
        for i in range(1, 6, 1):
            # time.sleep(3)
            action = ActionChains(self.driver)
            time.sleep(3)
            btn = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[' + str(i) + ']/input[1]')
            action.move_to_element(btn).click().perform()
            time.sleep(7)
            a = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[' + str( i) + ']/input[1]').get_attribute('value')
            print(a)
            if a != Line['B' + str(i)].value:
                time.sleep(3)
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[' + str(i) + ']/input[1]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                time.sleep(2)
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[' + str(i) + ']/input[1]').send_keys(Line['B' + str(i)].value)
                time.sleep(2)
                print('value is not matching..')
            elif a == Line['B' + str(i)].value:
                print(a + ' is matching')
                time.sleep(5)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Line Section fields updated",attachment_type=AttachmentType.PNG)
        linesection = line_section(self.driver)
        linesection.add_to_consolidate()
        allure.attach(self.driver.get_screenshot_as_png(), name="After added to consolidated section",attachment_type=AttachmentType.PNG)
        time.sleep(2)
        linesection.click_consolidate_ok()
        allure.attach(self.driver.get_screenshot_as_png(), name="click consolidated ok",attachment_type=AttachmentType.PNG)
        time.sleep(2)
        linesection.click_preview_consolidate()
        allure.attach(self.driver.get_screenshot_as_png(), name="preview consolidated page",attachment_type=AttachmentType.PNG)
        time.sleep(5)
        linesection.click_submit()
        allure.attach(self.driver.get_screenshot_as_png(), name="click invoice submit",attachment_type=AttachmentType.PNG)
        time.sleep(3)
        linesection.click_continue()
        time.sleep(7)
        linesection.click_Ok()
        allure.attach(self.driver.get_screenshot_as_png(), name="click ok for invoice submit",attachment_type=AttachmentType.PNG)
        time.sleep(3)

