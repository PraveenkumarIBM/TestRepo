import time
import pytest
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Functions.LoginPageVerification import LoginpageVerification
from utilities.customlogger import LogGen
from selenium.webdriver.support import expected_conditions as EC
from Functions.FileUpload import Upload_Document_Functionality
from selenium.webdriver import ActionChains
from pynput.keyboard import Controller, Key
import openpyxl
import logging
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.InvoiceUploadRestructure import Upload_Document_NewUI

path = "./testData/Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Sheet = workbook.get_sheet_by_name('Login')


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifyDocumentUploadFunctionality(BaseTest):

    def test_TC04_upload_invoices_greaterthan15mb_pdf(self):
         #Login verification
         loginpage=LoginpageVerification(self.driver)
         loginpage.test_loginpage_verification()
         #Upload document verification.
         uploaddocument = Upload_Document_Functionality(self.driver)
         uploaddocument.test_encrypted_functionality()

