import os
import time
from datetime import datetime

import allure
import pytest

allure.suite("Upload Functionality")
import openpyxl
from allure_commons.types import AttachmentType
from hamcrest import assert_that, equal_to, contains, contains_string
from pynput.keyboard import Controller, Key
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from pageObjects.InvoiceUploadRestructure import Upload_Document_NewUI
from pageObjects.LineSection import line_section

path = "C:\\Users\\PraveenKumar187\\Documents\\S2P\\Automation\\Content Intelligence\\Pytest\\testData\\Login_Amway_NewUI.xlsx"
workbook = openpyxl.load_workbook(path)
Sheet = workbook.get_sheet_by_name('Login')

class Upload_Document_Functionality():
    def __init__(self, driver):
        self.driver = driver

    @pytest.allure
    def test_uploadinvoices_lessthan5mb(self):
        upload=Upload_Document_NewUI(self.driver)
        upload.upload_document_newUI()
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="UploadDocumentScreen", attachment_type=AttachmentType.PNG)
        browse = self.driver.find_element(By.XPATH, "//span[contains(text(),'Drop file here or click to upload')]")
        browse.click()
        time.sleep(2)
        file_path = Sheet['K2'].value
        time.sleep(3)
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        time.sleep(2)
        keyboard.release(Key.enter)
        time.sleep(4)
        allure.attach(self.driver.get_screenshot_as_png(), name="FileUploaded", attachment_type=AttachmentType.PNG)
        action = ActionChains(self.driver)
        movelement=self.driver.find_element(By.XPATH, '//div[contains(text(),"File upload successful")]')
        action.move_to_element(movelement).perform()
        time.sleep(2)
        text=self.driver.find_element(By.XPATH,'//div[contains(text(),"File upload successful")]').text
        time.sleep(1)
        assert_that(text,equal_to('File upload successful'))
        time.sleep(3)
        upload.click_continue()
        time.sleep(4)
        # self.driver.find_element(By.XPATH, "//*[contains(@placeholder,'Region')]").send_keys(Sheet['H2'].value)
        # time.sleep(2)
        # upload.Enter_region(Keys.ENTER)
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//*[contains(@placeholder,'Country')]").send_keys(Sheet['I2'].value)
        # time.sleep(2)
        # upload.Enter_CountryID(Keys.ENTER)
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//*[contains(@placeholder,'Company Code')]").send_keys(Sheet['J2'].value)
        # time.sleep(2)
        # upload.Enter_CompanyID(Keys.ENTER)
        # time.sleep(3)
        # upload.click_continue()
        # time.sleep(2)
        # upload.click_ok()
        # allure.attach(self.driver.get_screenshot_as_png(), name="FileUploadedsuccessfully", attachment_type=AttachmentType.PNG)
        # time.sleep(3)

    def test_uploadinvoices_equalto5mb(self):
        upload=Upload_Document_NewUI(self.driver)
        upload.upload_document_newUI()
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="UploadDocumentScreen", attachment_type=AttachmentType.PNG)
        browse = self.driver.find_element(By.XPATH, "//span[contains(text(),'Drop file here or click to upload')]")
        browse.click()
        time.sleep(2)
        file_path = Sheet['K2'].value
        time.sleep(3)
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        time.sleep(2)
        keyboard.release(Key.enter)
        time.sleep(4)
        allure.attach(self.driver.get_screenshot_as_png(), name="FileUploaded", attachment_type=AttachmentType.PNG)
        upload.click_continue()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[contains(@placeholder,'Region')]").send_keys(Sheet['H2'].value)
        time.sleep(2)
        upload.Enter_region(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[contains(@placeholder,'Country')]").send_keys(Sheet['I2'].value)
        time.sleep(2)
        upload.Enter_CountryID(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[contains(@placeholder,'Company Code')]").send_keys(Sheet['J2'].value)
        time.sleep(2)
        upload.Enter_CompanyID(Keys.ENTER)
        time.sleep(3)
        upload.click_continue()
        time.sleep(2)
        upload.click_ok()
        allure.attach(self.driver.get_screenshot_as_png(), name="FileUploadedsuccessfully", attachment_type=AttachmentType.PNG)
        time.sleep(3)
    def test_uploadinvoices_greaterthan5mb(self):
        upload=Upload_Document_NewUI(self.driver)
        upload.upload_document_newUI()
        time.sleep(3)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="UploadDocumentScreen", attachment_type=AttachmentType.PNG)
        browse = self.driver.find_element(By.XPATH, "//span[contains(text(),'Drop file here or click to upload')]")
        browse.click()
        time.sleep(2)
        file_path = Sheet['K3'].value
        time.sleep(3)
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        time.sleep(2)
        keyboard.release(Key.enter)
        time.sleep(4)
        allure.attach(self.driver.get_screenshot_as_png(), name="FileUploaded", attachment_type=AttachmentType.PNG)
        action = ActionChains(self.driver)
        filemove=self.driver.find_element(By.XPATH, '//div[contains(text(),"The file size should not exceed 5MB.")]')
        action.move_to_element(filemove).perform()
        time.sleep(2)
        actualtext=self.driver.find_element(By.XPATH,'//div[contains(text(),"The file size should not exceed 5MB")]').text
        print(actualtext)
        time.sleep(3)
        #expectedtext = 'The file size should not exceed 5MB.'
        #if text == "The file size should not exceed 5MB":
        #    print("Error message is matched")
        #assert_that(expectedtext,equal_to(actualtext))
        assert actualtext == 'The file size should not exceed 5MB.'
        time.sleep(2)
        enabledornot=self.driver.find_element(By.XPATH,'//button[contains(text(),"Continue")]').is_enabled()
        print(enabledornot)
        allure.attach(self.driver.get_screenshot_as_png(), name="Filegreaterthan5mb", attachment_type=AttachmentType.PNG)
        time.sleep(3)
    def test_encrypted_functionality(self):
        linesection = line_section(self.driver)
        linesection.search_invoice(Sheet['D2'].value)
        time.sleep(4)
        invoiceispresent = self.driver.find_element(By.XPATH, "//span[contains(text(),'20240324_CI00000002')]")
        abc = invoiceispresent.is_displayed()
        print(abc)
        allure.attach(self.driver.get_screenshot_as_png(), name="InvoiceSearch", attachment_type=AttachmentType.PNG)
        time.sleep(5)
        btn = self.driver.find_element(By.XPATH, "//span[contains(text(),'20240324_CI00000002')]")
        self.driver.execute_script("arguments[0].click()", btn)
        time.sleep(8)
        self.driver.execute_script("document.body.style.zoom='100%'")
        time.sleep(8)
        upload=Upload_Document_NewUI(self.driver)
        upload.click_errorpopup()
        time.sleep(3)




