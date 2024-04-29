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
Login = workbook.get_sheet_by_name('Login')
logger = LogGen.loggen()

class InvoiceValidation():
    def __init__(self, driver):
        self.driver = driver

    def test_invoice_validation(self):
        linesection = line_section(self.driver)
        linesection.click_dashboard()
        time.sleep(4)
        linesection.click_reset()
        time.sleep(2)
        linesection.uncheck_showallpending()
        time.sleep(1)
        linesection.click_daterange()
        time.sleep(2)
        linesection.clear_fromdate()
        time.sleep(2)
        linesection.enter_fromdate('03/13/2024')
        time.sleep(2)
        linesection.clear_todate()
        time.sleep(2)
        linesection.enter_todate('03/21/2024')
        time.sleep(2)
        linesection.click_applyfilter()
        time.sleep(5)
        linesection.search_invoice(Login['D2'].value)
        time.sleep(3)
        invoiceispresent = self.driver.find_element(By.XPATH, "//span[contains(text(),'INV_CSV')]")
        abc = invoiceispresent.is_displayed()
        print(abc)
        allure.attach(self.driver.get_screenshot_as_png(), name="completedInvoice", attachment_type=AttachmentType.PNG)
        time.sleep(5)

