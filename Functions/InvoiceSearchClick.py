import time
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from pageObjects.LineSection import line_section
from utilities.customlogger import LogGen
import openpyxl

path = "./testData/Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Login = workbook.get_sheet_by_name('Login')

logger = LogGen.loggen()


class InvoiceSearchClick():
    def __init__(self, driver):
        self.driver = driver

    def test_invoicesearch_click(self):
        driver = self.driver
        linesection = line_section(driver)
        linesection.search_invoice(Login['D2'].value)
        time.sleep(4)
        invoiceispresent = self.driver.find_element(By.XPATH, "//span[contains(text(),'"+Login['D2'].value+"')]")
        abc = invoiceispresent.is_displayed()
        print(abc)
        allure.attach(self.driver.get_screenshot_as_png(), name="InvoiceSearch", attachment_type=AttachmentType.PNG)
        time.sleep(5)
        btn = self.driver.find_element(By.XPATH, "//span[contains(text(),'"+Login['D2'].value+"')]")
        self.driver.execute_script("arguments[0].click()", btn)
        time.sleep(8)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(8)
