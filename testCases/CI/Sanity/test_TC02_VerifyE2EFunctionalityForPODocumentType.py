import time
import pytest
import allure
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from Functions.InvoiceValidation import InvoiceValidation
from Functions.KVPSection import KvpSection
from Functions.LineSection import LineSection
from Functions.LoginPageVerification import LoginpageVerification
from Functions.InvoiceSearchClick import InvoiceSearchClick
from pageObjects.LineSection import line_section
from pageObjects.HeaderSection import header_section
from selenium.webdriver.common.keys import Keys
from utilities.customlogger import LogGen
from pynput.keyboard import Controller, Key
import openpyxl

path = "./testData/Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Login = workbook.get_sheet_by_name('Login')
Header = workbook.get_sheet_by_name('Header_GB')
Line = workbook.get_sheet_by_name('Line_GB')


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


logger = LogGen.loggen()


class Test_VerifyE2EFunctionalityforINVPO(BaseTest):

    def test_TC01_documentprocessing_for_pdf_with_doctype_invpo(self):
        # Login verification
        loginverification = LoginpageVerification(self.driver)
        loginverification.test_loginpage_verification()
        # invoice Search
        invoicesearch = InvoiceSearchClick(self.driver)
        invoicesearch.test_invoicesearch_click()
        # Verify the KVP section
        kvpseaction = KvpSection(self.driver)
        kvpseaction.test_kvp_section()
        #verify the line section
        linesection = LineSection(self.driver)
        linesection.test_line_section()
        # veify the invoice completed status verification
        invoicevalidation = InvoiceValidation(self.driver)
        invoicevalidation.test_invoice_validation()









