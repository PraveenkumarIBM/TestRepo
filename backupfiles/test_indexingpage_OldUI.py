import time
import pytest
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from pageObjects.LineSection import line_section
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key
import openpyxl
import log
from pageObjects.InvoiceUpload import Upload_Document
path = "C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\testData\\Login_praveen.xlsx"
workbook = openpyxl.load_workbook(path)
Login = workbook.get_sheet_by_name('Login')
Header = workbook.get_sheet_by_name('Header')
Line = workbook.get_sheet_by_name('Line')

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_002_LineSection(BaseTest):
    def test_loginpage_verification(self):
        self.driver.execute_script("document.body.style.zoom='75%'")
        time.sleep(5)
        CI = self.driver.find_element(By.XPATH, "//span[contains(text(),'Content Intelligence')]")
        logging.info("The name of the home page is " + CI.text)
        homepagename = CI.text
        assert_that("Content Intelligence", equal_to(homepagename))
        time.sleep(5)

    def test_search_invoice(self):
        driver = self.driver
        linesection= line_section(driver)
        linesection.search_invoice(Login['D2'].value)
        time.sleep(4)
        invoiceispresent = self.driver.find_element(By.XPATH, "//td[contains(text(),'INV_CSV')]")
        abc = invoiceispresent.is_displayed()
        print(abc)
        time.sleep(3)

    def test_click_on_invoice(self):
        btn = self.driver.find_element(By.XPATH, "//a[contains(text(),'20240310_CI00000003')]")
        self.driver.execute_script("arguments[0].click()", btn)
        time.sleep(8)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(5)

    def test_verify_and_validate_KVP_section(self):
        for i in range(2, 10, 1):
            self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').click()
            a = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').get_attribute('value')
            print(a)
            if a != Header['A' + str(i)].value:
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').clear()
                time.sleep(3)
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[' + str(i) + ']/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]').send_keys(Header['A' + str(i)].value)
                print('value is not matching..')
            elif a == Header['A' + str(i)].value:
                print(a + ' is matching')
            time.sleep(10)

    def test_verify_and_validate_Line_section(self):
        for i in range(1, 11, 1):
            #time.sleep(3)
            action = ActionChains(self.driver)
            time.sleep(4)
            btn=self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td['+str(i)+']/input[1]')
            action.move_to_element(btn).click().perform()
            time.sleep(7)
            a = self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td['+str(i)+']/input[1]').get_attribute('value')
            print(a)
            if a != Line['A' + str(i)].value:
                time.sleep(5)
                self.driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td['+str(i)+']/input[1]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                time.sleep(3)
                self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td['+str(i)+']/input[1]').send_keys(Line['A' + str(i)].value)
                time.sleep(2)
                print('value is not matching..')
            elif a == Line['A' + str(i)].value:
                print(a + ' is matching')
                #time.sleep(7)









