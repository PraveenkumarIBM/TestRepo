import time
import pytest
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Controller, Key
import openpyxl
from pageObjects.InvoiceUpload import Upload_Document
path = "C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\testData\\Login_praveen.xlsx"
workbook = openpyxl.load_workbook(path)
Sheet = workbook.get_sheet_by_name('Sheet1')

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_001_Login(BaseTest):
    def test_loginpage_verification(self):
        self.driver.execute_script("document.body.style.zoom='75%'")
        time.sleep(5)
        CI = self.driver.find_element(By.XPATH, "//span[contains(text(),'Content Intelligence')]")
        logging.info("The name of the home page is " + CI.text)
        homepagename = CI.text
        assert_that("Content Intelligence", equal_to(homepagename))
        time.sleep(5)

    def test_uploadinvoices(self):
        for a in range(2, 11, 1):
            driver = self.driver
            UploadDocument = Upload_Document(driver)
            UploadDocument.upload_document()
            time.sleep(3)
            self.driver.execute_script("document.body.style.zoom='100%'")
            time.sleep(3)
            # UploadDocument.Cluster_ID('EU')
            UploadDocument.Cluster_ID(Sheet['G' + str(a)].value)
            time.sleep(1)
            UploadDocument.Enter_clusterId(Keys.ENTER)

            time.sleep(1)
            UploadDocument.Click_UD_windows()
            time.sleep(1)
            # UploadDocument.CountryID('BE')
            UploadDocument.CountryID(Sheet['H' + str(a)].value)
            time.sleep(1)
            UploadDocument.Enter_CountryID(Keys.ENTER)
            time.sleep(1)
            UploadDocument.Click_UD_windows()
            time.sleep(1)
            # UploadDocument.CompanyId('2990')
            UploadDocument.CompanyId(Sheet['I' + str(a)].value)
            time.sleep(1)
            UploadDocument.Enter_CompanyID(Keys.ENTER)
            time.sleep(1)
            UploadDocument.Click_UD_windows()
            time.sleep(4)
            browse = self.driver.find_element(By.XPATH, "//button[contains(text(),'Browse File')]")
            browse.click()
            file_path = Sheet['J' + str(a)].value
            time.sleep(3)
            keyboard = Controller()
            keyboard.type(file_path)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
            UploadDocument.Click_Submit()
            time.sleep(7)
            UploadDocument.click_ok()
            time.sleep(4)





